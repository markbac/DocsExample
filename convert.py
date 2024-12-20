"""
This script processes markdown files containing various diagram code blocks, generating images from those diagrams and updating the markdown to reference the images.

Required tools:
1. mermaid-cli (for generating Mermaid diagrams)
   Install with: `npm install -g @mermaid-js/mermaid-cli`
2. PlantUML (for generating PlantUML diagrams)
   Install with: `brew install plantuml` (macOS) or download from: http://plantuml.com/download
3. vega-cli (for generating Vega diagrams)
   Install with: `npm install -g vega-cli`
4. bytefield-svg (for generating Bytefield diagrams)
   Install with: `npm install -g bytefield-svg`
5. wavedrom-cli (for generating WaveDrom diagrams)
   Install with: `npm install -g wavedrom-cli`
6. nwdiag (for generating network and rack diagrams)
   Install with: `pip install nwdiag`
7. graphviz (for generating Graphviz diagrams)
   Install with: `sudo apt install graphviz` or equivalent package manager.

Usage:
1. Place your markdown files with supported diagram code blocks in the input directory.
2. Run the script with the following command:
   python convert.py -i <input_directory> -o <output_directory> [--debug]

   -i, --input_dir: Directory containing markdown files to process
   -o, --output_dir: Directory where the processed markdown files and images will be saved
   --debug: Optional flag to enable detailed logging

Note: The script will process all markdown files in the input directory recursively, 
generate images for the supported diagram code blocks, and save them in the output directory.
The markdown files will be updated to reference the generated images.
"""
import os
import re
import shutil
import subprocess
import logging
import json
import requests
from pathlib import Path
import argparse

# Custom log formatter for coloured log levels
class ColouredFormatter(logging.Formatter):
    COLOURS = {
        'DEBUG': '\033[0;34m',    # Blue
        'INFO': '\033[0;32m',     # Green
        'WARNING': '\033[0;33m',  # Yellow
        'ERROR': '\033[0;31m',    # Red
        'RESET': '\033[0m'        # Reset
    }

    def format(self, record):
        level_colour = self.COLOURS.get(record.levelname, self.COLOURS['RESET'])
        time_colour = self.COLOURS['DEBUG']  # Time always blue
        reset_colour = self.COLOURS['RESET']
        record.levelname = f"{level_colour}{record.levelname}{reset_colour}"
        record.asctime = f"{time_colour}{self.formatTime(record)}{reset_colour}"
        return super().format(record)

# Set up logging
def setup_logging(debug, log_file=None):
    log_level = logging.DEBUG if debug else logging.INFO
    handlers = []

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColouredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
    handlers.append(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        handlers.append(file_handler)

    logging.basicConfig(level=log_level, handlers=handlers)

# Check tool availability
def check_tools(tools):
    missing_tools = []
    for tool in tools:
        if not shutil.which(tool):
            missing_tools.append(tool)
    if missing_tools:
        logging.error(f"Missing required tools: {', '.join(missing_tools)}")
        raise RuntimeError(f"Install the missing tools: {', '.join(missing_tools)}")

# Validate output directory
def validate_output_dir(output_dir):
    output_path = Path(output_dir)
    if output_path.name == "docs":
        raise ValueError("Output directory cannot be named 'docs' directly. Please use a different name.")

# Generate nwdiag using Kroki service
def generate_nwdiag_with_kroki(code, output_file):
    kroki_url = "https://kroki.io/nwdiag/png"
    try:
        response = requests.post(kroki_url, data=code, headers={"Content-Type": "text/plain"}, timeout=30)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            f.write(response.content)
        logging.info(f"Generated nwdiag diagram using Kroki: {output_file}")
    except requests.RequestException as e:
        logging.error(f"Error generating nwdiag diagram via Kroki: {e}")
        raise

# Process Markdown files
def process_markdown_file(input_file, output_file, output_dir, metadata):
    logging.info(f"Processing markdown file: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    output_content = content
    base_filename = input_file.stem
    relative_path = input_file.relative_to("docs-src").parent
    diagram_subdir = output_dir / relative_path

    diagram_index = 0

    diagram_patterns = {
        "mermaid": {
            "pattern": r'```mermaid(.*?)```',
            "command": lambda temp, image: ["mmdc", "-i", str(temp), "-o", str(image)],
            "extension": "png"
        },
        "plantuml": {
            "pattern": r'```plantuml(.*?)```',
            "command": lambda temp, image: ["plantuml", "-tpng", str(temp)],
            "extension": "png"
        },
        "vega": {
            "pattern": r'```vega(.*?)```',
            "command": lambda temp, image: ["vg2png", str(temp), "-o", str(image)],
            "extension": "png"
        },
        "bytefield": {
            "pattern": r'```bytefield(.*?)```',
            "command": lambda temp, image: ["bytefield-svg", "-i", str(temp), "-o", str(image)],
            "extension": "svg"
        },
        "wavedrom": {
            "pattern": r'```wavedrom(.*?)```',
            "command": lambda temp, image: ["wavedrom-cli", "-i", str(temp), "-p", str(image)],
            "extension": "png"
        },
        "graphviz": {
            "pattern": r'```dot(.*?)```',
            "command": lambda temp, image: ["dot", "-Tpng", "-o", str(image), str(temp)],
            "extension": "png"
        },
        "nwdiag": {
            "pattern": r'```nwdiag(.*?)```',
            "generate_with_kroki": True,
            "extension": "png"
        },
    }

    for diag_type, settings in diagram_patterns.items():
        for match in re.finditer(settings["pattern"], output_content, re.DOTALL):
            code = match.group(1).strip()
            image_file = diagram_subdir / f"{base_filename}_{diagram_index}.{settings['extension']}"

            # Ensure the parent directory exists
            diagram_subdir.mkdir(parents=True, exist_ok=True)

            if diag_type == "nwdiag" and settings.get("generate_with_kroki", False):
                generate_nwdiag_with_kroki(code, image_file)
            else:
                temp_file = output_dir / f"{base_filename}_{diagram_index}.tmp"
                with open(temp_file, "w") as f:
                    f.write(code)

                try:
                    subprocess.run(
                        settings["command"](temp_file, image_file),
                        check=True,
                        timeout=60
                    )
                    logging.info(f"Generated {diag_type} diagram: {image_file}")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Error generating {diag_type} diagram: {e}")
                    raise
                finally:
                    os.remove(temp_file)

            output_content = output_content.replace(match.group(0), f"![{diag_type} diagram]({image_file.name})")
            diagram_index += 1

            metadata.append({
                "file": str(input_file),
                "type": diag_type,
                "image": str(image_file),
                "code_snippet": code[:50]
            })

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_content)

    logging.info(f"Saved processed markdown file: {output_file}")

# Process directories
def process_directory(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metadata = []

    for file_path in input_dir.rglob("*.md"):
        output_file_path = output_dir / file_path.relative_to(input_dir)
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        process_markdown_file(file_path, output_file_path, output_dir, metadata)

    metadata_file = output_dir / "diagram_metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
    logging.info(f"Saved metadata file: {metadata_file}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Process Markdown files to generate diagrams.")
    parser.add_argument("-i", "--input_dir", required=True, help="Input directory containing Markdown files.")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory for processed Markdown files and images.")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
    parser.add_argument("--log_file", help="Optional log file to save logs.")

    args = parser.parse_args()
    setup_logging(args.debug, args.log_file)

    logging.info("Starting script...")

    tools = ["mmdc", "plantuml", "vg2png", "bytefield-svg", "wavedrom-cli", "dot"]
    check_tools(tools)

    try:
        validate_output_dir(args.output_dir)
    except ValueError as e:
        logging.error(e)
        return

    try:
        process_directory(args.input_dir, args.output_dir)
    except Exception as e:
        logging.error(f"Error: {e}")
    else:
        logging.info("Processing complete!")

if __name__ == "__main__":
    main()

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
from pathlib import Path
import argparse

# Set up logging
def setup_logging(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

# Check tool availability
def check_tools(tools):
    missing_tools = []
    for tool in tools:
        if not shutil.which(tool):
            missing_tools.append(tool)
    if missing_tools:
        logging.error(f"Missing required tools: {', '.join(missing_tools)}")
        raise RuntimeError(f"Install the missing tools: {', '.join(missing_tools)}")

# Diagram generation functions
def generate_diagram(command, code, input_file, output_dir, base_filename, diagram_index, extension):
    """Generate an image from a diagram code block"""
    image_file = output_dir / f"{base_filename}_{diagram_index}.{extension}"
    temp_file = output_dir / f"{base_filename}_{diagram_index}.tmp"

    with open(temp_file, "w") as f:
        f.write(code)

    try:
        subprocess.run(command + [str(temp_file), str(image_file)], check=True)
        logging.info(f"Generated image: {image_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating image: {e}")
        raise
    finally:
        os.remove(temp_file)

    return image_file

def copy_image_file(src_image_path, output_dir):
    """Copy an image from the source to the output directory."""
    try:
        image_rel_path = Path(src_image_path)
        dest_image_path = output_dir / image_rel_path.name

        # Copy the image to the output directory
        shutil.copy(src_image_path, dest_image_path)
        logging.info(f"Copied image {src_image_path} to {dest_image_path}")
        
        return dest_image_path
    except Exception as e:
        logging.error(f"Error copying image {src_image_path}: {e}")
        raise

# Process Markdown files
def process_markdown_file(input_file, output_file, output_dir, metadata):
    logging.info(f"Processing markdown file: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    output_content = content
    base_filename = input_file.stem
    diagram_index = 0

    diagram_patterns = {
        "mermaid": {
            "pattern": r'```mermaid(.*?)```',
            "command": ["mmdc", "-i"],
            "extension": "png"
        },
        "plantuml": {
            "pattern": r'```plantuml(.*?)```',
            "command": ["plantuml", "-tpng"],
            "extension": "png"
        },
        "vega": {
            "pattern": r'```vega(.*?)```',
            "command": ["vg2png"],
            "extension": "png"
        },
        "bytefield": {
            "pattern": r'```bytefield(.*?)```',
            "command": ["bytefield-svg"],
            "extension": "svg"
        },
        "wavedrom": {
            "pattern": r'```wavedrom(.*?)```',
            "command": ["wavedrom-cli", "-i"],
            "extension": "png"
        },
        "nwdiag": {
            "pattern": r'```nwdiag(.*?)```',
            "command": ["nwdiag"],
            "extension": "png"
        },
        "packetdiag": {
            "pattern": r'```packetdiag(.*?)```',
            "command": ["packetdiag"],
            "extension": "png"
        },
        "graphviz": {
            "pattern": r'```dot(.*?)```',
            "command": ["dot", "-Tpng"],
            "extension": "png"
        },
    }

    for diag_type, settings in diagram_patterns.items():
        for match in re.finditer(settings["pattern"], output_content, re.DOTALL):
            code = match.group(1).strip()
            image_file = generate_diagram(settings["command"], code, input_file, output_dir, base_filename, diagram_index, settings["extension"])
            output_content = output_content.replace(match.group(0), f"![{diag_type} diagram]({image_file.name})")
            diagram_index += 1

            # Update metadata
            metadata.append({
                "file": str(input_file),
                "type": diag_type,
                "image": str(image_file),
                "code_snippet": code[:50]  # Save first 50 chars of code for reference
            })

    # Find image references in markdown and copy them
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'  # Matches image syntax ![alt](path)
    for match in re.finditer(image_pattern, output_content):
        image_path = match.group(2)
        logging.debug(f"Found image reference: {image_path}")
        
        # Handle relative paths (starting with ./ or ../)
        if image_path.startswith(('./', '../')) or os.path.isabs(image_path):
            abs_image_path = Path(input_file.parent) / image_path
            if abs_image_path.exists():  # Only copy if the image exists
                dest_image_path = copy_image_file(abs_image_path, output_dir)
                output_content = output_content.replace(image_path, Path(dest_image_path).name)
            else:
                logging.warning(f"Image {image_path} not found in input directory.")

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

    # Save metadata
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

    args = parser.parse_args()
    setup_logging(args.debug)

    logging.info("Starting script...")

    # Verify required tools are installed
    tools = ["mmdc", "plantuml", "vg2png", "bytefield-svg", "wavedrom-cli", "nwdiag", "packetdiag", "dot"]
    check_tools(tools)

    try:
        process_directory(args.input_dir, args.output_dir)
    except Exception as e:
        logging.error(f"Error: {e}")
    else:
        logging.info("Processing complete!")

if __name__ == "__main__":
    main()

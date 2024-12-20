#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

VENV_DIR="docs-venv"

# Function to format debug messages with colour and timestamp
debug() {
    local BLUE="\033[0;34m"
    local GREEN="\033[0;32m"
    local YELLOW="\033[0;33m"
    local RED="\033[0;31m"
    local NC="\033[0m" # No Colour
    local TIMESTAMP="$(date +'%Y-%m-%d %H:%M:%S')"

    case "$2" in
        "INFO")
            echo -e "${BLUE}[$TIMESTAMP] ${GREEN}[INFO] $1${NC}"
            ;;
        "WARNING")
            echo -e "${BLUE}[$TIMESTAMP] ${YELLOW}[WARNING] $1${NC}"
            ;;
        "ERROR")
            echo -e "${BLUE}[$TIMESTAMP] ${RED}[ERROR] $1${NC}"
            ;;
        *)
            echo -e "${BLUE}[$TIMESTAMP] $1${NC}"
            ;;
    esac
}

pip install yaml

# Function to activate the virtual environment
debug "Creating script to activate virtual environment..." "INFO"
cat <<EOL > activate_venv.sh
#!/bin/bash
if [[ -n "\$VIRTUAL_ENV" ]]; then
    echo "Deactivating existing virtual environment..."
    deactivate
fi
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate
echo "Virtual environment activated."
EOL
chmod +x activate_venv.sh

# Function to deactivate the virtual environment
debug "Creating script to deactivate virtual environment..." "INFO"
cat <<EOL > deactivate_venv.sh
#!/bin/bash
if [[ -n "\$VIRTUAL_ENV" ]]; then
    echo "Deactivating virtual environment..."
    deactivate
    echo "Virtual environment deactivated."
else
    echo "No virtual environment is currently active."
fi
EOL
chmod +x deactivate_venv.sh

debug "Updating system packages..." "INFO"
sudo apt update && sudo apt -y upgrade || debug "Failed to update and upgrade system packages." "ERROR"

debug "Installing dependencies..." "INFO"
# Ensure required packages are installed
sudo apt install -y nodejs npm python3 python3-pip python3-venv default-jdk graphviz || debug "Failed to install dependencies." "ERROR"

# Set up virtual environment
debug "Setting up Python virtual environment..." "INFO"
if [[ -d "$VENV_DIR" ]]; then
    debug "Virtual environment already exists. Skipping creation." "INFO"
else
    if [[ ! -w $(pwd) ]]; then
        debug "Current directory is not writable. Please run the script in a writable directory." "ERROR"
        exit 1
    fi
    python3 -m venv $VENV_DIR || debug "Failed to create virtual environment." "ERROR"
fi
source $VENV_DIR/bin/activate

# Ensure pip is up-to-date in the virtual environment
debug "Upgrading pip in the virtual environment..." "INFO"
pip install --upgrade pip || debug "Failed to upgrade pip." "ERROR"

debug "Installing Vega CLI..." "INFO"
if ! command -v vg2pdf &> /dev/null; then
    npm install -g vega-cli || debug "Failed to install Vega CLI." "ERROR"
else
    debug "Vega CLI is already installed." "INFO"
fi

debug "Installing Wavedrom CLI..." "INFO"
if ! command -v wavedrom &> /dev/null; then
    debug "Cleaning up partial installations of Wavedrom CLI..." "WARNING"
    rm -rf $(npm root -g)/wavedrom-cli
    npm install -g wavedrom-cli || debug "Failed to install Wavedrom CLI." "ERROR"
else
    debug "Wavedrom CLI is already installed." "INFO"
fi

debug "Installing Mermaid CLI..." "INFO"
if ! command -v mmdc &> /dev/null; then
    npm install -g @mermaid-js/mermaid-cli || debug "Failed to install Mermaid CLI." "ERROR"
else
    debug "Mermaid CLI is already installed." "INFO"
fi

debug "Installing Bytefield..." "INFO"
if ! command -v bytefield-svg &> /dev/null; then
    npm install -g bytefield-svg || debug "Failed to install Bytefield." "ERROR"
else
    debug "Bytefield is already installed." "INFO"
fi

debug "Installing Blockdiag tools (including nwdiag, packetdiag)..." "INFO"
pip install blockdiag nwdiag seqdiag || debug "Failed to install Blockdiag tools." "ERROR"

debug "Installing PlantUML..." "INFO"
# PlantUML uses Java, ensure JDK is installed
if ! command -v plantuml &> /dev/null; then
    sudo apt install -y plantuml || debug "Failed to install PlantUML." "ERROR"
else
    debug "PlantUML is already installed." "INFO"
fi

debug "Installing MkDocs and plugins..." "INFO"
# Install MkDocs and plugins/extensions
if ! pip show mkdocs &> /dev/null; then
    debug "Installing MkDocs and common plugins..." "INFO"
    pip install mkdocs  mkdocs-mermaid2  mkdocs-literate-nav mkdocs-include mkdocs-material mkdocs-macros-plugin mkdocs-pdf-export-plugin mkdocs-include-markdown-plugin plantuml-markdown mkdocs-video || debug "Failed to install MkDocs or plugins." "ERROR"
else
    debug "MkDocs and plugins are already installed." "INFO"
fi

echo
debug "Verifying installations..." "INFO"
debug "Node.js version: $(node -v)" "INFO"
debug "NPM version: $(npm -v)" "INFO"
debug "Pip version: $(pip --version)" "INFO"
java_version_output=$(java -version 2>&1 | tr '
' ' ')
java_formatted_output=$(java -version 2>&1)
debug "Java version (formatted):" "INFO"
echo "$java_formatted_output" | while IFS= read -r line; do
    debug "$line" "INFO"
done
debug "PlantUML version: $(plantuml -version)" "INFO"
debug "MkDocs version: $(mkdocs --version)" "INFO"
debug "Vega CLI version: $(vg2png --version)" "INFO"
debug "Wavedrom CLI version: $(wavedrom-cli --version)" "INFO"
debug "Mermaid CLI version: $(mmdc --version)" "INFO"
bytefield_version=$(npm list -g bytefield-svg --depth=0 2>/dev/null | grep "bytefield-svg@" | awk -F@ '{print $2}')
if [[ -n "$bytefield_version" ]]; then
    debug "Bytefield version: $bytefield_version" "INFO"
else
    debug "Bytefield is not installed or version could not be determined." "ERROR"
fi
debug "Blockdiag version: $(blockdiag --version)" "INFO"
debug "Nwdiag version: $(nwdiag --version)" "INFO"
debug "Seqdiag version: $(seqdiag --version)" "INFO"

debug "All tools installed successfully in the virtual environment!" "INFO"
debug "Use 'source ./activate_venv.sh' to activate the virtual environment." "INFO"
debug "Use './deactivate_venv.sh' to deactivate the virtual environment." "INFO"

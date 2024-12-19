#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing dependencies..."
# Ensure required packages are installed
sudo apt install -y nodejs npm python3 python3-pip default-jdk graphviz

echo "Installing Vega CLI..."
npm install -g vega-cli

echo "Installing Wavedrom CLI..."
npm install -g wavedrom-cli

echo "Installing Mermaid CLI..."
npm install -g @mermaid-js/mermaid-cli

echo "Installing Bytefield..."
pip install bytefield-svg

echo "Installing Blockdiag tools (including nwdiag, packetdiag)..."
pip install blockdiag nwdiag seqdiag actdiag rackdiag packetdiag

echo "Installing PlantUML..."
# PlantUML uses Java, ensure JDK is installed
sudo apt install -y plantuml

echo "Verifying installations..."
echo "Node.js version: $(node -v)"
echo "NPM version: $(npm -v)"
echo "Pip version: $(pip --version)"
echo "Java version: $(java -version)"

echo "All tools installed successfully!"

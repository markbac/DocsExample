
# README for Structurizr Lite Setup and Usage

---

## **Overview**

This repository contains the **Structurizr DSL** model for the **E470 Series 6 ESME (Electricity Smart Metering Equipment)**. The system architecture is modelled to represent the core software, hardware, and integration layers, enabling easy collaboration, documentation, and maintenance. Structurizr Lite is used to render these models as diagrams and provide a visual understanding of the system.

Key features of this repository include:
- A DSL (`workspace.dsl`) for the E470 Series 6 ESME system architecture.
- Scripts to process and enhance documentation (`convert.py`).
- Support for embedding diagrams (Mermaid, PlantUML) within markdown.
- Layout customisations stored to preserve consistent visualisation.

---

## **File and Directory Structure**

- **`workspace.dsl`**: The primary Structurizr DSL file, describing the architecture model, relationships, and views.
- **`workspace.json`**: A JSON file containing the exported Structurizr workspace, including all model and view customisations.
- **`.structurizr/`**: Directory containing Structurizr Lite's internal data, including indices, cached assets, and custom layout configurations.
- **`convert.py`**: Script to process markdown files containing Mermaid and PlantUML diagrams and generate corresponding images.
- **`docs-src/`**: Source markdown files with embedded diagrams for documentation.
- **`docs/`**: Processed markdown files and generated images ready for inclusion in Structurizr or other tools.
- **`adrs/`**: Architecture Decision Records (ADRs) that document design decisions.
- **`tmp/`**: Temporary files and intermediate processing outputs.

---

## **Prerequisites**

### **System Requirements**
- **Operating Systems**: 
  - Windows 10/11
  - Linux (Ubuntu 20.04+ or via Windows Subsystem for Linux (WSL))
- **Required Tools**:
  - Docker (for running Structurizr Lite)
  - Python 3.8+ (for `convert.py`)

### **Software Installation**

#### **Structurizr Lite**
1. Install Docker:
   - **Windows**: Download and install Docker Desktop from [Docker's official site](https://www.docker.com/products/docker-desktop).
   - **Linux (Ubuntu)**:
     ```bash
     sudo apt update
     sudo apt install -y docker.io
     sudo systemctl enable --now docker
     ```

2. Pull the Structurizr Lite Docker image:
   ```bash
   docker pull structurizr/lite
   ```

#### **Python and Dependencies**
1. Install Python:
   - **Windows**: Download from [python.org](https://www.python.org) and install.
   - **Linux (Ubuntu)**:
     ```bash
     sudo apt update
     sudo apt install -y python3 python3-pip
     ```

2. Install required Python packages:
   ```bash
   pip install markdown
   ```

#### **Mermaid and PlantUML**

Refer to the [Appendix: Installing Mermaid and PlantUML](#appendix-installing-mermaid-and-plantuml) for detailed installation instructions for Mermaid CLI and PlantUML.

---

## **How to View and Modify the Structurizr Model**

### **Viewing the Model**
1. Run Structurizr Lite:
   Navigate to the project directory and run:
   ```bash
   docker run -p <host_port>:8080 -v "$(pwd):/usr/local/structurizr" structurizr/lite
   ```
   - Replace `<host_port>` with the port number you wish to use on your machine (e.g., `8081`).
   - Replace `$(pwd)` with the full path to your project directory if needed.

2. Access Structurizr Lite:
   - Open your browser and navigate to `http://localhost:<host_port>` (e.g., `http://localhost:8081`).
   - Load the `workspace.dsl` file from the Structurizr Lite interface.

### **Modifying the Model**
1. **Using Structurizr Lite**:
   - Open the model in Structurizr Lite.
   - Drag and position elements within views to customise layouts.
   - Add or edit components, containers, or relationships as needed.

2. **Editing the DSL**:
   - Make changes directly in the `workspace.dsl` file using any text editor.
   - Reload the updated file in Structurizr Lite to reflect changes.

3. **Saving Custom Layouts**:
   - Layout customisations made in Structurizr Lite are saved in the `.structurizr` directory. These are automatically preserved when running Structurizr Lite locally.

4. **Advanced Customisation**:
   - Export the workspace to `workspace.json` to preserve all modifications, including model and view customisations.
   - Commit both `workspace.dsl` and `workspace.json` to version control for full traceability.

---

## **File Revision Control**

### **Include in Revision Control**:
1. **Core Files**:
   - `workspace.dsl`: The primary architecture model.
   - `workspace.json`: Preserves model and view customisations.
   - `convert.py`: Diagram processing script.
   - `.structurizr/`: Required for layout preservation.

2. **Source Documentation**:
   - `docs-src/`: Raw markdown files containing embedded diagrams.
   - `adrs/`: Architecture Decision Records.

### **Exclude**:
- `docs/`: Generated documentation and images (can be recreated).
- `tmp/`: Temporary and intermediate files.

---

## **Improvements and Work to Be Done**

### **Potential Improvements**:
1. **Diagram Consistency**:
   - Apply uniform styles using Structurizr's themes.
   - Automate layout alignment for complex views.

2. **Automation**:
   - Integrate `convert.py` into a CI/CD pipeline to automate diagram generation.
   - Create a validation script for `workspace.dsl`.

3. **Enhanced Documentation**:
   - Expand ADRs to include all major design decisions.
   - Add a glossary for technical terms specific to the E470 Series 6 ESME.

4. **Broader Model Views**:
   - Include deployment and runtime views for a holistic system perspective.

### **Work Still Needed**:
1. **Review and Expand Views**:
   - Ensure all container and component relationships are accurately reflected.
   - Add missing subsystems or third-party integrations.

2. **Error Handling in `convert.py`**:
   - Handle edge cases for malformed diagrams more robustly.

3. **Version Traceability**:
   - Establish links between elements in `workspace.dsl` and corresponding source code modules.

4. **Documentation**:
   - Improve instructions for onboarding new contributors.

---

## **Troubleshooting**

### **Common Issues**
1. **Docker Errors**:
   - Port already in use: Stop other services on port 8080 or change the Docker run command to use another port.

2. **`convert.py` Failures**:
   - Missing Python dependencies: Reinstall with `pip install -r requirements.txt`.

3. **Layout Issues**:
   - Missing `.structurizr` directory or corrupted layout configurations: Restore from backup or reset.

---

## **FAQ**

**Q: What’s the difference between `workspace.dsl` and `workspace.json`?**  
`workspace.dsl` is the source code for the model, while `workspace.json` is an exported version containing custom layouts and other metadata.

**Q: Can I recreate diagrams if I delete `.structurizr`?**  
Yes, but any custom layouts will be lost unless stored in `workspace.json`.

**Q: How do I add new diagrams?**  
Modify the relevant markdown files in `docs-src/` and use `convert.py` to process them.

---

## **Appendix: Installing Mermaid and PlantUML**

### **Mermaid Installation**

#### **For Windows**:
1. Install Node.js (includes npm):
   - Download the Node.js installer from [Node.js official site](https://nodejs.org).
   - Run the installer and follow the prompts to complete the installation.
   - Verify installation by running:
     ```cmd
     node --version
     npm --version
     ```

2. Install mermaid-cli:
   - Open a Command Prompt or PowerShell and run:
     ```cmd
     npm install -g @mermaid-js/mermaid-cli
     ```
   - Verify installation by running:
     ```cmd
     mmdc --version
     ```

#### **For Linux (Ubuntu)**:
1. Install Node.js and npm:
   - Run the following commands:
     ```bash
     sudo apt update
     sudo apt install -y nodejs npm
     ```

2. Install mermaid-cli:
   - Run:
     ```bash
     npm install -g @mermaid-js/mermaid-cli
     ```
   - Verify installation by running:
     ```bash
     mmdc --version
     ```

---

### **PlantUML Installation**

#### **For Windows**:
1. Install Java (required to run PlantUML):
   - Download and install OpenJDK from [AdoptOpenJDK](https://adoptium.net/) or Oracle.

2. Download PlantUML:
   - Visit the [PlantUML download page](http://plantuml.com/download) and download the `plantuml.jar` file.

3. Create a batch file or use Command Prompt:
   - Save the `plantuml.jar` file to a directory (e.g., `C:\Tools`).
   - To run PlantUML, use the following command:
     ```cmd
     java -jar C:\Tools\plantuml.jar diagram.puml
     ```

#### **For Linux (Ubuntu)**:
1. Install Java (required to run PlantUML):
   - Run:
     ```bash
     sudo apt update
     sudo apt install -y default-jdk
     ```

2. Download PlantUML:
   - Run:
     ```bash
     wget https://sourceforge.net/projects/plantuml/files/plantuml.jar/download -O plantuml.jar
     ```
     Save it to a directory (e.g., `$HOME/tools/plantuml.jar`).

3. Create an alias for easier use:
   - Add this to your `.bashrc` or `.zshrc`:
     ```bash
     alias plantuml="java -jar ~/tools/plantuml.jar"
     ```
   - Apply the changes:
     ```bash
     source ~/.bashrc
     ```

4. Run PlantUML:
   - Use the alias to generate diagrams:
     ```bash
     plantuml diagram.puml
     ```

---

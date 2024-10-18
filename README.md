
# Structurizr MkDocs Framework

This repository provides a framework for generating documentation using Structurizr DSL diagrams, MkDocs, and GitHub Actions for CI/CD. The framework supports publishing to GitHub Pages, generating a PDF version of the documentation, and integrating arc42 architectural documentation.

## Repository Structure

```
structurizr_mkdocs_framework/
├── .github/
│   └── workflows/
│       └── build.yml        # GitHub Actions workflow for building and deploying documentation
├── arc42/                   # Directory containing arc42 formatted documentation sections
│   ├── 01_introduction.md   # Introduction for arc42 documentation
│   ├── 02_requirements.md   # Requirements for arc42 documentation
│   └── ...                  # Additional arc42 documentation files
├── docs/
│   ├── diagrams/            # Directory where Structurizr generated diagrams will be saved
│   └── index.md             # Main page of the documentation
├── mkdocs.yml               # Configuration for MkDocs
├── workspace.dsl            # Example Structurizr DSL workspace file
└── .gitignore               # Git ignore file to ignore certain files and directories
```

## Workflow

### GitHub Actions Workflow (`.github/workflows/build.yml`)

The GitHub Actions workflow automates the following tasks when changes are pushed to the `main` branch:

1. **Setup Environment**: Checks out the repository and sets up Python with version 3.9.

2. **Install Dependencies**: Installs the necessary dependencies for MkDocs, including the plugins for PDF export, Mermaid, and PlantUML.

3. **Generate Structurizr Diagrams**: Uses Docker to generate diagrams from the Structurizr DSL. The Docker image `ghcr.io/aidmax/structurizr-cli-docker` is used to run Structurizr CLI commands to export diagrams in the Mermaid format.

   - **Command**: 
     ```bash
     docker pull ghcr.io/aidmax/structurizr-cli-docker
     docker run --rm -v $DOCS_PATH:/root/data -w /root/data ghcr.io/aidmax/structurizr-cli-docker \
         export --workspace workspace.dsl --format mermaid --output docs/diagrams/
     ```
   
4. **Build Documentation**: Runs `mkdocs build` to generate static HTML documentation from markdown files.

5. **Generate PDF Documentation**: Runs `mkdocs pdf-export` to generate a PDF version of the documentation, including a table of contents and an index for better navigation.

6. **Deploy to GitHub Pages**: Deploys the generated HTML documentation to GitHub Pages using `peaceiris/actions-gh-pages@v3`.

7. **Upload PDF as Release Artifact**: Uploads the generated PDF file as a GitHub artifact, making it available for download.

8. **Create Release with PDF**: Creates a new GitHub release that includes the PDF file as an asset.

### MkDocs Configuration (`mkdocs.yml`)

- **Site Name**: Configures the name of the site as "Structurizr Documentation".
- **Theme**: Uses the "material" theme for MkDocs.
- **Plugins**: Includes plugins for Mermaid, PlantUML, and PDF export.
- **arc42 Navigation**: Provides navigation for arc42 architectural documentation.

### Structurizr Diagram Generation (`workspace.dsl`)

The `workspace.dsl` file contains an example of how to define a workspace in Structurizr DSL. The diagrams generated from this file are stored in the `docs/diagrams/` directory and are embedded within the MkDocs documentation.

## How to Use This Repository

1. **Clone the Repository**: Clone the repository to your local machine.
   ```sh
   git clone <repo-url>
   ```

2. **Modify Documentation**: Update the markdown files in the `docs/` or `arc42/` directories as needed. You can also add Structurizr DSL files to the `structurizr/` directory.

3. **Push Changes**: Commit and push changes to the `main` branch to trigger the GitHub Actions workflow.

4. **View Documentation**:
   - The HTML documentation will be available on GitHub Pages.
   - The PDF version will be available as a release artifact.

## Dependencies

- **MkDocs**: A static site generator for creating project documentation.
- **Structurizr CLI Docker**: Used to generate diagrams from Structurizr DSL.
- **GitHub Actions**: For automating the build and deployment of documentation.

## Key Features

- **arc42 Documentation Format**: Supports the popular arc42 architecture documentation format.
- **Automated CI/CD**: The workflow is fully automated with GitHub Actions, making it easy to generate and deploy documentation.
- **PDF Export**: The documentation is also exported as a PDF, including a table of contents and an index for easy reference.

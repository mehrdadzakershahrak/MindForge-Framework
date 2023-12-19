# Installation Guide for MindForge

This guide outlines the steps required to install and set up MindForge on your system.

## Prerequisites
- Python 3.11 or later
- Git

## Cloning the Repository
Clone the MindForge repository using Git:
```bash
git clone https://github.com/mehrdadzakershahrak/MindForge.git
cd MindForge
```

## Setting Up a Virtual Environment (Recommended)
Create and activate a virtual environment:
```python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Installing Dependencies
Install the required Python packages:

```pip install -r requirements.txt```

## Environment Variables
Set up necessary environment variables, such as API keys:

- Rename .env.example to .env.
- Edit src/.env to include your specific keys and settings if you are planning on using openAI API.

## Running MindForge
After installation, run MindForge using:
```python src/main.py```

This `INSTALL.md` provides a basic structure for setting up MindForge. Modify as necessary to match the specific requirements and structure of your project.

For guidelines on how to use MindForge and examples of its capabilities, please refer to the [USAGE.md](docs/USAGE.md)  documentation.

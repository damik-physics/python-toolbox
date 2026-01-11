#!/usr/bin/env python3
from pathlib import Path
import re
import typer

MAIN_TEMPLATE = """
def main():
    print("Hello from {project_name}!")

if __name__ == "__main__":
    main()
"""

PYPROJECT_TEMPLATE = """
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Default description for {project_name}"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]

[tool.setuptools.packages.find]
where = ["src"]
"""

DOCKERFILE_TEMPLATE = """
FROM python:3.10-slim as base

# Setup env
ENV PYTHONFAULTHANDLER=1 \\
    PYTHONHASHSEED=random \\
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy source
COPY src/ ./src/

# Run as non-root user
RUN useradd -m appuser
USER appuser

CMD ["python", "-m", "{project_name}"]
"""

DOCKERIGNORE_TEMPLATE = """
__pycache__/
*.py[cod]
*$py.class
.venv/
.git/
.dockerignore
Dockerfile
dist/
build/
"""

app = typer.Typer()

def create_file(path: Path, content: str):
    path.write_text(content.strip() + "\n")

@app.command()
def init(project_name: str = typer.Argument(..., help="Name of the new project")):
    """
    Creates a standardized, modular Python project structure.
    """

    # Validate project name
    if not re.match(r"^[a-zA-Z0-9_-]+$", project_name):
        typer.secho("Error: Project name contains invalid characters.", fg="red", bold=True)
        raise typer.Exit(code=1)
    
    base_path = Path.cwd() / project_name

    # Check existence of directory
    if base_path.exists():
        typer.secho(f"Error: Directory {project_name} already exists.", fg="red")
        raise typer.Exit(code=1)
        
    # Create directory structure
    package_name = project_name.replace("-", "_")
    dirs = [
        base_path / "src" / package_name,
        base_path / "tests",
        base_path / "docs",
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        (d / "__init__.py").touch()

    # Create package entry point
    create_file(dirs[0] / "__main__.py", MAIN_TEMPLATE.format(project_name=package_name)) # dirs[0] points to src/package_name

    # Generate remaining configuration files 
    create_file(base_path / "README.md", f"# {project_name}\n\n{project_name} description.")
    create_file(base_path / ".gitignore", "__pycache__/\n*.pyc\n.venv/\ndist/")
    create_file(base_path / "pyproject.toml", PYPROJECT_TEMPLATE.format(project_name=project_name))
    create_file(base_path / "Dockerfile", DOCKERFILE_TEMPLATE.format(project_name=package_name))
    create_file(base_path / ".dockerignore", DOCKERIGNORE_TEMPLATE)

    typer.echo("") 
    typer.secho("─" * 50, fg=typer.colors.BLUE)
    typer.secho(f"Project '{project_name}' initialized successfully!", fg=typer.colors.GREEN, bold=True)
    typer.secho(f"Path: {base_path}", fg=typer.colors.BRIGHT_WHITE)
    typer.secho("─" * 50, fg=typer.colors.BLUE)
    typer.echo("")

# Python Project Scaffolder

A lightweight CLI utility designed to bootstrap production-ready Python projects in seconds. This tool is part of the `python-toolbox` and focuses on modularity, security, and standardization.

## Features

- **PEP 621 Compliance**: Generates a modern `pyproject.toml` using `setuptools` as the build backend.
- **Docker-Ready**: Includes a hardened `Dockerfile` using a slim base image and non-root user configuration for security.
- **Modular Structure**: Enforces the `src/` layout pattern to ensure clean imports and testability.
- **Automation**: Pre-configures `.gitignore` and `.dockerignore` for common Python workflows.
- **Linting & Type Checking**: Built-in optional dependencies for `pytest`, `ruff`, and `mypy`.

## Usage

Initialize a new project by running:

```bash
pt-init my-new-project
```

## Generated Structure

```text
my-new-project/
├── src/
│   └── my_new_project/
│       └── __init__.py
├── tests/
├── docs/
├── .gitignore
├── .dockerignore
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Platform Engineering Highlights

This scaffolder implements several "Security by Design" and "Clean Code" principles:

- **Non-Root User**: The generated Dockerfile creates an appuser to avoid running containers with elevated privileges.

- **Dependency Layering**: The Dockerfile uses optimized COPY instructions to leverage Docker's build cache for faster CI/CD pipelines.

- **Standardized Environments**: Uses PYTHONUNBUFFERED and PYTHONFAULTHANDLER to ensure reliable logging and debugging in containerized environments.

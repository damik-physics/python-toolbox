# Python Toolbox

A collection of modular Python CLI utilities for automation, developer productivity, and system optimization. This project is structured as a unified package leveraging modern Python standards.

## Installation

The toolbox is designed to be installed as a unified package. To install the utilities and their dependencies, run:

```bash
git clone https://github.com/damik-physics/python-toolbox.git
cd python-toolbox
pip install .
```

## Available Tools

### 1. Project Scaffolder (`pt-init`)

A CLI utility to bootstrap new Python projects with production-ready defaults.

- Standards: Generates PEP 621 compliant `pyproject.toml`.

- Containerization: Includes hardened `Dockerfile` templates with non-root user security.

- Structure: Enforces the professional `src` directory layout.

### 2. Todo CLI (`todo`)

A persistent task manager for terminal-centric workflows.

- Storage: Lightweight JSON-based persistence.

- Safety: Implements defensive programming for file handling and user input.

### 3. Flashcard CLI (`flash`)

A lightweight spaced-repetition training tool.

- Modularity: Separation of core logic from I/O layers for better testability.

### General remarks 

- Packaging: Managed via `pyproject.toml` using `setuptools` as the build backend.

- Layout: Adopts the `src` layout to ensure import isolation and reliable testing.

- Automation: All tools are designed to be callable globally once installed.

- Static Analysis: Pre-configured for `ruff` and `mypy`.


## Directory Structure

```plaintext
python-toolbox/
├── src/
│   └── toolbox/            # Main package
│       ├── scaffolder/     # Project Scaffolder
│       ├── todo_cli/       # Todo Utility
│       └── flashcards_cli/ # Spaced-repetition Tool
├── pyproject.toml          # Build and dependency configuration
└── README.md
```

## License

This project is licensed under the MIT License.

## Author

David Mikhail, PhD Computational researcher and software engineer specializing in high-performance computing, automation, and backend systems.
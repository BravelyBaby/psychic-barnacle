 # Psychic Barnacle

 [![Proprietary](https://img.shields.io/badge/license-Proprietary-red)](CLA.md) [![CLA required](https://img.shields.io/badge/cla-required-yellow)](CLA.md)

 > ⚠️ Proprietary — contact lifeoflandry@gmail.com to request a license or reuse permission. Contributions require a signed Contributor License Agreement (see `CLA.md`).

Small, adaptable project template meant to be developed inside a devcontainer. The current codebase implements a lightweight Python task-management core that can back CLIs, web APIs, or automations. Extend it with additional runtimes (Node, Python, etc.) as you grow the project.

 Quick links
 - CLA and contributor instructions: `CLA.md` / `CONTRIBUTING.md`
 - Maintainer helper: `scripts/verify-cla.sh`
 - Devcontainer: `.devcontainer/devcontainer.json`
 - CI workflows: `.github/workflows/`

## Features

- `Task` dataclass with validation, ordering, and serialization helpers.
- `TaskManager` collection with creation, completion, overdue filtering, and aggregate summaries.
- `pytest` test suite demonstrating common behaviors.

## Getting started (local)
1. Clone the repo:
    ```bash
    git clone https://github.com/BravelyBaby/psychic-barnacle.git
    cd psychic-barnacle
    ```
2. Create a virtual environment (recommended) and install the optional development dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .[dev]
    ```
3. Run the test suite:
    ```bash
    make test
    ```
4. Explore the task primitives in a Python shell:
    ```python
    >>> from psychic_barnacle import TaskManager
    >>> manager = TaskManager()
    >>> manager.create_task("Draft release notes", priority=2)
    >>> manager.summary()
    {'total': 1, 'completed': 0, 'pending': 1, 'overdue': 0, 'by_priority': {2: 1}}
    ```

 Devcontainer and environment
 - A minimal devcontainer is included at `.devcontainer/devcontainer.json`. It provides an Ubuntu base image and common CLI tools. Customize it if you add language toolchains (Node, Python, etc.).
 - To open a URL in the host's default browser from inside the container use:
     ```bash
     $BROWSER <url>
     ```

## Project layout
- `src/psychic_barnacle/` — Python package with task primitives
- `tests/` — pytest suite (see `tests/README.md`)
- `docs/` — documentation and design notes (create as needed)
- `.github/` — PR templates, workflows, and actions

 Common commands
 - Update system packages:
     ```bash
     sudo apt update && sudo apt upgrade
     ```
 - Build/run with Docker (only if a `Dockerfile` is present):
     ```bash
     docker build -t psychic-barnacle .
     docker run --rm -it psychic-barnacle
     ```

 Contributing & CLA (important)
 - This repository is proprietary. Do not submit code unless you have explicit permission from the owner.
 - All contributions require a signed Contributor License Agreement (`CLA.md`).
 - To contribute: fill `CLA-<your-name>.md` with the signed CLA, include `<!-- CLA-SIGNED: true -->` at the top, attach the file to your PR, and check the CLA box in the PR template.
 - Automated checks will verify the CLA file and apply a `cla/present` label. A maintainer will perform manual verification and add the `cla/verified` label before merge. Maintainers can use `scripts/verify-cla.sh <pr-number>` to add the `cla/verified` label after verification.

 Maintainer notes
 - Recommended branch protection (Settings → Branches): require the status checks `CLA check` and `CLA Verified Gate` before merging to `main`.
 - If you install a CLA App (e.g., CLA Assistant), follow `CLA-INTEGRATION.md` and consider disabling the repository's Actions-based checks.
 - Detailed maintainer instructions (verification flow, scripts, and branch protection steps) are in `CONTRIBUTING.md`.

 Security and secrets
 - No secrets should be committed. Use environment variables for configuration and document any required secrets in `docs/` (but never check them in).

 License & legal
 - This repository is proprietary. Contact lifeoflandry@gmail.com for licensing or reuse permissions.

 Need help?
 - Open an issue or email lifeoflandry@gmail.com. For maintainers, see `CLA-INTEGRATION.md` and `CONTRIBUTING.md` for workflows and helper scripts.

 Notes
 - This is a minimal template — when you add a language runtime, include the standard manifest (e.g., `package.json`, `pyproject.toml`) and update README with exact build/test commands.


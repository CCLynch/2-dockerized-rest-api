# my-first-ci-project

A simple Python project demonstrating Continuous Integration (CI) using GitHub Actions.

## Project Structure

- `my_module/`: Contains the core Python functions (e.g., `add`, `subtract`, `power`).
- `tests/`: Contains `pytest` unit tests for the functions in `my_module/`.
- `requirements.txt`: Lists the Python dependencies required for this project (`pytest`).
- `.github/workflows/ci.yml`: Configures the GitHub Actions workflow to run tests automatically on every push to `main`.

## Setup and Local Development

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CCLynch/ds6620_cicd_1.git
    cd ds6620_cicd_1
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run tests locally:**
    ```bash
    python -m pytest
    ```

## Continuous Integration

This project uses GitHub Actions for CI. Any push to the `main` branch will automatically trigger the workflow defined in `.github/workflows/ci.yml`. This workflow will:

1.  Check out the code.
2.  Set up a Python environment.
3.  Install project dependencies.
4.  Run all `pytest` unit tests.

If all tests pass, the build is considered successful.

### CI Status

[![Python CI](https://github.com/CCLynch/ds6620_cicd_1/actions/workflows/ci.yml/badge.svg)](https://github.com/CCLynch/ds6620_cicd_1/actions/workflows/ci.yml)
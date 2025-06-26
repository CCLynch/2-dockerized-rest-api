# Dockerized REST API

This project demonstrates the evolution of a simple Python library into a fully containerized RESTful API using Docker and Flask. The original CI pipeline for the library's unit tests has been adapted to test the new API endpoints within a Docker container, ensuring a consistent and reproducible environment.

The API provides standard CRUD (Create, Read, Update, Delete) operations for a simple collection of in-memory items.

[![Dockerized CI](https://github.com/CCLynch/2-dockerized-rest-api/actions/workflows/ci.yml/badge.svg)](https://github.com/CCLynch/2-dockerized-rest-api/actions/workflows/ci.yml)

## Project Philosophy

The primary goal was to create a standardized development and testing environment using containers. This approach solves the "it works on my machine" problem by packaging the application, its dependencies, and its runtime into a single, portable Docker image.

-   **RESTful Design**: The API follows REST principles, using different HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`) and endpoints (`/items`, `/items/<id>`) to manage a collection of resources.
-   **Test-Driven Development (TDD)**: The API endpoints were developed using a TDD approach. Tests were written first to define the expected behavior (including status codes like `200`, `201`, `404`), driving the implementation of the application code.
-   **Separation of Concerns**: The project uses two distinct `Dockerfile` configurations:
    -   `Dockerfile.api`: For building an image that runs the live API server.
    -   `Dockerfile.test`: For building an image that runs the `pytest` suite and exits, providing a clear pass/fail signal for CI.
-   **Automation**: User-friendly shell scripts (`run_api.sh`, `run_tests.sh`) simplify local Docker commands. A GitHub Actions workflow (`ci.yml`) automates the test execution on every push, ensuring code quality and reliability.

## Local Development and Testing

### Running the API

This command builds the API image and starts a container in the background.

```bash
# Make the script executable (only needed once)
chmod +x run_api.sh

# Run the script
./run_api.sh
```

The API will be accessible at `http://localhost:5001`.

To stop and remove the container:
```bash
docker stop rest-api-container
docker rm rest-api-container
```

### Running the Tests

This command builds the test image, runs the complete `pytest` suite inside a container, and then removes the container. The script will exit with a `0` on success and a non-zero code on failure.

```bash
# Make the script executable (only needed once)
chmod +x run_tests.sh

# Run the script
./run_tests.sh
```

## Continuous Integration

This project uses GitHub Actions to automatically build the test image and run the test suite on every push to the `main` branch. The workflow is defined in `.github/workflows/ci.yml`. The status badge at the top of this README reflects the result of the latest run.
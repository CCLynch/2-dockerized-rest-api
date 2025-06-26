#!/bin/bash

# Build the Docker image for testing.
echo "Building the test Docker image..."
docker build -f Dockerfile.test -t rest-api-tests .

# Run the Docker container from the test image.
echo "Running the tests in a Docker container..."
docker run --rm rest-api-tests

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Tests failed. Exit code: $EXIT_CODE"
fi

exit $EXIT_CODE

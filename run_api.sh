#!/bin/bash

echo "Building the API Docker image..."
docker build -f Dockerfile.api -t rest-api-app .

echo "Running the API container..."
docker run -d -p 5001:5000 --name rest-api-container rest-api-app

echo "API is running. Access at http://localhost:5001"
echo "To stop the container, run: docker stop rest-api-container"
echo "To remove the container after stopping, run: docker rm rest-api-container"
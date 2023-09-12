# Define the Docker image name and tag
DOCKER_IMAGE = hello-world-python:latest

# Define the name for your container
CONTAINER_NAME = hello-world-container

# Define the path to your Dockerfile
DOCKERFILE_PATH = .

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) $(DOCKERFILE_PATH)

# Run a Docker container from the built image
run:
	docker run -it --rm --name $(CONTAINER_NAME) $(DOCKER_IMAGE)

# Stop and remove the running container
stop:
	docker stop $(CONTAINER_NAME)

# Remove the Docker image
clean:
	docker rmi $(DOCKER_IMAGE)

# Help command to display available targets
help:
	@echo "Available targets:"
	@echo "  build       - Build the Docker image."
	@echo "  run         - Run a Docker container from the image."
	@echo "  stop        - Stop and remove the running container."
	@echo "  clean       - Remove the Docker image."
	@echo "  help        - Display this help message."

.PHONY: build run stop clean help

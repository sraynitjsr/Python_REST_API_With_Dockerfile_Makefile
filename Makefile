DOCKER_IMAGE = hello-world-img

CONTAINER_NAME = hello-world-container

PORT = 8080

build:
	docker build -t $(DOCKER_IMAGE) .

run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(DOCKER_IMAGE)

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rmi $(DOCKER_IMAGE)

help:
	@echo "Available targets:"
	@echo "  build       - Build the Docker image."
	@echo "  run         - Run the Docker container in detached mode."
	@echo "  stop        - Stop and remove the running container."
	@echo "  clean       - Remove the Docker image."
	@echo "  help        - Display available targets and their descriptions."

.PHONY: build run stop clean help

# Build Image
## docker build -t hello-world-img .

# Run Image
## docker run -d hello-world-container sleep infinity

# Get Inside The Container
## sudo docker exec -it hello-world-container /bin/sh

# Save Docker Image
## docker save -o hello-world-img.tar hello-world-python

# Build Image
## sudo docker build -t hello-world-img .

# Run Image
## sudo docker run -d --name hello-world-container hello-world-img sleep infinity

# Get Inside The Container
## sudo docker exec -it hello-world-container /bin/sh

# Save Docker Image
## sudo docker save -o hello-world-img.tar hello-world-python

# Makefile Build
## sudo make build

# Makefile Run
## sudo make run

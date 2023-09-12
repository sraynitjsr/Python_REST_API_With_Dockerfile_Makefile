# Option One, Running Docker Commands Manually
## sudo docker build -t hello-world-img .
## sudo docker run -d --name hello-world-container hello-world-img sleep infinity
## sudo docker exec -it hello-world-container /bin/sh
## sudo docker save -o hello-world-img.tar hello-world-python

# Option Two, Automated With Makefile
## sudo make build
## sudo make run
## Try => http://localhost:8080/helloWorld

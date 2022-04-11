**Jupyter Notebooks** are a popular way of accessing the compute power of a remote server but can be a bit difficult to install and maintain. In this example we will run Jupyter server in a docker container so all we need to install on the server is docker, and then run the Jupyter Server container in docker.<br>
To get an idea of the popularity of running Jupyter Notebook via Docker, try searching on Internet for "Docker Jupyter" [https://www.google.com/search?q=docker+jupyter](https://www.google.com/search?q=docker+jupyter)

## Docker
Install Docker (if you see different versions of docker to install, choose the CE version Community Edition, which is the totally free one):

Official install page:
https://docs.docker.com/engine/install/

On the cloud VM you will install for ubuntu and there is an official convenience install script (You can just paste this in the terminal on the Cloud Instance you have created):

    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh

If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:
    
    sudo usermod -aG docker <your-user>

Now when you have docker installed you can try running a docker command that downloads and run the "Hello world" container:

    sudo docker run hello-world
    
Another example is to run a docker container with latest ubuntu and print "Hello World" from inside the container. Inside the container `bash` is executing command `echo Hello World` and directing output into file `/data/hello-from.container.txt`

    sudo docker run ubuntu:latest /bin/bash -c "echo Hello World"
    
Another example is to run a docker container with latest ubuntu and print "Hello World" to a file from inside container, the `-v` switch is mounting your "Present Working Directory" to directory `/data/` in the container. Inside the container `bash` is executing command `echo Hello World` and directing output into file `/data/hello-from.container.txt`

    sudo docker run -v $PWD:/data ubuntu:latest /bin/bash -c "echo Hello World > /data/hello-from.container.txt"

Now you can check that the file is there by listing files in directory with `ls` command. And write contents of the newly file onto screen with `cat hello-from.container.txt`

You can create your own Docker image, but most of the time you will use images that are created by someone else, often the author of the program you want to use. Ready to go images are then stored in Docker Repositories, where [https://hub.docker.com/](Dockerhub) is the biggest one, you can browse all there images at: [https://hub.docker.com/](https://hub.docker.com/)


## Jupyter
When you have docker installed you can run Jupyter server as a container without need for installation.

Here is a list of official jupyter containers: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)

Here are official instructions for running jupyter with docker: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html

 [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html)

When running on the server we need to edit the commands from the official documentation a little bit:

You can use following parameters:

`--name notebook` (Name your running container - makes it easier to stop it)

`-p 8888:8888` Allow container to use port 8888 of computer

`--network host` (makes container part of your host computer network - easier without port-mapping, but less isolated)

`-v <local dir>:<container dir>` Mounts a directory or file on the host file system into the running container file system.


Example command if you want to run on the server: 

    sudo docker run --name notebook --network host -v $PWD:/home/jovyan --rm jupyter/scipy-notebook bash -c "jupyter notebook --ip 0.0.0.0 --port=8888 --no-browser --NotebookApp.default_url='/lab'"

Example command if you want to run on your local computer:

    docker run --name notebook -p 8888:8888 -v $PWD:/home/jovyan --rm jupyter/scipy-notebook

Now check the output of your command and if you are running on server change url ip from `127.0.0.1` to the Public Floating IP of your server, e.g. `http://127.0.0.1:8888/?token=922e19c80d0a0b2183f6346c5a429b1c2fa616ae9cf282f6` to `http://130.238.xx.xx:8888/?token=922e19c80d0a0b2183f6346c5a429b1c2fa616ae9cf282f6`

Use the url to access your Jupyter notebook!



### Stop your docker container

First list running containers:<br>
`sudo docker ps --all`

Stop a running container:<br>
`sudo docker stop <container id or name>`

Remove a running container:<br>
`sudo docker rm <container id or name>`






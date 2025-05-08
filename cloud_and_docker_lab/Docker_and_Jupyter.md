**Jupyter Notebooks** are a popular way of accessing the compute power of a remote server but can be a bit difficult to install and maintain.


They are especially beneficial for performing analyses directly on cloud resources because:

- **Remote Accessibility**: Jupyter Notebooks running on a cloud server can be accessed from anywhere using a standard web browser.
- **Computational Power**: You can leverage the high-performance computing resources (CPU, RAM, GPUs) available on cloud servers, enabling you to handle large datasets and computationally intensive analyses effortlessly.
- **Interactive Development**: You can run code snippets step-by-step, facilitating immediate feedback and iterative exploration.

#### Why Use Docker to Run Jupyter Server?

Docker is a containerization technology that simplifies software installation and configuration by encapsulating applications in a container—a lightweight, portable, and consistent runtime environment. Using Docker to run Jupyter Server offers significant advantages:

- **Easy Setup**: No complex installation processes or configuration issues. A single Docker command can set up your Jupyter environment.
- **Portability**: Containers can be easily deployed on any cloud instance, ensuring your analysis environment is consistent and reproducible across different systems.
- **Isolation**: Docker containers run independently, ensuring your host system remains unaffected by dependencies and conflicts, providing a secure and isolated environment.

In this task we will run Jupyter server in a docker container so all we need to install on the server is docker, and then run the Jupyter Server container in docker.
<br>
To get an idea of the popularity of running Jupyter Notebook via Docker, try searching on Internet for "Docker Jupyter" [https://www.google.com/search?q=docker+jupyter](https://www.google.com/search?q=docker+jupyter)

## 1. Install Docker on your cloud server

First you need to connect to your cloud server from the terminal:

    ssh ubuntu@<your floating ip>


On the server, Install Docker (if you see different versions of docker to install, choose the CE version Community Edition, which is the totally free one):

Official install page for reference:
https://docs.docker.com/engine/install/

    # install from ubuntu repositories
    sudo apt install docker.io


### Test your Docker installation

Now when you have docker installed you can try running a docker command that downloads and run the "Hello world" container:

    sudo docker run hello-world

You can create your own Docker image, but most of the time you will use images that are created by someone else, often the author of the program you want to use. Ready to go images are then stored in Docker Repositories, where [https://hub.docker.com/](Dockerhub) is the biggest one, you can browse all there images at: [https://hub.docker.com/](https://hub.docker.com/)


## Run Jupyter
When you have docker installed you can run a Jupyter notebook server as a container without need for installation.

Here is a list of official jupyter containers: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)

Here are official instructions for running jupyter with docker: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html

 [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html)

When running on the server we need to edit the commands from the official documentation a little bit, here is a example command if you want to run on the cloud server:

    sudo docker run --name notebook --network host -v $PWD:/home/jovyan --rm jupyter/scipy-notebook


Example command if you want to run on your local computer:

    docker run --name notebook -p 8888:8888 -v $PWD:/home/jovyan --rm jupyter/scipy-notebook

We have changed the following parameters from the official documentation:

`--name notebook` (Name your running container - makes it easier to stop it)
`-p 8888:8888` Allow container to use port 8888 of computer
`--network host` (makes container part of your host computer network - easier without port-mapping, but less isolated)
`-v <local dir>:<container dir>` Mounts a directory or file on the host file system into the running container file system.

### Accessing Your Jupyter Notebook

Once your container is running, Docker will output a URL similar to:

```
http://127.0.0.1:8888/?token=922e19c80d0a0b2183f6346c5a429b1c2fa616ae9cf282f6
```

If you're running Jupyter on a **remote cloud server**, replace `127.0.0.1` with your server’s **Floating IP address**.

For example, change:

```
http://127.0.0.1:8888/?token=922e19c80d0a0b2183f6346c5a429b1c2fa616ae9cf282f6
```

to:

```
http://130.238.xx.xx:8888/?token=922e19c80d0a0b2183f6346c5a429b1c2fa616ae9cf282f6
```

**Now open the updated URL in your browser — you should see the Jupyter Notebook interface!**


### Stop and remove your docker container

First list running containers:<br>
`sudo docker ps --all`

Stop a running container:<br>
`sudo docker stop <container id or name>`

Remove a running container:<br>
`sudo docker rm <container id or name>`






**Jupyter Notebooks** are a popular way of accessing the compute power of a remote server but can be a bit difficult to install and maintain. In this example we will run Jupyter server in a docker container so all we need to install on the server is docker, and then run the Jupyter Server container in docker.

## Docker
Install Docker (if you see different versions of docker to install, choose the CE version Community Edition, which is the totally free one):

Official install page:
https://docs.docker.com/engine/install/

On the cloud VM you will install for ubuntu and there is an official convenience install script (You can just paste this in the terminal on the Cloud Instance you have created):
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:
```
sudo usermod -aG docker <your-user>
```
## Jupyter
When you have docker installed you can run Jupyter server as a container without need for installation.

Here is a list of official jupyter containers: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)

Here are official instructions for running jupyter with docker: [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html


 [https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html)

When running on the server we need to edit the commands from the official documentation a little bit:

You can use following parameters:
--name notebook (Name your running container - makes it easier to stop it)
--network host (makes container part of jour host computer network - easier without port-mapping)


docker run --name notebook --network host -p 8888:8888 -e \
      -it ghcr.io/pharmbio/pharmbio-notebook:bigdata-spark bash -c "jupyter notebook --ip 0.0.0.0 --port=8888 \
      --allow-root --no-browser  --NotebookApp.password='' --NotebookApp.token=''"






Jupyter Notebooks are a popular way of accessing the compute power of a remote server but can be a bit difficult to install and maintain. In this example we will run Jupyter server in a docker container so all we need to install on the server is docker, and then run the Jupyter Server container in docker.

Install Docker (if you see different versions of docker to install, choose the CE version Community Edition, which is the totally free one):

Official install page (you can of course also install on your own computer if you want to try docker there as well)
https://docs.docker.com/engine/install/

On the cloud VM you will install for ubuntu and there is an official convenience install script::


curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Procedure for starting a Virtual Machine at SNIC Science Cloud

In this lab you will learn the basics of how to work with the OpenStack based Infrastructure-as-a-Service (IaaS). The lab can be done using Linux, Windows, or MacOS. The guide assumes you're using Ubuntu 22.04-LTS if you're on Linux or Windows-10 if you're on Windows. It should be completely doable on other linux distributions as well, and on any windows-version that is SSH-capable (i. e. has OpenSSH installed).

## Tasks

The aim of this lab is to give you hands-on experience with the cloud computing infrastructure. The SNIC Science Cloud (SSC) is an SNIC (Swedish National Infrastructure for Computing) national resource that provide Infrastructure-as-a-Service (IaaS). It is based on the OpenStack cloud software (Newton release).

In this lab you will perform the following tasks:

* Task 1: Creating a Key-pair
* Task 2: Creating a Virtual Machine
* Task 3: Install docker on the server and running Jupyter as a container
* Task 4: Optional. Restore a session from a snapshot.


### Important links:

1.	Information page: https://cloud.snic.se

The SSC information page contains links to the dashboard, to the OpenStack end-user guide (which you need to consult to complete the tasks below), as well as answers to many of the questions.

Good Luck!

## Task 1: Create a new SSH-keypair
SSH-key-pairs are the only way to access the generated instances at SSC. Username/Password logins have been disabled as per standard secure operating procedure for any safe cloud computing. Because of this, you will need to generate a SSH-keypair either through the Horizon GUI presented on the project page at SNIC (https://east-1.cloud.snic.se/project/), or by using the terminal to generate a local keypair on your computer. The procedure will be slightly different depending on your chosen platform.

A simple explaination of how ssh-keys works: http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html.

The OpenStack software helps you create/import keys, and will make sure that your public keys are injected in the instaces you create. The private key should be private and is for you to safekeep on your clients.

### Terminal Method
#### for Linux:

1.  Type `ssh-keygen` in the terminal
2.  The terminal will prompt you to select a key-install location. Just press ENTER to install it in the default location; this will allow your client to automatically find the key. The default location is `home/<user>/.ssh/` **OBS! NOTE:** if you already have a key with a given name **DO NOT OVERWRITE IT!** This will cause you to loose access to whatever your previous key was used for.
3.  The terminal will ask you for a password. Either keep it secure in your system, or add a password to it. This is up to you. If you wish to bypass the password, just press ENTER.
4.  You now have a keypair. Upload the .PUB key to the instance in task-2 when it asks you for keys

#### for Windows
Verify that OpenSSH is installed or Instal OpenSSH under settings -> apps and features -> optional features. It should come as standard on windows-10 if you have the latest build.

1.  Run cmd.exe as administrator
2.  Type `ssh-keygen` in the terminal
3.  The terminal will prompt you to select a key-install location. Just press ENTER to install it in the default location; this will allow your client to automatically find the key. The default location is `C:/Users/<username>/.ssh/` **OBS! NOTE:** if you already have a key with a given name **DO NOT OVERWRITE IT!**. This will cause you to loose access to whatever your previous key was used for.
4.  The terminal will ask you for a password. Either keep it secure in your system, or add a password to it. This is up to you. If you wish to bypass the password, just press ENTER.
5.  You now have a keypair. Upload the .PUB key to the instance in task-2 when it asks you for keys

#### for MacOS
1.  Type `ssh-keygen` in the terminal
2.  The terminal will prompt you to select a key-install location. Just press ENTER to install it in the default location; this will allow your client to automatically find the key. The default location is `Users/<user>/.ssh/` **OBS! NOTE:** if you already have a key with a given DO NOT OVERWRITE IT! This will cause you to loose access to whatever whatever your previous key was used for.
3.  The terminal will ask you for a password. Either keep it secure in your system, or add a password to it. This is up to you. If you wish to bypass the password, just press ENTER.
4.  You now have a keypair. Upload the .PUB key to the instance in task-2 when it asks you for keys

### OpenStack GUI Method (only do this step if above Terminal methods does not work):
1. 	Go to compute -> Key Pairs
2. 	Click on "+ Create new keypair" on the upper right corner
3. 	Name you keypair something unique, and select "SSH key" in the drop-down menu in the second field.
4. 	Download the key and move it to the .SSH folder in your ~/ (home/) directory. If there is no such folder, make it.
5. 	Make sure file access rights on your private key is limited to you only and remove any "other users" permissions on the key. If this is not done, you will not be able to log on to the cloud instance. If you get error "Permission is to open" then you need to open a terminal and execute `chmod 600 <path to your private key>` chmod 600 will make the file read/write for the owner only and no other users or groups.


## Task 2: Provisioning a Virtual Machine

1. 	Create a new security group under networks --> security groups. Name it something unique.
- Security groups in OpenStack are **virtual firewalls** so you can manage network traffic to and from virtual machines (VMs). Each security group contains a set of rules that define both inbound and outbound network traffic policies. These rules specify which traffic is allowed to enter or leave the VMs that are associated with the security group.
2. 	Click on "manage rules".
 	- Click on "Add rule", and open port 22 for ingress. (This is for ssh-access)
 	- Click on "Add rule", and open port 8888 for ingress. (This is for the Jupyter notebook that you might want to run on server in later example)
3. 	Start the "Instance Wizard" to generate an instance by clicking on "Launch Instance" under compute -> instance.
- An "instance" refers to a virtual server created within a cloud environment like OpenStack, AWS, or Google Cloud. It acts much like a traditional physical server but is hosted on a shared physical hardware infrastructure
4. 	In the launch configuration menu you'll be presented with a number of option; under details name your instance something unique. Leave the rest as default.
5. 	Under source you should select the OS (Operating System) Image you wish to run; for this excercise we will use Ubuntu 22.04-LTS. **OBS! Set "create new volume" to "No"**
6. 	Under flavor you select a flavor with up to 2 cpu and 2 GB memory.
- This allocates the size of your VM considering RAM memory and number of CPUs.
7. 	Under Security Groups you add your own custom group.
8. 	Under "Key-pairs" you select the key you generated in task-1.
    **NOTE: if you used the terminal version you need to upload your key from your .SSH folder.**
9.  Now the instance settings should be OK and it is time to press "Launch instance" to start it.
10. Go to Network -> floating IPs. Assign a floating IP to your VM.
- A Floating IP in a cloud environment like OpenStack is a public IP address that is assigned to your virtual machine (VM) so it gets an address on the internet and you can access it.
13. Now you can access the instance by connecting to it through an SSH-client (Terminal if on Linux, OpenSSH if on Windows) using `ssh ubuntu@<float-IP>`. If you created a key in the OpenStack GUI then you need to specify it with the `-i` option, e.g. `ssh -i <your private key file> ubuntu@<float-IP>`.
14. Install cowsay (first run `sudo apt update` then `sudo apt install cowsay`)
- The installation of cowsay is just a simple, lightweight method to confirm that the instance's setup is successful, particularly to see that you have the ability to install any software on your new virtual server. Cowsay is a program that generates ASCII pictures of a cow with a speech bubble containing specified text.
15. Test the installation by using cowsay. I.e. in the terminal of your virtual server type `cowsay -f tux "Hello World!"`

Now when you have a basic understanding of instance provisioning, please review the SSC user security guidelines: https://cloud.snic.se/index.php/user-security-guidelines/

## Task-3:

**Jupyter Notebooks** are a popular way of accessing the compute power of a remote server but can be a bit difficult to install and maintain. In this task we will run Jupyter server in a docker container so all we need to install on the server is docker, and then run the Jupyter Server container in docker.

Here is the detailed instructions for installing Docker on the server and running Jupyter as a container. OBS if you prefer to install and test docker and jupyter on your laptop instead you are more than welcome! You can use the same instructions: [Docker_and_Jupyter.md](Docker_and_Jupyter.md)


## Task 4 (Optional)

1.  Go to compute -> instances. Click "create a snapshot" in the dropdown menu for your instance. Name it something unique
2.  Delete your instance
3.  Now redo task-3. Can you still find your file using `ls` in the terminal? what about docker? can you still run `sudo docker run hello-world`? Now delete this instance.
4.  Redo task-3 with one difference; under SOURCE you should select Image in the SELECT BOOT SOURCE menu. Now you should be able to see the snap-shot you made available for selection. Load it into the instance. Then finish creating the instance. Can you find your file now? What about docker?

This guide was adapted from the technical manual found on
https://github.com/SNICScienceCloud/technical-training/tree/master/introduction-to-ssc#readme
last updated by sztoor.


# Procedure for allocation of Virtual Machines at SNIC Science Cloud - Redux 

In this lab you will learn the basics of how to work with the OpenStack based Infrastructure-as-a-Service (IaaS).  

## Tasks

The aim of this computer assignment is to give you hands-on experience with the cloud computing infrastructure. The SNIC Science Cloud (SSC) is an SNIC (Swedish National Infrastructure for Computing) national resource that provide Infrastructure-as-a-Service (IaaS). It is based on the OpenStack cloud software (Newton release) and Ceph storage and offers the following services:


In this lab you will perform the following five tasks: 

* Task 1: Creating a Key-pair
* Task 2: Allocating  Virtual Machine
* Task 3: Deploy a simple REST-endopoint enable service: "Cowsay as a Service" 

Please follow the instructions, execute the tasks and answer the related questions. 

### Important links:  

1.	Information page: https://cloud.snic.se

The SSC information page contains links to the dashboard, to the OpenStack end-user guide (which you need to consult to complete the tasks below), as well as answers to many of the questions. 

Good Luck!

## Task 1: Create a new SSH-keypair
SSH-key-pairs are the only way to access the generated instances at SSC. Username/Password logins have been disabled as per standard secure operating procedure for any safe cloud computing. Because of this, you will need to generate a SSH-keypair either through the Horizon GUI presented on the project page at SNIC (https://east-1.cloud.snic.se/project/), or by using the termnial to generate a local keypair on your computer. The procedure will be slightly different depening on your chosen platform.

### For Linux:
#### GUI Method:
1. 	go to compute -> Key Pairs
2. 	Click on "+ Create new keypair" on th eupper right corner
3. 	Name you keypair something unique, and select "SSH key" in the drop-down menu in the second field.
4. 	Download the key and move it to the .SSH folder in your ~/ (home/) directory. If there is no such folder, make it.
5. 	Disable all Sudo and "other users" permissions on the key. if this is not done, the cloud instance will not accept it.

A simple explaination of how it works: http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html. 

The OpenStack software helps you create/import keys, and will make sure that your public keys are injected in the instaces you create. The private key should be private and is for you to safekeep on your clients. 


## Task 2: Provisioning a Virtual Machine

1. 	Create a new security group under networks --> security groups. Name it something unique.
2. 	Click on "manage rules". Click on "Add rule", and open port 22 for ingress. 
3. 	Generate an instance by clicking on "Launch Instance" under compute -> instance.
4. 	in the launch configuration menu you'll be presented with a number of option; under details name your instance something unique. leave the rest as default.
5. 	Under source you should select the OS-image you wish to run; for this excercise we will use Ubuntu18.04-LTS. Keep "create new colume" on "YES" and "delete volume on instance delete" on "NO"
6. 	Under flavor you select "ssc.xsmall". this allocates the size of your VM.
7. 	Under Security Groups you add your own custom group.
8. 	Under "Key-pairs" you select the key you generated in task-0.
    NOTE: if you used the terminal version you need to upload your key from your .SSH folder.
9. 	go to Network -> floating IPs. Assign a floating IP to your VM.
10. Now you can access the instance by connecting to it through an SSH-client (Terminal if on Linux, OpenSSH if on Windows) using `ssh -i ~/.ssh/yourkey.pem ubuntu@<float-IP>`
11. install cowsay (sudo apt install cowsay)
12. test the installation by using cowsay. I.e. `cowsay -f tux "Hello World!"`
13. create a file

With a basic understanding of instance provisioning, please review the SSC user security guidelines: https://cloud.snic.se/index.php/user-security-guidelines/

## Task-3: Cowsay as a Service

Here you will deploy cowsay as an online service. You will need to create a python script and deploy it on your VM.

```bash
from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)


@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    data=subprocess.check_output(["cowsay","Hello student"])
    return data

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

```
You could do this by using the `echo "<code>" > cowsay-app.py` or pasting it directly through a terminal text editor such as VIM.

Run:

```bash
# python cowsay-app.py
```
It will start a webserver on your instance.

If you get any messages about missing packages, just go ahead and install them using “pip” (a Python package management system).

Test that things are working by executing (from your client)

Run: 
```bash
# curl -i http://<floating_ip>:5000/cowsay/api/v1.0/saysomething
```
If you are using Windows, use a Linux instance or install a cURL client for Windows.

####Disclaimer

This guide was adapted from the technical manual found on 
https://github.com/SNICScienceCloud/technical-training/tree/master/introduction-to-ssc#readme
last updated by sztoor.
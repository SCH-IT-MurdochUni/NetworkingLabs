I have written this activity with the idea that you will complete this in class as well as at home on your own Linux machine. If you are doing this in the labs, you will need to do this simultaneously with your partner next to you, as you will be sshing into each other's machines. At home, I suspect it may vary depending on your approach. If you do not yet have your own Linux machine at home, please see: [[Your own mobile Linux box]]

## Installing and running OpenSSH-server 

Start by ensuring that the machine that you are trying to ssh into has the openssh server installed. In ubuntu:

	sudo apt update
	sudo apt install openssh-server

You can check whether it is running with

	sudo systemctl status sshd

If you want to run it at boot you can do a 

	sudo systemctl enable sshd

If it is not running, you can start it with

	sudo systemctl start sshd
 
## Verify Connectivity

Before we do anything complex with keys, lets just verify that ssh works. If you are in the labs, you will need to trade IP addresses with your neighbor and

	ssh murdoch@[neighborsIPaddress]

the password would just be the word student

Verify that this works before moving on.

## Creating and installing the keys

To create the keypair, run:

	 ssh-keygen -t rsa

You can accept the defaults. Then cd into .ssh 

	cd .ssh

and examine the two files created:

	ls -la

You should see that you have created two files ''id_rsa'' and ''id_rsa.pub''. The ''id_rsa'' file is your private key and ''id_rsa.pub'' is your public key. I generally use scp to transfer the public key another machine. I would use:

	scp id_rsa.pub murdoch@[neighborsIPaddress]:/home/murdoch
	
This will put the file in your neighbour's /home/murdoch directory. 

The text found within ''id_rsa.pub'' should be appended to the file ''.ssh/authorized_keys'' in the other machine. After performing this operation, you should be able to login, from the machine that was transferred the public key, to the machine that ran ssh-keygen. Put your public key on any machine that you would like to automatically have passwordless login.

## Adding a hosts entry 

If you are logging into a machine frequently, and that machine has a static IP address, I would also add an entry into ''/etc/hosts''. Simply open the file

	sudo vim /etc/hosts

And add a simple line to the end, obviously substituting the IP address and name to one that is relevant for you.

	111.111.111.111 internet-server

After this, the following one line should log you into your server without a password

	ssh internet-server

## Contemplation and Discussion

Please chat with your partner and tutor about how you plan to approach [[Your own mobile Linux box]].


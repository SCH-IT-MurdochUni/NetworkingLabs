 _     _                    ____                  _               
| |   (_)_ __  _   ___  __ / ___|  ___ _ ____   _(_) ___ ___  ___ 
| |   | | '_ \| | | \ \/ / \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
| |___| | | | | |_| |>  <   ___) |  __/ |   \ V /| | (_|  __/\__ \
|_____|_|_| |_|\__,_/_/\_\ |____/ \___|_|    \_/ |_|\___\___||___/

In this lab, we will look at how command-line Linux servers can offer services. This lab will also continue our exploration of the command line, superusers, networking, and firewalls. We will continue to expand your knowledge of the command line by extracting compressed files and moving them between Internet-connected machines. 

If you are an External student, an online student, or a transnational student then complete this before proceeding: [[Linux Services#External Online & Transnational students]]. The reason that you must do this as an external, online on transnational student is because we need to set you up with two virtual machines on on your personal laptop/desktop.

If you are attempting this activity from the South St campus, you may need to reconfigure the Virtual Network adaptors. This video should show you how: https://echo360.net.au/media/6d282595-0fe6-4d11-9103-e25553cbae72/public

## Apache Web Server ##	

Let's start by installing and configuring the Apache webserver. Start by deploying the Ubuntu Operating system. Once you have booted into Ubuntu, open a terminal and type:

	sudo 	apt update

This command will consult the repositories about the latest software available for the distribution. Type

	sudo apt install apache2

This command will install the Apache web server. While we are installing software on our machines, let's install two additional pieces of software. Type

	sudo apt install nmap

Then: 

	sudo apt install openssh-server

Open up a web browser in the GUI and visit your own web page at http://127.0.0.1 
Discuss with your partner what is special about the 127.0.0.1 address

Find out what your Ethernet IP address is with:
	
	ip a

You'll also see a reference to the 127.0.0.1 address we used earlier.
Trade IP addresses with your partner and see if you can access each others web page. Their page should look identical to yours. If you have problems then ensure that you log out of the gateway.

Make some changes to the html of your Apache web page with:

	nano /var/www/html/index.html 
OR
	gedit /var/www/html/index.html

Two questions:

*  Did you get permissions errors when editing /var/www/html/index.html - how might you fix that?
*  What is the difference between nano and gedit?

Make some changes to your index.html page and get your partner to check your page.

## Nmap ##

Type:

	nmap [ipaddressofneighbor]

Nmap is a port scanning tool and will tell you what ports are open on a machine connected to the Internet. Have a look at the results. Can you identify any of the services that are running?

Try removing apache2 and then re-running the nmap test. 

	sudo apt remove apache2

What has changed and why? Reinstall Apache2 with:

	sudo apt install apache2

## UFW ## 

UFW is the Ubuntu firewall. We will use sudo to make changes, why? 

Try: 

	sudo ufw status verbose

Ask your neighbour to use nmap to scan your computer's ports.

Turn on the firewall:

	sudo ufw enable

Verify that the firewall is running by issuing the "status" command again:

	sudo ufw status verbose

Ask your neighbour to use nmap to scan your computer's ports. What has changed and why? Allow port 80

	sudo ufw allow 80/tcp

Get your neighbour to nmap your computer again. What can they see? Can they still access your webserver? What has changed?

## SSH ##

SSH is a program that allows you to get command-line access to machines on the Internet. A username and password are required to access another machine. See if you can log into your neighbour's machine via ssh with:

	ssh [ipaddressofneighbor_but_omitt_square_brackets]

If this does not work, could it be a firewall problem? Can you selectively open the port required for ssh?

### Create a new user ###

Look at the contents of:

	less /etc/passwd

Look through the entire file and think about what you are looking at. Then add a new user with: 

	sudo adduser [enter_a_new_username_but_omit_the_square_brackets]

You will need to set a password for that user. Look at the contents of:

	less /etc/passwd

What has changed?

### SSH revisited ###

By default if you just: 

	ssh [ipaddressofneighbor_but_omitt_square_brackets]

Then you will ssh using the username of the system that you are sitting on. Ask your neighbour for the username and password of their newly created user. To send a different username, try:

	ssh [username_no_brackets]@[ipaddressofneighbor_but_omitt_square_brackets]

See if you can login as their new user. Once you have finished, make sure you log out. You can do this with:

	exit

You should see the command prompt change back to your machine. If you have not returned to your regular machine. Type:

	exit

Again

## Dealing with compressed archives ## 

You will be familiar with compressing files in your regular operating system. In Linux, it is also easy to do this via the GUI but on a server, we will need to do this via the command line. 

Obtain the following 3 books; these are public domain books so this is completely free and legal:

*  https://www.gutenberg.org/files/76/76-0.txt
*  https://www.gutenberg.org/files/36/36-0.txt
*  http://www.gutenberg.org/files/12/12-0.txt

You can download them by right-clicking and doing "save as". Alternatively, you can:

	wget https://www.gutenberg.org/files/76/76-0.txt
	wget file2
	wget you get the idea ;)

Then, we want to create a Tar archive from the 3 files:

Create a directory called Books

	mkdir books

Then use the mv command to move the three books into the directory. I will leave you to do the move task on your own. 

After this type:

	tar cf books.tar books

You can now bzip this with

	bzip2 books.tar

If you now do a:

	ls -la

You should see ''books.tar.bz2'' - compare the filesize of ''books.tar.bz2'' with the sum of the three individual files. What sort of compression ratio did you observe?

If you wanted to you could decompress with:

	bunzip2 books.tar.bz2
	tar -xvf books.tar

If you finish this section wondering why compressing many files in Linux is important then consider how you might best physically move a large number of files on or off an Internet server.

## Extension Tasks ##

### Challenge 1 ###

Can you ssh into your neighbour's machine? Once you have logged into your neighbour's machine, see if you can create a text file on their desktop saying Hi_[neighborsname]

### Challenge 2 ### 

Try launching gedit while ssh'ed into your neighbour's machine. Was it successful? Why?

### Challenge 3 ### 

scp or secure copy works similarly to the cp command that we used last week. The format is:

	scp [source] [destination]

The difference between scp and cp is that scp is designed to be used over a network. It can copy a file or a set of files between any two Internet-connected Unix systems in the world.

See if you can use scp to securely copy a file between you and your neighbours PC. If you are stuck, see:

	man scp

Once you have worked out how to copy a single file between machines, see if you can copy all the files in a directory to a foreign machine. Try:

	scp [localpath] [ip]:/[path]

When you provide a path starting with a / this means that it is an absolute path. In this case, you would specify the entire directory structure.

### Challenge 4 ###

Download the top ten books from Gutenberg in UTF format. https://www.gutenberg.org/browse/scores/top

Compress them using the techniques in this lab and then scp them to your lab partner.

## External Online & Transnational students ##

To complete the lab above you may need two virtual machines. So start by cloning your current virtual machine in VirtualBox. You will need to stop it first, then right click and clone it. 
	
We then need to ensure that your two machines sit on the same network. To do this, you can follow the description below, or you can use this video guide: https://www.youtube.com/watch?v#98bz_It3UL8

In the Virtual Box application click File->Preferences, then click on Network.

Then the add button on the right to add a network.  

On each of your two virtual machines, go to Settings->Network. Within Network, change Attached to: Nat Network and then select the name of your NAT network. 

Make sure that both your virtual machines are switched off, then switch them back on again.

Check their IP addresses with a:

	ip a 

If you cloned your machines like I did, your two machines will have the same IP address. The reason they have the same IP address is because they have the same MAC address. The reason that they have the same MAC address is that cloned virtual machines are supposed to be IDENTICAL in every possible way. To fix this problem and proceed with the lab you need to re-initialize the MAC address. See: https://superuser.com/questions/655670/two-virtualbox-vms-running-in-parallel-assigned-same-ip/655746

See if they can ping each other

	ping [insert_ip_of_other_computer]

If this works see if you can SSH between the machines. Type:

	ssh [insert_ip_of_other_computer]


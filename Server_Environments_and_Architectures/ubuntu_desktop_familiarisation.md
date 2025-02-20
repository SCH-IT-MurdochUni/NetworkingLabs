```
 _   _ _                 _           ____            _    _              
| | | | |__  _   _ _ __ | |_ _   _  |  _ \  ___  ___| | _| |_ ___  _ __  
| | | | '_ \| | | | '_ \| __| | | | | | | |/ _ \/ __| |/ / __/ _ \| '_ \ 
| |_| | |_) | |_| | | | | |_| |_| | | |_| |  __/\__ \   <| || (_) | |_) |
 \___/|_.__/ \__,_|_| |_|\__|\__,_| |____/ \___||___/_|\_\\__\___/| .__/ 
                                                                  |_|    
 _____               _ _ _            _           _   _             
|  ___|_ _ _ __ ___ (_) (_) __ _ _ __(_)___  __ _| |_(_) ___  _ __  
| |_ / _` | '_ ` _ \| | | |/ _` | '__| / __|/ _` | __| |/ _ \| '_ \ 
|  _| (_| | | | | | | | | | (_| | |  | \__ \ (_| | |_| | (_) | | | |
|_|  \__,_|_| |_| |_|_|_|_|\__,_|_|  |_|___/\__,_|\__|_|\___/|_| |_|
                                                                    
```

In this lab, you will become more familiar with the Ubuntu Desktop environment, but we will try to emphasise the use of the command line as many Internet servers do not have Desktop Graphical User Interfaces (GUIs). Towards the end of this lab, we will show you all of the different ways that software can be installed and introduce you to file permissions. 

## GUI Familiarisation ##

Familiarise yourself with the Ubuntu Desktop environment. Work with the students around you, and your tutor, to do the following. 

* Open Firefox to check that the Internet works - If you are an internal South St student then your tutor will explain how this works in Linux.
* Start Libre Office and type some text
* Open the file manager and navigate up and down the directory structure
* Install a program from the Ubuntu Software Centre

If you place the terminal and the file browser side by side then it may help to visualise the changes that you make on the command line.

## CLI Familiarisation ## 

Open a Terminal by clicking on the Ubuntu start bar and typing terminal. Hit enter. It may also be helpful to open the file browser so that you can visualize some changes to the folder as you type the commands. 
 
Try out the following commands, If available, chat with your peers as you go.
 
	 ps -e

Then: 

	 top 

While you are looking at the information in top, press 1. What does this change? You can exit top by hitting "q". What are these commands doing?

Try the following:

	 ls

Then:

	 ls -la

What was the difference between these two commands?

Create a file with:

	 touch testfile

Then graphically edit it with:

	 gedit testfile

Depending on the version of your distribution, you may not have gedit. In this case, you could try:

	 featherpad testfile

Copy in a few paragraphs from an online article on Google. Save and exit. Now try:

	 nano testfile

What is the difference between gedit and nano. Do you think you could use gedit if you only had a remote terminal prompt? Why/Why Not?

There are some other ways that we could view rather than edit a file. What is the difference between:

	 cat testfile

And

	 less testfile

You can hit "q" to exit. Lets look at moving files around. Try:

	 cp testfile testfile2

Now run:

	 ls

Then try:

	 mv testfile2 testfile3

Rerun:

	 ls

What is the difference between cp and mv? 

Try:

	 ls -lah

How is this different from ls

Try the following: 

	 uname -a

What do you think this tells us? How is this different from:

	 lsb_release -a

Now try:

	 hostnamectl

Finally, the following is a useful ls command:

	 ls -alt

Look carefully at the output, what does it do? Hint: look at the dates and times

## Super User ##

Both Windows and Linux feature different user levels. In Windows, the all-powerful user is the administrator. In Linux the equivalent is root. In both cases it is recommended that, regardless of your skill level, you should operate as a regular user until you need to elevate your privileges. This way you are being deliberate about when you are assuming the status of Administrator or Root. 

Type:

	 whoami

This should echo back you username. Ok, lets try to do something that only the root user should be able to do. Lets try to add a new user. Type:

	 adduser [enter_a_new_username_but_omit_the_square_brackets]

You should find that the system responds to tell you that only the root user can do this. 

Type 
 
	 sudo whoami

A password will be requested. This will be the OS password that you logged in with. When you enter this, the system should respond with "root". Type:

	 sudo adduser [enter_a_new_username_but_omit_the_square_brackets]

You should now find that you can add a new user. Sudo is the current preferred way to temporarily become the root user on a Linux system, whenever you type sudo, you will be doing so with the privileges of the root user.

## Network Configuration ##

Open a new terminal and type
 
	 ip a

Ping is a connectivity test that you can use to determine whether two devices are connected. If you are on the South St campus, can you ping your neighbour?

	 ping [neighborsipaddress]

If you are completing from home can you ping Google's DNS server

	 ping 8.8.8.8

Does it work? Why/Why not. Discuss with your peer about what this address might do and how it works. Click on the network icon in the top right of the screen. Explore the graphical network configuration options.

### Hosts ###

If your computer or system frequently accesses other computers and you want to avoid typing in or remembering IP addresses, you can edit the hosts file to create something that locally resolves IP addresses. View the hosts file with: 

	 less /etc/hosts

Notice that you have an entry like:

	 127.0.0.1       localhost

From the command line ping local host

	 ping localhost

Ok, now lets add our own name, lets edit /etc/hosts

	 sudo nano /etc/hosts

Add the following line

	 8.8.8.8 GoogleEpicDNS

Now ping: 

	 ping GoogleEpicDNS

Hopefully you now understand how this file works.

### DNS ###

DNS works like the names file above, except it is shared across the entire Internet. Lets use a command-line tool to lookup google.com

	nslookup google.com

This should resolve an IP address. Take that IP address and plug it into your browser. Hopefully now you understand that DNS is just a widely shared lookup service for names. The difference between the hosts file, that we edited earlier, is that it is just localised to that computer. DNS works on any computer. 

If you ever want to know who to contact about a domain name then: 

	 sudo apt install whois

Then:

	 whois google.com

This should provide you with the email addresses in the case that you have a complaint to make.

### Public and Private IP addresses ###

On your computer, issue an:

	 ip a

This requires some skill to interpret but if you look closely, my IP address is:  

	 192.168.1.26

Now open your web browser and go to https://whatismyipaddress.com/

This should tell you a different address. What is going on here, why are different addresses being reported from different points in the Internet. We will discuss this again later in the unit but for now, have a quick read here about the difference between public and private IP addresses: https://www.geeksforgeeks.org/difference-between-private-and-public-ip-addresses/

## Hardware ##

Try the following commands. 

	 lsusb

Then:

	 lspci

Then:

	 less /proc/cpuinfo 

Discuss with your partner what these commands are showing you. How many cores does the computer have? 

Find "About this Computer", which is located under settings in the GUI. Is it more or less useful? Which do you prefer?

## Redirecting output to a file ##

We can redirect the output from a script or program, into a file. Try the following:

	 lsusb > output_of_lsusb

What do you think this is doing?
	
	Try:

	less output_of_lsusb

And

	cat output_of_lsusb

What is the difference between "less" and "cat". How big is the file you just created?

	ls -la output_of_lsusb

You can remove it with:

	rm output_of_lsusb

## Installing Software ##

Installing software can feel a little different on Linux systems, in this section, we will try to compare and contrast different options for installing software, while constantly thinking about how this differs from, or is similar to, your current experience. 

### Software as a Service ###

This has been growing as a preferred software model over the last decade. Typically this software requires no installation, as you access and use it through a web browser. Office 365, Google Drive/Docs and Grammarly are all examples that you should be familiar with. In this case, there is no difference between Windows, MacOS or Linux based systems. Generally, the only pre-requisite is that you sign up for an account and have a supported web browser. 

### Downloading and Installing a binary from the web ###

You will be familiar with this but I am probably just using new terms to categorise this familiar task. You will probably be familiar with installing an alternative web browser from the internet. In Windows, you would be familiar with .exe files. Which are executables that will install programs? In MacOS these are .dmg files.

You can also obtain software for Linux this way, On your Ubuntu system, visit the Google Chrome webpage and install Chrome. Note that while the file extension is a .deb there are many different ways to package binaries, most notably .rpm which is used by Red Hat type distributions. If you already have Chrome or would just like to try something new, have a look at installing [https://www.opera.com/ Opera], currently my browser of choice.

### Downloading and Installing a binary a trusted repository ###

If you have an iOS or Android smartphone, these are both Unix/Linux systems by the way, you will be familiar with the Apple App Store or Google Play. When you download software through these apps, you are again downloading a binary but you are doing from a repository where there has been a degree of checking from Apple/Google. 

While this may seem like a relatively recent concept, Linux based distributions have been doing this for decades. Install some software using this method in Ubuntu Linux. Open an app called Ubuntu software centre and see if you can install an alternative word processor to Open/Libre Office. 

After you have installed some software from a repository, lets consider how this works. Type the following command into a terminal:
 
	 less /etc/apt/sources.list

What do you think this file contains. Talk to your neighbour and your tutor if you are unsure. You can exit from less by hitting q. 

Type the command:
 
	 sudo apt update

What do you think this command does? Talk to your neighbour and your tutor if you are unsure.

Try 

	 sudo apt upgrade

This is how you would install OS system updates in a Linux system. Feel free to install the updates and watch the process.

Remember that Linux servers on the internet rarely use Graphical User Interfaces, even if they are serving web content. This means that you need to be familiar with installing software via the command line only 

Use apt to install the Video Lan Media player via the command line. You can search the apt repository on the command line using:

	 sudo apt search [keyword]

You could use the keyword vlc to install that software package. You can install software with:

	 sudo apt install [software_name_omitting_brackets]

### Installing from source code ###

Although it is increasingly uncommon, sometimes we need to install software from the source code. You may want to do this if you want to try a pre-release of some software, or you wish to use an old version or if the software is simply niche and someone hasn't pre-compiled binaries for Windows, MacOS or Linux. Also, if you are an advanced coder, you may want to check exactly what the software is doing and the only way to do this is to read the source code. Another reason might be that you want some code to run on a piece of hardware where no pre-compiled binary exists, so you want to run a regular piece of software on an ARM chipset where no binary has been compiled. 

If you are learning software development and want an easy environment to compile your c code, this should also be of interest.

To get the tools to compile C programs, make sure that build-essential is installed.

 sudo apt install build-essential

Ok so lets take a hello_world example:

```
#include <stdio.h>
int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!\n");
   return 0;
}
```

Take the above code and save it as:

	hello_world.c

Compile it with

	gcc hello_world.c -o hello_world_executable

You can then execute it with:

	./hello_world_executable

If you get permission type errors, then you need to make the file executable. We will cover this properly in future weeks but for now, you can change the permissions with:

	chmod 777 hello_world_executable

Congratulations, you now know how to compile code from source. Compare the source code with the machine code:

	less hello_world.c 
	less hello_world_executable

Think about why they are different.

### Reflection ###

Reflect on all the different ways to distribute software that we have covered. What are the pros and cons of each approach for you as a user? What are the pros and cons of each approach if you are a software development company?


```
    _                                     _____ ____ ____  
   / \   _ __ ___   __ _ _______  _ __   | ____/ ___|___ \ 
  / _ \ | '_ ` _ \ / _` |_  / _ \| '_ \  |  _|| |     __) |
 / ___ \| | | | | | (_| |/ / (_) | | | | | |__| |___ / __/ 
/_/   \_\_| |_| |_|\__,_/___\___/|_| |_| |_____\____|_____|
                                                           
__        __   _       ____                  _               
\ \      / /__| |__   / ___|  ___ _ ____   _(_) ___ ___  ___ 
 \ \ /\ / / _ \ '_ \  \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
  \ V  V /  __/ |_) |  ___) |  __/ |   \ V /| | (_|  __/\__ \
   \_/\_/ \___|_.__/  |____/ \___|_|    \_/ |_|\___\___||___/
                                                             
```


This lab will introduce you to Amazon EC2 web services. By the end of this lab you will have a virtual machine running at a location of your choosing and serving files via an Apache web server. In subsequent weeks we will link this virtual machine to DNS.

Note that this lab is designed around using Amazon EC2 Web services, but you are not restricted to this choice at all. Just like we encourage studnets to try VirtualBox and Vmware, you are encouraged to compare and choose between: 
* [Amazon EC2](https://aws.amazon.com/ec2/)
* [Amazon Lightsail](https://aws.amazon.com/lightsail/)
* [Microsoft Azure](https://portal.azure.com/)
* [Digital Ocean](https://www.digitalocean.com/)
* [Vultr](https://www.vultr.com/)


This lab assumes that you have viewed the weekly videos and that you have an account with Amazon EC2. The lab is written around you using your Linux VM that are running, or the lab machines, but it should work just fine on MacOS or Windows. Just like Linux, you will need to ensure that you are executing your ssh commands in the same directory as the .pem file that you download from Amazon.

## Log in to the Amazon EC2 Management Console ##

To start the lab, log into the Amazon EC2 management console: http://aws.amazon.com/ec2/

For the purposes of the signup, being a Business or School and using your Murdoch email has had reports of the fewest delays with credit card checks.

## Launch an Ubuntu Machine in EC2 ##
* Launch a new instance (virtual machine)
* Follow the steps on the AWS site. 
* Instance type - Pick a "free tier eligible" Ubuntu 20.04 Instance.
* Configure the instance details - You can leave everything as the default.
* Add storage - The default is to create a virtual machine with an 8GB hard drive. That's fine, leave it at the default.
* Add tags - There is no need to add any tags so continue to "Configure Security Group".
* Configure Security Group
*  Security group name - Call it "ssh-and-web"
*  There is an existing SSH permission that is needed to manage your remote server, that is fine.
*  Click "Add Rule" and select HTTP (web) as the type.  This allows web requests to be received by our server.
* Review and Launch
* There may be a warning that your server is "open to the world".  That's fine, we are building a public webserver!
* If you are happy with the configuration, click "Launch".
* Create a new "key pair".  AWS uses key files rather than a username and password to verify your identity when logging into your virtual machine.  If you lose this file it is unlikely you will be able to mange your virtual machine so it is important to keep it safe.  Give it a meaningful name like "webserver-key" so that you can identify it later.
* Launch Instance - Click on "Launch Instance" and your server will start. After this you can use "View Instance" to monitor it's progress.

## Console Access to the Virtual Machine ##
Now that your server is running in the cloud you need to login to the command line of your virtual machine. If you select your virtual machine and click the "connect" button. Then click on SSH client and note the string provided. 

Open Powershell, the Linux command line or the MacOS terminal on yur device. Then use 'cd' to move to the directory where you downloaded your key. Then you can paste the string that was provided to you above. It shuold look something like: 

    ssh -i "yourkeyname.pem" ubuntu@ec2-12-123-1-35.ap-southwest-5.compute.amazonaws.com

You should now have SSH access to your cloud machine. 

## Install Apache ##

Once you have command-line access to your virtual machine, the apt repositories may be out of date. Before you install anything, it is often a good idea to update them with 

	sudo apt update

Install the Apache Web Server using:

	sudo apt install apache2

Test by visiting your new webserver. On your machine sitting in front of you, you should be able to type the Amazon machine's IP into your web browser.

## Edit index.html on the Webserver and test ##

Once the machine has been launched, try to modify /var/www/html/index.html with

	nano /var/www/html/index.html

If you get permission problems with this command, think carefully about the best approach to editing it.

This will ensure that your page is unique. Browse to your web page using a web browser to ensure it is working. You can find the Public IP address of your webserver on the AWS console page.

Paste that IP address, with http:// before the IP address into your browser. Note that modern browsers will try to force https:// so you will need to ensure that you are actually visiting the http site.

## Linking to files from your webserver ##

Now that we are building confidence with editing our index.html, we are going to push the boundaries a bit an link to some actual files. You can  download files from the Internet straight to your machine in the cloud with wget.

As an example try:
	
	wget http://www.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf

This command should download the weekly reading into your /home/ubuntu directory. You would then need to move it into the /var/www/html directory using sudo. Try: 

	sudo cp EECS-2009-28.pdf /var/www/html/

Now we can try to access that pdf file remotely via a web browser. You will need to add that file name preciscely to the end of your website string.

If you have difficulties accessing the file via a browser, here are some potential issues:
* At times Apache has changed the default directory from which it serves HTML.  /var/www or /var/www/html are common.  One way to find out where the files are being served from is to locate the existing "index.html" file and place your files in the same directory.
* Rights and ownership can also be an issue.
** Some Apache installs require the owner to be the user www-data.
** Check that there are Read rights to the file.

## Create Links in index.html ##

Once these files have been uploaded, you should create a link to the file by modifying the HTML in index.html. You can insert the following html into index.html as an example of how to create hyper-links to files. 

	<a href="filename.pdf">Click here</a>

You should ensure that the path for your pdfs matches the path that is shown below. Hint - you may need to add a directory and move some files around. Hints:

	mkdir
	mv

## Test ##

Test your configuration. Get your lab partner to try to download one of your files. Alternately, try downloading a file via your smartphone or laptop. Again, be careful to ensure that you are accessing the http page and not the https page. We will do https next week.

Once you have done this successfully, congratulations! You can now access any of the files you uploaded from anywhere in the world. Please do be aware that the web page you have created is not secure and any materials that you upload onto that webpage can be viewed by anyone.

## Budgets and Costs - Super Important! ##

If you won't be using your instance anymore, you may wish to shut it down or terminate (delete) it to decrease the chances of inadvertently running multiple instances and incurring EC2 usage charges. It is easy to launch instances in different countries and not notice them running. Remember that cloud-based services are often billed on the run-time of your server.  Be particularly careful if you launch an expensive instance featuring large memory, fast CPUs or GPU processors. 

At the most simple level, you want to ''click on your name in EC2 and go to My Billing Dashboard''. See the image to the right. You should be able to reconcile the costs that you see here.

You will also want to set a budget, with an alert as well. Make sure that you follow the slideshow below, to set an actual budget and an alert. To get started ''click on your name in EC2 and go to My Billing Dashboard'' then look for the AWS budgets link, as indicated in the first image in the slideshow below. Then follow the text description below the slideshow to setup a budget with alerts.

## Challenges ##

### Challenge 1 ###

*Try pinging some servers in different parts of the world. Look at the round trip time or latency. Does it match up with your expectations?
*What are some alternatives to Amazon EC2?

### Challenge 2 ###

If you have local files on your Linux machine then you can move them onto the webserver with the following command:

	scp -i your_pem.pem file_to_upload ec2-user@[dns_entry_or_IP_address]:/home/ec2-user

This command will move file_to_upload into /home/ec2-user. Remember that SCP or Secure Copy is using the SSH port (22) to copy files. Once the file has been transferred to /home/ec2-user you can then move the file to /var/www/html/

### Challenge 3 ###

Learn some basic HTML and try to create your own index.html page.


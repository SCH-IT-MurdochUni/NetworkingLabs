```
 ____            _       _   _               _     _                  
/ ___|  ___ _ __(_)_ __ | |_(_)_ __   __ _  | |   (_)_ __  _   ___  __
\___ \ / __| '__| | '_ \| __| | '_ \ / _` | | |   | | '_ \| | | \ \/ /
 ___) | (__| |  | | |_) | |_| | | | | (_| | | |___| | | | | |_| |>  < 
|____/ \___|_|  |_| .__/ \__|_|_| |_|\__, | |_____|_|_| |_|\__,_/_/\_\
                  |_|                |___/                            
 ____                             _____                 _   _                 
/ ___|  ___ _ ____   _____ _ __  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
\___ \ / _ \ '__\ \ / / _ \ '__| | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 ___) |  __/ |   \ V /  __/ |    |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
|____/ \___|_|    \_/ \___|_|    |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
```

The goal of this week is to write a script that will backup the contents of /home/ubuntu/Documents into /home/ubuntu/backup. This backup script should use cron to schedule it every hour. The name of the backup file should be the date of the backup. We will also export the backup to the cloud. The lab below is not a step by step guide. It is expected that you will have watched the videos. Each section below describes how to do an individual piece of the solution. It is your job to combine them to achieve the backup function described above. You should be constantly testing your script as you add functionality to it. 

The lab below assumes that you are logged in as the user ubuntu, but if your username is different then just remember to adapt the commands.

== Some Bash basics ==

=== Hello World! ===

Try running the following code. 

```
 #!/bin/bash
 # This is a bash comment 
 echo "Hello Bash World!"
```

You will need to save the code as in a text editor, provide privileges

	chmod 777 somecode.sh

Then execute:

	./somecode.sh

=== Variables ===

Modify your current code using the following code snippets

Bash
	a="Hello bash using variables"
	echo $a

Make sure you understand everything before moving on.

=== Basic calculations ===

Lets add some calculations to our previous code:

Bash
```
 a=10
 b=5
 c=$((a+b))
 echo $c
```

Once you understand, I would like you to modify the examples so that you are familiar with subtraction, multiplication and division.

=== Modify the Code 1 ===

Examine the following code snippet written in Bash.

Bash
```
 #!/bin/bash
 for ((i=0;i<10;i++)); 
 do 
   echo $i
 done
```

Modify the code snippet to sum each number in the sequence. 

== Creating the backup script == 

=== Create files and folders ===

Create a bunch of files and folders within /home/ubuntu/Documents with:

```
 touch file1
 touch file2
 touch file3
 touch file4
 touch file5
 mkdir testfolder
 cd testfolder
 touch file11
 touch file22
 touch file33
 touch file44
 touch file55
```

These are the files and directories that your script will backup. So with the commands above we are deliberately creating files and subdirectories within /home/ubuntu/Documents

=== Creating a basic script ===

Create a file with all of the commands you will use. To reiterate, we are creating a backup script, the goal is to list the commands required to recursively copy all the files from /home/ubuntu/Documents and put them in /home/ubuntu/backup. You would need to create the backup directory. The recursive copy command that you will need to backup all the files and subdirectories are shown in the videos this week. 

List each command, that your script will execute, on a new line within a file called testscript.

	nano /home/ubuntu/testscript

Give the file execute permissions, you should know this command now. Then test by executing the file:

	./testscript

Remember that you cannot recursively copy from one set of folders into the same set of folders so best to copy from /home/murdoch/Documents into /home/murdoch/backup.

=== Making the script available system wide ===

Your script is in the current user's home directory which may not be accessible to other users.  Scripts which are to be used by all system users are better stored in a common location where individual users have the rights to read and execute them but not to delete them.

Allow your script to be available system wide by moving it to the /usr/bin directory with the command below. Remember that when you edit the file it will now be /usr/bin/testscript 

	sudo mv /home/ubuntu/testscript /usr/bin/testscript

As we ran the previous command with sudo, we need to change the owner 

	sudo chown ubuntu /usr/bin/testscript

Test whether the file is available to be executed system wide. Make sure you are not in the same directory as your test script when you run the following from the command line.
 
	testscript

Linux can find your script even though you didn't tell it where to look because there are a series of paths that are automatically checked when a command is typed.  You can see these paths by displaying the system variable $PATH.  Try the following:
 
	echo $PATH

=== Creating an archive ===

The current backup script is a little primitive. Let's zip up all of the files and provide a date as the filename. Integrate the following subsections into a bash script that will zip up the desired files and folders, and provide a dd/mm/yy filename.

=== Zipping ===

The following command will zip all files in the current directory and name the archive as zippedfile.

	zip zippedfile *

=== Adding the date ===

You can create a variable in your script called now and insert the date into it, using dd/mm/yy format with:

	now=$(date +"%d_%m_%y")

You can then use that date in a file name. For example:

	mv currentfile $now

The previous command will change the name of currentfile to $now

Modify your script so it creates a zipped copy of your directory with a filename that reflects the current date.
Remember most command-line utilities such as zip have inbuilt help.

	zip --help

===  Cron ===

Edit Cron with the following 

	sudo nano /etc/crontab

Modify a line to ensure that your script will run every hour. The order is: minute, hour, day of the month, day of the week, user, command to run. You can use an asterisk to indicate any/every.

My crontab file looked like:

```
 # m h dom mon dow user command
   9 * *   *   *   root /usr/bin/testscript
```

It is likely that the entry you are making is not the only entry that will be present on your system.

=== A quick Power Mangement detour ===

Set aside your backup script for a moment. Sit back and think about the skills you have just developed. Use the following code on your Linux virtual machine running locally, not your cloud-based machine. We are going to do some power management. The suspend and Hibernate states on computers use a fraction of the power or energy as compared when running. 

The bash below will send your Linux device into a suspend state. Lets see if we can test this on the command line first:

	sudo bash -c "echo `date '+%s' -d '+ 30 seconds'` > /sys/class/rtc/rtc0/wakealarm"
	sudo systemctl suspend

Once you understand how this works, try getting cron to run this at a scheduled time in the future. Think carefully about how we might be able to use something like this to sleep computers at 6:00pm for 12 hours, until 6:00 am the next morning.

=== Exporting your backup to the Cloud ===

Once we have a script that will zip up a set of files, provide a date based file name and do this automatically using cron, then you can look at exporting this backup to the cloud.

You can scp this file onto your Linux server in the cloud with the following. 
 
	scp -i [your_pem].pem [file_to_upload] ubuntu@[dns_entry_or_IP_address]:/home/ubuntu

Once you have successfully integrated this into your code then you can move on.

=== Solution ===

The script that I used is below. There are some sticky issues that are difficult for students to understand so this is a challenge. As cron runs as root, it assumes the working directory, so I generally got around by providing complete paths. I also needed to have ssh'd once from my root user to my cloud server so 

	sudo ssh -i thursday.pem ubuntu@53.117.232.219

This is needed to accept the certificate. 

```
now=$(date +"%d_%m_%y")
cp -R /home/david/Documents/* /home/david/backup/
zip -r $now.zip /home/david/backup/*
cp $now.zip /home/david/
scp -i /home/david/thursday.pem $now.zip ubuntu@53.117.232.219:/home/ubuntu/
</pre>
```

== Challenge 1 ==

Take the script that you have created and get it to run at boot time. You can check out the weekly video which will describe how to run scripts at boot time.

== Challenge 2 ==

See the image at the top of the page. Explore neofetch and figlet. Think about how they could be used to display information when users login. See if you can work out how to use them in the Linux message of the day to craft a unique greeting when a user logs in. See [[Linux_MOTD]]


[[File:lecture.png|right|thumb|x250px|alt#The old lecture you would receive from Linux when first elevating your privileges |The old lecture you would receive from Linux when first elevating your privileges]]
The ability to change the permissions of files to fit the intended need and purpose is crucial to running a secure system. This lab will test you on your understanding and ability to manipulate file permissions in Linux.

Log in to your Ubuntu machine and open a terminal by clicking the Ubuntu icon in the top left of the Desktop screen.

Create three different users: Alice, Bob and Mallory. Create a directory called 'shared' in /home/. Create ten files inside it. Ensure that this folder has the User group and permissions to ensure that:
* Alice can read, write and execute files
* Bob can read and execute files, but cannot write to them
* Mallory can neither read, write or execute files

To complete this, you will need to use group membership.

Commands Required:  Square brackets indicate optional fields.  Keep in mind that some of these commands may require [sudo]. 
[[File:permissions.jpg|right|thumb|x350px|alt#Linux Permissions|Linux Permissions]]
```
 sudo
 ls [-l]
 groupadd
 adduser [bob] [awesomegroup]
 deluser [bob] [awesomegroup]
 less /etc/passwd
 less /etc/group
 delgroup
 chmod
 chown
 chgrp
 rm
 mkdir
 touch
 su [alice] [bob] [mallory] -s /bin/bash
 whoami
```
Make sure you check the permissions from the perspective of the user you created.  That is you must log in as that user. You can use the ''su'' command to switch between users and the ''whoami'' command to check your work. You may also want to use the '''-R''' flag, to recursively make changes. As an example: 
```
 chown -R
 chgrp -R
```
### Challenge ###

Can you work out how to put Mallory in the sudoers group. Work out how to do this, implement and then test. How does this change access to files for Mallory?

When you are finished, recursively delete the folder and all files within.


```
 ____            _        ____          _ _               _          _     
| __ )  __ _ ___| |__    / ___|___   __| (_)_ __   __ _  | |    __ _| |__  
|  _ \ / _` / __| '_ \  | |   / _ \ / _` | | '_ \ / _` | | |   / _` | '_ \ 
| |_) | (_| \__ \ | | | | |__| (_) | (_| | | | | | (_| | | |__| (_| | |_) |
|____/ \__,_|___/_| |_|  \____\___/ \__,_|_|_| |_|\__, | |_____\__,_|_.__/ 
                                                  |___/                    
```


Lab Structure
Introduction to Linux and Bash
Navigating the File System and Managing Files
Creating and Executing Basic Bash Scripts
Implementing Loops and Conditionals
Automating System Monitoring Tasks
Enhancing Security with Bash Scripting
Challenging Tasks and Extensions
###  Introduction to Bash


The Linux terminal is a powerful tool that allows users to interact with the operating system through text-based commands. Bash (Bourne Again SHell) is the default command-line interpreter for most Linux distributions, including Ubuntu.

### Navigating the File System and Managing Files

Familiarize yourself with essential Linux commands that will be frequently used in scripting:

You should now be roughly familiar with the following commands  

```
pwd	Displays the current directory path.
ls	Lists files and directories.
cd	Changes the current directory.
mkdir	Creates a new directory.
touch	Creates a new empty file.
cp	Copies files or directories.
mv	Moves or renames files or directories.
rm	Removes files or directories.
echo	Displays a line of text/string.
cat	Concatenates and displays file content.
```

Open the Terminal:

Locate the terminal icon on your desktop or access it via the applications menu.
Display Current Directory:

Create a new directory:

    mkdir LabFiles
    cd LabFiles

Create a New File:

    touch notes.txt

Write Content to the File:

    echo "This is a Bash scripting lab." > notes.txt

Display File Content:

    cat notes.txt

Copy the File:

    cp notes.txt backup_notes.txt

Rename the File:

    mv backup_notes.txt old_notes.txt

Remove a File:

    rm old_notes.txt

Reflection Questions
 * What command did you use to create a new directory?
 * How can you view the contents of a file without opening it in a GUI besed text editor?
 * What is the difference between cp and mv commands?

### Creating and Executing Basic Bash Scripts

Bash scripts are text files containing a series of commands that the Bash interpreter executes sequentially. They are used to automate repetitive tasks, manage system operations, and perform complex workflows.

    cd ~/LabFiles

Create a New Script File:

    nano hello_world.sh

Add the Following Content to the Script:

    BASH
    #!/bin/bash
    echo "Hello, World!"
    Save and Exit:

Press CTRL + X, then Y, and ENTER to save the file.
Make the Script Executable:

    chmod 777 hello_world.sh

Execute the Script:

    ./hello_world.sh

    nano hello_world.sh

Modify the echo Command:

    echo "Welcome to the Bash scripting lab!"

Save and Execute:

    ./hello_world.sh

Reflection Questions
 * What is the purpose of the chmod +x command?
 * Why do we use the shebang (#!/bin/bash) at the beginning of scripts?
 * How can you modify the script to display a personalized message?

### Implementing Loops and Conditionals

Loops allow repeated execution of a set of commands. Common loops include for, while, and until.

Conditionals enable scripts to make decisions based on certain conditions using if, elif, else statements.

Create a New Script:

BASH
    nano system_info.sh

Add the Following Content:

BASH

```
#!/bin/bash

echo "System Information Script"

# Display current user
echo "Current User: $(whoami)"

# Loop through the next five numbers
for i in {1..5}
do
    echo "Iteration: $i"
    sleep 1s
done

# Conditional Statement
read -p "Enter a number between 1 and 10: " number

if [ "$number" -le 5 ]; then
    echo "You entered a number less than or equal to 5."
elif [ "$number" -le 10 ]; then
    echo "You entered a number greater than 5 but less than or equal to 10."
else
    echo "Number out of range."
fi
```

Save and Make Executable:


    chmod 777 system_info.sh

Run the Script:

    ./system_info.sh

Sample Interaction:

Reflection Questions
 * How does the for loop in the script operate?
 * What happens if a user enters a number greater than 10?
 * How can you modify the script to handle invalid inputs gracefully?

### Automating System Monitoring Tasks

Automate the monitoring of system resources such as CPU usage, memory usage, and disk space.

Create a New Script:

    nano resource_monitor.sh

Add the Following Content:

```
BASH
#!/bin/bash

echo "System Resource Monitoring"

# Number of iterations
read -p "How many times would you like to monitor the system? " iterations

# Loop based on user input
for ((i=1; i<=iterations; i++))
do
    echo "----- Monitoring $i -----"
    
    # Display CPU usage
    echo "CPU Usage:"
    top -b -n1 | grep "Cpu(s)"

    # Display Memory usage
    echo "Memory Usage:"
    free -h

    # Display Disk usage
    echo "Disk Usage:"
    df -h | grep "^/dev"

    echo "-----------------------"
    sleep 5s
done

echo "Monitoring complete."
```

Save and Make Executable:

chmod 777 resource_monitor.sh

Run the Script:

    ./resource_monitor.sh

Reflection Questions
 * What information does the free -h command provide?
 * How can you modify the script to monitor network usage?
 * Why is automating system monitoring beneficial for administrators?

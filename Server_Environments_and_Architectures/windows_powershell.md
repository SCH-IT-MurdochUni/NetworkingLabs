```
__        ___           _                   
\ \      / (_)_ __   __| | _____      _____ 
 \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / __|
  \ V  V / | | | | | (_| | (_) \ V  V /\__ \
   \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ |___/
                                            
 ____                        ____  _          _ _ 
|  _ \ _____      _____ _ __/ ___|| |__   ___| | |
| |_) / _ \ \ /\ / / _ \ '__\___ \| '_ \ / _ \ | |
|  __/ (_) \ V  V /  __/ |   ___) | | | |  __/ | |
|_|   \___/ \_/\_/ \___|_|  |____/|_| |_|\___|_|_|
                                                  
```

## PowerShell Introduction ##

PowerShell is the newest and most powerful offering from Microsoft providing a command shell and configuration toolkit built on the .NET framework. More interesting still, is the fact that PowerShell also supports the management of network devices and Linux machines, and also can be installed on Linux. As you will see at the end of this lab, Linux can also be installed on Windows too.

Windows has a long history of supporting command line and scripting tools. Even before PowerShell arrived on the scene, the Windows Scripting Host (WSH) provided support for power users to develop their own scripts and interact directly with operating system objects.

PowerShell is here to stay. The current attitude is that if a proposed Windows Server feature does not integrate with PowerShell, then they won’t release it. This assures administrators that they will be able to perform all manner of administrative scripting tasks with current and future iterations of Windows Server. Similar to Linux Bash scripting, Powershell will initially seem quite daunting.

Let’s look at a few small examples. We will use the PowerShell integrated scripting environment (ISE), to write, debug and test our PowerShell scripts in one place. This is purely for ease of use, you may wish to use notepad or the editor of your choice and the results will be the same. You can find the ISE by searching for Powershell ISE. On both Linux and Windows systems, I have moved away from using the cursor to find applications. I simply hit Start and search.

The ISE will have 2 panes. The top pane is an editor for writing scripts, and the bottom pane is simply a command shell. You can type commands directly into that pane in the same way that you would use a command line. Try the “get-help” command in this pane to see it in action.

PowerShell was designed for automating tasks in the Windows environment. Any windows server machine, such as one that you access through: https://portal.azure.com/ will work for this activity. If you are running Windows natively then you can choose to use that, alternatively, you can load up a Windows Server image and the RDP in. After this, start by opening Windows Powershell ISE. Remember to right-click and "Run as Administrator".

Our very first PS script is a one liner. Using the write-host command create a script to write “Hello World” to the console. If you are unsure, you can first try “get-help write-host” in the command prompt pane. Now let’s move onto using a variable in this script. We can create a variable using the below syntax:

    $myVariable=”ISEA” 

Now try and display this variable in the same way that you displayed the “Hello World” text. Ask your tutor if you get stuck. It is likely that running scripts may be disabled on your system. See if you can work out how to enable the execution of powershell scripts. http://www.faqforge.com/windows/windows-powershell-running-scripts-is-disabled-on-this-system/

You should have an ISE window like this, if not then remember to click the script arrow near the top right.
You should have an ISE window like this, if not then remember to click the script arrow near the top right.
You may be able to add:

    write-host $myVariable

There are many more commands that we can use. If we want to see a big list we can invoke the:

    get-command

operation on the command prompt in the bottom pane. You may then get individual help on specific commands.

As you’ll see many of these have aliases that are identical to Linux, try things like rm, cp, mv, ps or kill

Powershell Basic Backup[edit]
Before we get started let's install the iis webserver. Click this link to see the instructions.

Now we will play with the following script. Make sure you change the username component then save it as unknown_script.ps1 and then execute it. What do you think it is doing?
```
$source = "C:\inetpub\wwwroot\"
$destination = "C:\Users\User\Documents\"
Copy-item $source $destination -Recurse
```

If you get an error message about the server execution policy then you can rectify this by typing the following into the command line:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Take a look at the contents of
```
 C:\Users\User\Documents
```

### Inserting dates and zipping ###

The following is a pretty good starting point. Lets just get PowerShell to dynamically insert a date and time and then we can schedule the backup. Run the following code snippet independently. I created in the Powershell editor and saved it as powershell_backup_script.ps1 and then executed it from the powershell command line by typing its name. Make sure that the username, in this case Administrator, is correct.
```
 $source = "C:\inetpub\wwwroot\"
 $destination = "C:\Users\Administrator\Date_Backup.zip"

 If(Test-path $destination) {Remove-item $destination}

 Add-Type -assembly "system.io.compression.filesystem"

 [io.compression.zipfile]::CreateFromDirectory($Source, $destination)
```

Try running the snippet below. Make sure you understand what it is doing before moving on.

#### Naming a file dynamically with the date ####
```
$a = Get-Date
echo $a

echo "this is a string"

$a = $(get-date -f yyyy-MM-dd)
echo $a
```

Hack the two code snippets together to create a powershell script that will create a zip file of a directory and copy this to another directory. Hint: When assigning values to a variable you can join strings and variables together using the "+" operator.

### Schedule the task ###
Use the example commands below to schedule task to run every 10 minutes. The command-line tool to do this is schtasks. Try it out on the command line:

    schtasks

The following command schedules, example.ps1, to run every 10 minutes. The command uses the /sc parameter to specify a minute schedule and the /mo parameter to specify an interval of 10 minutes. /tn is the name of the task and /tr is the task that will run.

    schtasks /create /sc minute /mo 10 /tn "Backup Script" /tr "powershell.exe -file C:\Users\Administrator\example.ps1"

Schedule your backup task to run and monitor the file creation time in the directory to verify it is periodically writing a new backup.

The following command shows you all the processes that are scheduled to run.

    schtasks

In Linux we have often used grep. You have probably entered the following command on a linux system many times.

    ps -e | grep searchterm

Windows is the same. Below we are just replacing grep with findstr

    schtasks | findstr Backup

#### Listing and Killing a process

Open notepad from the command line.

We can get a list of processes using the “Get-Process” command. This simply displays a list of all processes running. Since the output might be a bit hard to follow, we will sort it using the “Sort-Object ID” command. Use the pipe symbol for separation “|”.

Get-Process | Sort-Object ID
That one liner will give us a list of all processes, sorted by process ID. But that’s still not helping us to find a specific process in the list. The “findstr” command is similar to “grep” from Linux.

Can you build up on the command to only list processes that have the name “notepad”?

Hint: There are two different ways that you can accomplish this task.

Remember that if you need to kill a process you can use the following. List the programs that are running on your Windows System:

tasklist
Kill this process from the command line. You can do this with the name or the Process ID (PID). The /f is for "force"

taskkill /im process.ps1 /f 
OR

taskkill /pid 1234 /f
Powershell Loops[edit]
As you can see from the big list of commands (“get-commands”), PowerShell supports "for" and "while" loops as well as conditional statements. We will try out a basic for loop below. Instead of hardcoding the parameters for the loop, we based it on the size of an array, so if the array was bigger, then we would have more iterations of the loop.

$array = 1..5
$count = $array.Count
For( $i=0; $i -lt $count; $i++ )
{
  write-host “Testing”
  Start-Sleep -s 1
}
write-host “Success"
Hint: The code above will work if you copy and paste it as a block. You may have trouble if you type it line by line. The problem is when you press <Enter> Powershell tries to execute just that line and commands like the FOR loop don't make sense if you split up the components. If you are typing this into powershell, use <Shift><Enter> at the end of each line and this will insert a <Line Feed> that does not start execution. After typing the last statement you should press <Enter> to execute it.

Extra-task: Modify the script so that it will loop 10 times

Extra-task: Change the line that says testing, such that the program counts every iteration

Final Example: Take a break[edit]
In this example, we’ll use the code snippet below to display a message every 30 minutes asking you to take a break. We’ll do this by using the task scheduling feature in Windows.

$a = new-object -comobject wscript.shell
$b = $a.popup(“You should take a break and get a glass of water”, 1)
Modify the code so that the popup will remain for 10 seconds.

Once you have modified the code, save it to a known location. In the examples that follow we saved the file to the folder C:\Users\user because that was our home directory. You should substitute your own directory as you apply commands.

The following schtasks command should schedule your desired task every minute. You may wish to do this for testing purposes.

schtasks /create /sc minute /mo 1 /tn "Pop Up" /tr "powershell.exe -file C:\Users\Administrator\popup.ps1"
You can list the scheduled tasks with

schtasks /query
You can refine the list of scheduled tasks with

schtasks /query | findstr Pop
You can disable a scheduled task with:

Disable-ScheduledTask -TaskName "Pop Up"
Shutting down & Saving Power[edit]
Public access computers or computers where we know that people will not be using them after a certain hour. We can shut them down.

Explore the shutdown command options by typing the following in the powershell window:

shutdown
Shutdown /r would restart your computer but shutdown /s will completely shut it down

If you are using a windows machine sitting in front of your, then see if you can use schtasks to hibernate your computer:

shutdown /h
On you cloud-based server machine, see if you can shut it down just a few minutes into the future. You can then watch this happen. Try something like:

shutdown /s
Obviously, this might be useful to shutdown all library, department computers to save power after 6:00 pm.


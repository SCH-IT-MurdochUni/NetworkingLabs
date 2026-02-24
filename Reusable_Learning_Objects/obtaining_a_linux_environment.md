```
  ___  _     _        _       _                       _     _                  
 / _ \| |__ | |_ __ _(_)_ __ (_)_ __   __ _    __ _  | |   (_)_ __  _   ___  __
| | | | '_ \| __/ _` | | '_ \| | '_ \ / _` |  / _` | | |   | | '_ \| | | \ \/ /
| |_| | |_) | || (_| | | | | | | | | | (_| | | (_| | | |___| | | | | |_| |>  < 
 \___/|_.__/ \__\__,_|_|_| |_|_|_| |_|\__, |  \__,_| |_____|_|_| |_|\__,_/_/\_\
                                      |___/                                    
 _____            _                                      _   
| ____|_ ____   _(_)_ __ ___  _ __  _ __ ___   ___ _ __ | |_ 
|  _| | '_ \ \ / / | '__/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
| |___| | | \ V /| | | | (_) | | | | | | | | |  __/ | | | |_ 
|_____|_| |_|\_/ |_|_|  \___/|_| |_|_| |_| |_|\___|_| |_|\__|
```

This lab is designed to get you up and running in a Linux environment as quickly as possible. In this week the goal is to get the Linux environment on your Windows or OSX operating system running on the computer sitting in front of you. Internal South St students are encouraged to do this in the labs, and then go home and re-do the task on their own computer. Online students, as well as Singapore and Dubai-based students, will complete this on their own computers in class.

Note for completing in the South St labs: You will need to log into the Windows environment. You can log into the lab PCs using your Murdoch University username and password credentials. Once logged in, make sure you wait for scripts that copying Virtual Machines to finish. <del>And then start Windows in VMware. The credentials, username and password for Windows running in a virtual machine are:</del>
* <del>''username: murdoch''</del>
* <del>''password: student''</del>

<del>Once running Windows in VMware, you will have sufficient privileges to install Virtual box within that system to complete this lab.</del>

The strikethrough content might reflect the day to day experience of your IT life. The original idea of this lab is to use VMware to simulate your Windows laptop and you will install VirtualBox in it then create and install an Ubuntu 24.04 virtual machine. Such approach of running VM in another VM is called nested virtualization. 

The world is evolving, we upgraded to Windows 11 in 2026 S1. Unfortunately, Windows 11 introduced a new security feature called Virtualization Based Security (VBS) with UEFI lock, which might break this nested virtualization in Windows and it is validated by our test before running this unit. 

To proceed in South St labs, please just use the installed VirtualBox on the computer. And feel free to download and install VirtualBox on your own computer. 

## Virtualisation 

Virtual box offers a virtualised environment to run an operating system. The images to the right show Ubuntu Linux running in a Windows environment. Below that you can see Windows running in a Linux environment. We can virtualise any operating system within another and this is a very powerful tool that should become clearer as we progress through the unit. VirtualBox is just one of many approaches to doing this. If you are interested in trying something different outside of class time, feel free to have a read and try to understand the difference between:

*  Hyper-V for Windows
*  Virtual Box
*  VMware
*  Parallels for MAC
*  KVM on Linux

You can download VirtualBox at the link below, but if you are in the South St labs, running windows, this will already be done: 

*  https://www.virtualbox.org/wiki/Downloads

Note that if you are in the South St labs, you should speak with your tutor about how to access the Internet for your operating system.

If you are working on your own computer, and you already have a Virtualisation tool such as VMware or Parallels, feel free to use that but understand that you will need to translate the Virtual box instructions below to your own software. Also if you have completed this exercise in the labs and would like to try something else on your home PC, feel free to do this. Experimenting is a great way to learn.

After you have installed Virtual box, you should download the Ubuntu Linux image. Although pre-installed Ubuntu Virtualbox images exist, and this would be the most expedient approach, we will download a .iso file. These types of files are used to install an operating system from scratch and were historically burned onto a cd. Download from a local mirror: 

We will now use the .iso image file, that you Download below in Virtual box.

### Beginner

This is a lightweight variant of Ubuntu linux that should be low on storage memory for your system.

* Official Website: https://lubuntu.me/downloads/
* The actual download page would be: https://cdimage.ubuntu.com/lubuntu/releases/noble/release/

If you have a powerful computer with more than 8GB of RAM, then you can try a regular ubunt image: 

* https://ubuntu.com/download/desktop

If you are still unsure, consult with your tutor about which image to download.

## Start Virtualbox

If you are working from home, download and install virtualbox: https://www.virtualbox.org/wiki/Downloads. After it is installed, start Virtualbox, then:

```
 *Start VirtualBox
 *Create a new virtual machine
 *Type the name, put the downloaded iso file into iso selection and uncheck unattended install
 *Choose 4096 MB or 8192MB Memory if you have enough to spare'' 
 *Choose 2 core or 4 core if you have enough to spare'' 
 *Follow the defaults as shown''
 *Follow the defaults as shown''
 *Follow the defaults as shown''
 *Click start to start the virtual machine'' 
 *Virtual Box will tell you that you are starting a machine with no boot media. You need to point Virtualbox towards your Ubuntu .iso file so that it can boot from this'' 
```

Note that what we are doing here is mapping the iso as a virtual cd drive. After doing this, the Ubuntu machine should start booting. Eventually, you should be able to click Install Ubuntu.

#### Work through the installation of your Ubuntu Linux install

Yes, we are throwing you in at the deep end here!  If you get stuck please make use of the forums, your tutor and your peers. That's what they are there for! Working through the problems and seeking assistance will get you there. Along the way, you'll be learning applied skills and a problem-solving approach that is essential for all IT professionals.

When your machine has finished installing you may need to manually reboot it. Go to Machine->Reset

Next week you will start to learn the Linux command line and get a bit more proficient in operating it. Internal students who have only completed this in the labs are encouraged to have a go on their home machine. Don't leave your lab yet, however.

#### Read and learn about different Linux Distros 

Spend some time reading about what we mean by the word distro. Read and think about the different Linux distros and their use. Feel free to have a read here: https://www.howtogeek.com/191207/10-of-the-most-popular-linux-distributions-compared/ 

You can also checkout the distro ranking by DistroWatch.com: https://distrowatch.com/dwres.php?resource=popularity 

Consider whether you would like to try something different at home. If you have time in the labs, this is the perfect time to try downloading a different distro and playing with it in Virtualbox.

Some of your local mirrors will distribute many different Linux Operating Systems.

* Perth: https://mirror.aarnet.edu.au/pub/
* Dubai: https://mirror.maeen.sa/
* Singapore: http://download.nus.edu.sg/mirror/

## External and Dubai/Singapore Students 

In future weeks labs might refer to getting your lab partner to test or try to do something on your Linux machine. For you, you will be your partner. In all these cases, where we might say "get your lab partner to test your webpage" OR "get your partner to login via ssh into your Linux machine, you will need to do this from your native operating system (most likely this is Windows or MacOS). 

To perform these tasks, we want your Linux Virtual machine's network interface to be accessible from your Windows or MacOS machine. Set the network adapter to bridged and select your network adapter which connects to the Internet. Please seek assistance from your tutor with this.

<!-- [[File:bridged.png|center|frame|x400px|alt#This is where you can change the network adapter to bridged so that you have bi-directional network access between the Ubuntu Virtual Machine and your Windows or OSX OS - Note that this can be problematic on some work networks such as eduroam| This is where you can change the network adapter to bridged so that you have bi-directional network access between the Ubuntu Virtual Machine and your Windows or OSX OS - Note that this can be problematic on some work networks such as eduroam]] -->

![Bridged example](../IMGs/Bridged.png?raw=true "Bridged Interface") <p style="text-align:center; font-style:italic;">This is where you can change the network adapter to bridged so that you have bi-directional network access between the Ubuntu Virtual Machine and your Windows or OSX OS - Note that this can be problematic on some work networks such as eduroam</p>

### Troubleshooting at home 

#### Apple M-chip 

If you have an Apple M-chip based computer, then great, these processors are amazing, but they do not run on x86_64 instruction sets that traditional Intel and AMD based processors would run. Instead they run a bespoke architecture based on the ARM instruction set. The ARM instruction set is currently used in mobile platforms, like phones and tablets but is also making its way into the server market. 

To get virtualisation setup on your Apple M-chips, a past ICT171 has generously produced this content to help M-chip Mac users: https://echo360.net.au/media/7ab80f6f-b405-431d-bcec-a9f60a88eba7/public 

You are using a different, but free virualisation tool on the Mac, and will be installing the ARM based version of Ubuntu. As with all these detours, working through these things is the learning so please don't view it as a barrier to your learning.

### VTx and VTd

If you experience errors stating that "VT-x" or "VT-d" is not available, you may need to turn on virtualisation in your bios. Every computer manufacturer has a different method to access the bios; you may need to google “HP how to turn on virtualisation bios” or “Dell how to turn on virtualisation bios”. 

For Apple or OSX this should already be enabled. Note that if you have very new MAC, with an M-chip processor, then you may need to chat with your tutor and unit coordinator. The new apples do not use x86_64 chips and thus, the way to do virtualisation is currently a moving target.

If you get stuck on this step or do not feel confident, then ask your tutor. Also, do lots of reading until you are confident that you know what you are doing. See the link below:

* https://forums.virtualbox.org/viewtopic.php?t=87752

## Extra ##

If you would like your guest VM to be able to resize the screen you may want to try installing the following extensions you will need to execute these in a terminal session.

    sudo apt install virtualbox-guest-utils 

If your virtual machine also has a GUI you should also do the following command. Do not use the following command if you are using a cli only machine. 

    sudo apt install virtualbox-guest-x11

You will need to reboot after you do this. If you are using VMware, then these steps tend to happen automatically.

## Free time ##

Remember that VirtualBox is just one of many approaches to doing this. If you are interested in trying something different outside of class time, feel free to have a read and try to understand the difference between:

* Hyper-V for Windows
* Virtual Box
* VMware
* Parallels for MAC

If you don't like VirtualBox, feel free to research about and try one of the others. In this unit, we want to teach you ways of working with servers, but ultimately leave the tool choice up to you. This is why when we come to Cloud Computing, you will use both Amazon EC2 as well as Microsoft Azure.

If you find yourself with more free time and you feel like you are pretty advanced, then please work through for your system.

## I can't get the lab to work but still need a Linux Environment ##

If you cannot get a virtual machine to run in Linux today then these are your options. Pick based on the operating system that you are using:

#### Mac ####

Click on the search tool in your mac and search for the terminal. It will look like:

<div style="text-align: center;">

![terminal in macos](../IMGs/Get_mac_terminal.png?raw=true "Terminal in MacOS") <p style="text-align:center; font-style:italic;">Terminal in MacOS</p>

</div>

#### Windows ####

Go here: https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab#pivot:overviewtab and "Get" Ubuntu from the Microsoft store. See "Get and Launch Ubuntu" below.

After this, you should go to the windows start bar and type ubuntu and try to open Ubuntu. 

If you get an error like:

 "The WSL Optional Component is not Enabled. Please Enable it and try again"

Then you need to follow the following steps to install WSL. See "Run Powershell as Admin" below to guide you.

* Click on the Windows start bar and type "Powershell".
* Right-click on the PowerShell icon and "Run as Administrator" 
* Type the following in the PowerShell window: 
 Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Now you should be able to go back and click on the start bar and open Ubuntu. When you are successful, you will be asked to create a user account. See "Windows running Ubuntu" below.

![wsl ubuntu](../IMGs/Get_and_launch_ubuntu.png?raw=true "Get and Launch Ubuntu") <p style="text-align:center; font-style:italic;">Get and Launch Ubuntu</p>



## The network doesn't work in my VM at school or Work ##

A lot of school and work networks will not allow you to use the bridged network mode for your VM. The reason is that it will look odd for your authenticated WiFi network session to be requesting two IP addresses. The solution is to hide your Virtual Machine behind your host operating system by using NAT. You will need to use NAT with whatever network adapter your connection is going through. Most likely this is your WiFi network adapter.


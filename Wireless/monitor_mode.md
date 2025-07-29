```
 __  __             _ _               __  __           _      
|  \/  | ___  _ __ (_) |_ ___  _ __  |  \/  | ___   __| | ___ 
| |\/| |/ _ \| '_ \| | __/ _ \| '__| | |\/| |/ _ \ / _` |/ _ \
| |  | | (_) | | | | | || (_) | |    | |  | | (_) | (_| |  __/
|_|  |_|\___/|_| |_|_|\__\___/|_|    |_|  |_|\___/ \__,_|\___|

```

These instructions assume that you are using Ubuntu Linux. You MUST turn off the wifi adapter in the graphical user interface in the top right of the screen in Ubuntu.

![Alt text](../IMGs/Turn_off_WiFi.png?raw=true "Basic Lab Setup") <p style="text-align:center; font-style:italic;">Basic Lab Setup</p>

Usually you would do this as the first thing in the labs, but I have seen cases where there are permission denied errors unless this is done after this command sudo iwconfig wlan0 mode monitor

## Connect the adapted and establish a baseline

First, we must connect the USB directly to our Linux Virtual Machine. Click VM at the top of your virtual machines. You will click:

    VM->Removeable Devices->Realtek 802.11n NIC->connect

Issue a:

    sudo ifconfig -a

If you are on Ubuntu, you will get a wlx98oeu8eoh like adapter name If you are on Kali should now see a wlan0 interface.

## Install aircrack-ng

    sudo apt install aircrack-ng

## Put the WiFi adapter in Monitor Mode

You must strictly follow the instructions below to get a reliable monitor mode. Do this one line at a time. Note that if you are on Ubuntu, you must substitute wlx93048324, or whatever your adaptor name is, into the part that says wlan0 below.

    sudo ifconfig wlan0 down                         # Make sure the interface is down 
    sudo iwconfig wlan0 mode monitor               # put it in monitor mode
    sudo rfkill unblock all                        # Make sure there are no hardware bocks
    sudo iwconfig wlan0 channel 1                  #Make sure you change the channel number to match the AP
    sudo ifconfig wlan0 up                         # Bring the interface back up

Now you should be able to capture on your wireless interface in monitor mode.


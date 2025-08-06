```
__        ___          _               
\ \      / (_)_ __ ___| | ___  ___ ___ 
 \ \ /\ / /| | '__/ _ \ |/ _ \/ __/ __|
  \ V  V / | | | |  __/ |  __/\__ \__ \
   \_/\_/  |_|_|  \___|_|\___||___/___/
                                       
 ____       _     _       _             
| __ ) _ __(_) __| | __ _(_)_ __   __ _ 
|  _ \| '__| |/ _` |/ _` | | '_ \ / _` |
| |_) | |  | | (_| | (_| | | | | | (_| |
|____/|_|  |_|\__,_|\__, |_|_| |_|\__, |
                    |___/         |___/ 
```


This week we investigate bridging with wireless 802.11 networks. The purpose of bridging is often to connect two different LAN segments that are unable to be connected using regular wired networking. There are a number of different ways that this can be achieved. The routers we use contain lots of helpful information which can explain the difference between the modes. Use this to aid your understanding of what you are doing (Wireless Tab → help)

As usual, when following labs, you should turn the transmission power down to 10dB, choose a unique SSID and change the default channel.


## Basic lab setup

In this method of bridging the left most AP operates as a standard AP and the other rightmost AP is used in client bridged mode (Wireless->Basic-Settings->Wireless-Mode. Switch the mode from AP mode to Client Bridge. In this mode, the client bridge will act like a regular WiFi station and connect to the AP. As the devices we are using actually bridge the WiFi Chip and the LAN switch into one logical device, the PC shown on the right-hand side should be able to obtain an IP from the DHCP server running on the AP mode device.

Start by changing the IP address of the bridge that is going to be put into client mode. We cannot have two devices with the same IP so change it to 192.168.1.2. Be mindful that when you save and apply these IP address changes you will need to point your browser to the new IP address. So you now need to point your browser to 192.168.1.2.

You can modify the APs wireless modes by clicking on the wireless tab. Make sure that both of your SSID's/channels on the devices have been changed to the same value. Verify that the two APs are associated by clicking status->sys-info. If the APs are not showing as associated to one another, troubleshoot. The client bridged mode AP will now have its DHCP server switched off. Confirm this at status->sys-info. This device should still forward DHCP messages.

## Client Bridge Mode

On both wired PC's do start->run and type cmd into the box that appears. Acquire new DHCP IP addresses by typing ipconfig /release then ipconfig /renew. Make sure that each PC acquires a new address and that every host can ping each other.

Bridge Performance
So now I would like you to test and try to increase the performance of your bridge. To test you should make one of the PCs in the above topology a Ubuntu Linux machine. Make sure the Ubuntu Linux machine gets an IP address on the 192.168.1.0/24 network. Then

	sudo apt update
	sudo apt install apache2

Now we are going to create a file of arbitrary size and put it in: /var/www/html/

You can create a file of a given size using:

	dd if=/dev/zero of=output.dat  bs=1M  count=1000

Then copy it

	sudo cp output.dat /var/www/html/

What is special about this directory? Why did we need sudo to copy it?

Now on you wired Windows PC on the other side of the bridge, you should open a web browser and type in 192.168.1.x/output.dat (Where x is the IP of the Ubuntu Linux machine).

What was the transmission speed. Can you change the Band, channel, channel width, or mode to increase the speed. You should try to picture the scenario where you are implementing this network for a client and would like to demonstrate that you have made all the changes and done all of the tests required to maximise the performance.

## WDS (Wireless Distribution System) Bridging

Try to setup WDS bridging between the two APs. You can work out how to do this by reading the help pages in the router. Verify that your solution is working by pinging between the two hosts. Also make sure you only have one DHCP server active and that both PC's can obtain IP's from this one DCHP server.

How does WDS differ from other methods of bridging?

### Challenge 1: WDS Bridging with multiple APs

Groups of students can work together to create a large WDS bridged network. Remembering that WDS operates at layer two there are two ways that this lab can be configured.

You can have one main node that serves as the root of the network. This will create a hub and spoke topology. The root node should have the MAC information of all other WDS bridges in the area. The other bridges should only include the MAC information of the root node.
The second way that the lab can be configured is that each WDS AP can include the MAC information of all the other nodes in the network. This will create a full mesh. Remember that we are dealing with a layer two technology so you must ensure that STP (Spanning Tree Protocol) is turned on to prevent the formation of L2 loops.
Whichever method you choose you must ensure that each AP has a different IP address within the same subnet. Furthermore, you must also remember to have only one DHCP server. Set the other APs to DHCP forwarding mode.

Before finishing the lab, connect a wired PC to each WDS AP. Show that it can obtain a IP address dynamically and also that it can ping all other wired PCs in the network.

## Challenge 2: Capturing WDS Frames

Capture some WDS frames using monitor mode. To get a client device in monitor mode, make sure you follow the instructions for the Alpha_USB_in_monitor_mode

What do they look like?


















In this lab, you will configure two different sophisticated pieces of Customer Premises Equipment (CPE). Many home users and very small offices might use a broadband router like the Linksys WiFi Router as the only device in their network. This works for small homes and offices, but frequently the location where the wired broadband connection enters a building might be the worst possible location for a WiFi Access point. Please spend 10 minutes carefully reading the [semi scientific guide to WiFi access point placement](https://arstechnica.com/gadgets/2020/02/the-ars-technica-semi-scientific-guide-to-wi-fi-access-point-placement/). This Arstechnica article has a lot of rules, you should read it in full, but to summarise; the placement of a WiFi Access point, should be relatively high, so that it is above most of the obstructions and is central in a house or office.

Hopefully you can appreciate that you don't want the placement of your Access Point (AP) to be dictated by wherever your broadband connection enters the house. 

We will use the Mikrotik as a Router and the Linksys as an Access Point (AP). This lab will hopefully:

* Force you to think about the optimal placement of WiFi access points
* Familiarise you with the data centre and cabling
* Make you consider the feature sets of Access Points and Routers
* Expose you to Power over Ethernet
* Expose you to PPPoE authentication
* Use SSH public/private keys
* Configure encryption and authentication on your WiFi AP

PPPoE is the authentication method most commonly used to securely authenticate customers with their ISP. You will need to work in at least groups of two to complete this activity. Using the Mikrotik hEX PoE, port 1 will be used as the WAN interface, while ports 2-5 will be the LAN interfaces. The Linksys has an Internet port, with the ports numbered 1-4 being used for the LAN.

## Cabling to the ISP/CCR 

You should connect a cable between your device and the Mikrotik Cloud Core Switch located in the data centre. For the purposes of this lab, the cloud core router will be the ISP and is running a PPPoE server. Use the table below to ensure that you use a unique username and password to authenticate to the Cloud Core Router.

![Alt text](../IMGs/Desk_ports.png?raw=true "Desk Ports") <p style="text-align:center; font-style:italic;">Desk Ports</p>

Review the diagram to the right about the desk ports available and talk to your lab instructor who will talk you through the best way to connect to the data centre.

The Cloud Core Switch is shown below, pay attention to the port numbers that you wire up in the data centre. Use the port number in the patch panel in the data centre that you connect to determine the username and password that you use in the table below. This workflow should prevent two groups from using the same PPPoE credentials.

![Alt text](../IMGs/Wiring_desk.png?raw=true "Desk Ports") <p style="text-align:center; font-style:italic;">Desk Ports</p>



| Pod # | Username | Password | Data Centre Port No |
|-------|----------|----------|---------------------|
| A     | alpha    | alpha    | 17                  |
| B     | beta     | beta     | 18                  |
| C     | charlie  | charlie  | 19                  |
| D     | delta    | delta    | 20                  |
| E     | echo     | echo     | 21                  |
| F     | foxtrot  | foxtrot  | 22                  |
| G     | golf     | golf     | 23                  |
| H     | hotel    | hotel    | 24                  |


## Configuration of the hEX PoE Router for PPPoE ##

Note that the Mikrotik CCS, has PoE. As there is a copper cable connecting the Mikrotik CCS to the Mikrotik HeX PoE on your desk, cabling the router correctly between the data centre and port the WAN/PoE port on your HeX PoE should turn it on.

Once you have turned it on, plug a cable into one of the LAN ports and connect to the default webpage at 192.168.88.1 using a web browser. The default username is admin with no password, please keep it this way for lab purposes. 

If you can't access the device at this IP address or the default username and password do not work then reset configuration:
* unplug the device from power
* press and hold the button right after applying power, hold the button for 5 seconds (USER LED will start flashing)
* release the button to clear configuration.

Configure PPPoE with the username and password, listed in the table using the simple QuickSet page. Ensure that DHCP Server and NAT check boxes have ticks. Your router should authenticate with the PPPoE server and from your PC you should be able to ping the WAN interface of your Mikrotik ping 100.64.0.x (Where x will be your IP address provided by the Mikrotik CCS). '''Note that if you are pinging from your computer, it may have two active Ethernet Connections, you may need to physically unplug from the Murdoch network to ping addresses in the 100.64.0.x range'''

Examine the status of your PPPoE connection by clicking WebFig->Interfaces. Then click on the interface that says pppoe-out1.

Before moving on spend 5 minutes to have a good look at the features provided. Note the amount of advanced functionality provided.

Does the Mikrotik support:
* BGP
* MPLS
* VPNs
* What else can you see?

## Configuration of the Linksys Router for PPPoE 

After you have successfully configured the hEX PoE, temporarily disconnect the hEX Poe device from our PPPoE network and move onto the Linksys. Start by plugging your PC into the LAN port of the Linksys and connect to the configuration page at 192.168.1.1. If you can't login, then reset by holding down the reset button for at least 10 seconds. If you were able to login, then manually reset the settings at Administration->Factory-defaults. Configure PPPoE with your username and password. This is found under Setup->Basic Setup->WAN Setup.

Reflect on the differences between the Mikrotik and the Linksys. Spend 5 minutes to have a good look at the features provided.

## Configuration of a Mikrotik/Linksys CPE scenario 

In the following scenario, you have decided that you would like the stability and rich feature set of the Mikrotik, but the wireless capability of the Linksys. You are going to reconfigure the Linksys as an access point only and use the routing/NAT/QoS/Security features of the Mikrotik. In addition to simply desiring the best features of these devices, in many cases, the location of the ADSL, DOCSIS, GPON broadband into the building is not the ideal location to situate the AP. Many APs may be wall or ceiling mounted to improve the RF coverage of the AP so often there are many reasons why small businesses or homes may separate the PPPoE, NAT, Firewall and routing functions of the router from the wireless capabilities of the AP.

Start by logging into your Linksys device at 192.168.1.1. Please keep the username as root and the password as admin. 

Under Setup->Basic Setup, you should change the WAN Connection type to Disabled. Change the Router IP address, under the Network Setup header to 192.168.88.2, the gateway should be 192.168.88.1. You should also disable the DHCP server. Then save and apply.

Then, run a cable between the LAN port on the microtik and into a LAN port on the Linksys. Switch you Wired connection on your Desktop PC on and off again to get a new IP address. You should find that you now have an IP address in the 192.168.88.0/24 subnet. You should be able to login to both the Mikrotik at 192.168.88.1 and the Linksys at 192.168.88.2.

### Setup the Linksys/DD-WRT AP (SSID, TX Power, Channels) 

Before attempting to connect to your AP, you should change the APs SSID. The SSID (Service Set Identifier) is basically a wireless network name. As all of the APs in the room should have the default SSID of dd-wrt, you should change your SSID to ensure that your wireless client actually connects to your own AP, and not your neighbours. To change the SSID click on the wireless tab, change the SSID, save and then apply the changes.

The second thing we will do before connecting our wireless client is to turn the transmission power down to a lower level. The reason we want to turn down the power levels of our APs in the lab environment is to avoid interference with other groups. We suggest turning the power down to 5 mW. Located under Wireless->Advanced Settings->TXpower to reduce interference with other groups and Murdoch's eduroam.

For those concerned about WiFi radiation and lab safety,  there is little to no danger in this unit. The equipment uses frequencies in the public or unlicensed portion of the wireless spectrum. One of the reasons these frequencies were picked by the FCC was because they pose the least risk to public health. While no long-term studies can conclusively dismiss that wireless radiation causes harm, we conclude that there is little or no risk in this unit because the levels of power being used, even before we lower the power to 5 mW, is a fraction of the 1 Watt used by most mobile phones.

Another measure we will take to avoid interfering with neighbouring groups is to change the channel from the default. Change the channel/frequency by clicking the wireless tab and change the wireless channel.

Connect to from your wireless computer by clicking network connections in the bottom right corner and selecting your SSID. On the wired machine that is browsing the dd-wrt configuration page click Status->sys-info and confirm that your wireless client is connected. Work out the IP addresses of the wireless PC and the wired PC. Confirm that they can both ping each other. To do this, click start->run. Type cmd in the box that opens. Then type ping [ip address] [enter]. When both PCs can ping each other.

### Security 

There are numerous security solutions for wireless LANs, this week we will configure the legacy WEP (Wired Equivalent Privacy) and then the newer and more secure, WPA (WiFi Protected Access).

#### WEP 

To configure a WEP key on the AP click Wireless->Wireless Security. Set the combo box to WEP. These keys can be configured as a pass-phrase which will be converted to HEX keys or, you can just enter a HEX key. Use 64 bit WEP and enter a 10 digit hex key. Save and then apply. 

Your wireless client should now be disconnected. You will need to enter the WEP key on your wireless client to connect. You should now be connected using WEP. Confirm this by pinging the wired host. If you are not connected, troubleshoot.

#### WPA 

We will now configure WPA encryption on our wireless system. On the AP, click Wireless->Wireless Security. Set the combo box to WPA2 Personal and select TKIP+AES. Enter a passphrase. In this case, you can use any ascii characters, save and apply.

You may now be disconnected. Ensure that you type in your new WPA passphrase and click ok. You should now be connected using WPA. Confirm this by pinging the wired host.

### Challenge 1: Ping 100.64.0.1 

From your PC, can you ping 100.64.0.1.

### Challenge 2: Connect your phone 

See if you can connect your smartphone to the WiFi network.

### Challenge 3: SSH Keys on the Mikrotik HexPoE 

Run through the following lab [SSH Keys et al](../Reusable_Learning_Objects/ssh_keys.md). When you have finished, see whether you can install your Linux machine's public key on the Mikrotik HexPoE. You should then be able to SSH from your Linux box.

## Challenge 4: Speed tests 

Create a reliable method of high bandwidth download between your two machines. Ask your instructor for help with this if you need it. To perform a speed test on a Windows PC you will need to find a large file and drop it in the shared folder. On Linux, you can create a large file with the following command.

Install a web server on a machine

	sudo apt update
	sudo apt install apache2

Create a file in: /var/www/html/

You can create a file of a given size using:
	
	dd if=/dev/zero of=output.dat  bs=1M  count=100

Download this file from the Linux client by with:

	wget http://ip_address/output.dat

Compare the speed of the HTTP download with the file share. Take some time to discuss and reflect on the performance differences observed when with the changing frequency, operating system and protocol. 

## Restore Factory defaults 

At the end of every lab you should restore factory defaults. To do this:

* On the Linksys: Administration->Factory Defaults->Yes, apply, ok.
* On the Mikrotik: Quick Set->Reset Configuration


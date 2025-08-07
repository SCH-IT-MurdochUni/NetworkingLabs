```
__        _______ ____  
\ \      / / ____|  _ \ 
 \ \ /\ / /|  _| | |_) |
  \ V  V / | |___|  __/ 
   \_/\_/  |_____|_|    
                        
```

Decrypting packets and/or accessing someone’s network without their consent is illegal. The purpose of this lab is not to encourage students to break into vulnerable networks, rather it is hoped that students will:

* Gain an appreciation of the specific technical vulnerabilities in WEP. This should help to make an informed decision about appropriate security measures to implement in your own or your employer’s wireless networks.
* Have sufficient understanding of the tools involved to be able to test your own network's security.

We will be using aircrack-ng. We want to encourage your interest in network and computer security but **DO NOT** use the tools or techniques that you learn in this lab on networks that are not your own. **DO NOT** attempt to use any of the tools on the Murdoch University infrastructure.

## Lab Setup ##

You should start by setting up a network as shown below.

![setup](../IMGs/common_wireless_lab_setup.png "Basic lab setup")

## Configure WEP ##

Our first task is to configure WEP over the wireless network. Please ensure that you keep the username as root and the password as admin. You can use any hex key that you like. Please be aware that using a WEP passphrase will still use the generated hex key for encryption. Ensure that the wireless Windows PC can Ping the Wired PC. Refer to [WEP setion in Broadband_CPE_Scenarios](./broadband_cpe_senarios.md#wep) if you need to: **Additionally, turn off the 5GHz radio and change the network mode on the 2.4 GHz radio to 802.11b/g only. Remember that there are two radios, and you will need to set the 5GHz radio mode to disabled.**

Your Linux based PC will capture as many packets as possible and try to decrypt the key. WEP cracking tools rely on capturing enough data to enable you to launch statistical attacks on the key. So, we will use two tools, airodump for capturing packets and aircrack for launching our statistical attack on the key.

Before you start, try scanning the local LAN using the following command: 
 
	nmcli d wifi

You may wish to record the channel of your target network.

## Putting the wireless interface in monitor mode ##

Follow the instructions here to put the Alpha USB Wifi adapter in monitor mode: [Alpha_USB_in_monitor_mode](./monitor_mode.md)

## Collecting Weak ivs ##

### Using Wireshark ###

Try capturing the encrypted packets in Wireshark. What filters do you need to ensure you have 50000 data packets? Save the pcap on the Desktop.

### Using Aerodump ###

Another alternative is using airodump. Type:

	sudo airodump-ng [interface_name] --ivs -w [filename] --channel [x]

That command will start airodump and save the ivs to the filename you give it.

You should see the frame count increasing and the SSID of the lab test network should be visible. While you wait to capture sufficient packets try setting up another client (if available) to associate with the AP once you have discovered the key.

## Cracking the WEP key ##

50,000 or less should defeat 40 bit encryption. While you are waiting, do some research of your own. Research the technical reasons why WEP failed. 

Once you think you have enough IVS. Press ctrl+c on the keyboard to exit airodump. We are now going to try to crack the key with aircrack. Type:

	sudo aircrack-ng [filename]

Now that you have the key. Capture some transmissions across the WEP network. Use Wireshark to decrypt the frames and then investigate what was transmitted. You will find that most web transactions are encrypted with SSL/TLS, but usually, DNS messages are in cleartext. 

## Questions ##

If a malicious user has cracked a WEP key, what threat does this pose to the network? To help you answer this question, how likely is it that banking/email accounts of the network users will be compromised?
What danger does a compromised WEP key pose to the network infrastructure? Why does an attack from a compromised WEP key pose a greater threat than an attack from the Internet?
How does WPA with TKIP overcome the problems with WEP?

## Challenge ##

Ok, so once you have the key, you should know how someone malicious might use it. Lets decrypt some frames in Wireshark. To do this, we need to capture the traffic in monitor mode. Make sure your network interface is in monitor monde and listening to the correct channel. 

	sudo iwconfig wlan0 channel 1 

Then

	sudo wireshark

and make sure you collect some data frames from your SSID. Now we need to insert the key into wirshark:

![enter the wep key](../IMGs/Enter_the_wepkey.png "Inserting keys in Wireshark")

What you are looking at is Wireshark->Edit->Preferences->Protocols->IEEE 802.11->Decryption keys (Edit)

Plug in the key to decrypt your own data frames. The process is the same for WPA.


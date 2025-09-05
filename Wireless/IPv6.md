```
 ___ ____         __   
|_ _|  _ \__   __/ /_  
 | || |_) \ \ / / '_ \ 
 | ||  __/ \ V /| (_) |
|___|_|     \_/  \___/ 
                         
```

In this lab, we will explore the default behaviour of Mobile broadband with an emphasis on addressing. Before we start looking at the addressing or performance of these networks, let's start with a baseline. Start by deploying the Ubuntu Virtual Machine in the labs. 

![Alt text](../IMGs/Ipv6.png?raw=true "Remember that in IPv6 address shortening, consecutive blocks of zeros can be replaced with :: once per address. Choose the option that correctly represents the shortened form of the given IPv6 addresses.") <p style="text-align:center; font-style:italic;">Remember that in IPv6 address shortening, consecutive blocks of zeros can be replaced with "::" once per address. Choose the option that correctly represents the shortened form of the given IPv6 addresses.</p>

## Basic Network Baselining ##

### Wired LAN ###

Open a terminal an type:

	ip a

What is your IP address? Is it IPv4, or IPv6? Is it private/public? Confirm your IPv6 predictions here:

	https://ipv6test.google.com/

Then go here:

	https://whatismyipaddress.com/

**Write your address on the board under the heading Wired LAN**

Does it correctly resolve your location and IP?

Run a speed test at: 
linux
	https://www.speedtest.net/

What is your upload and download speed? What latency is reported?

Try pinging:

	8.8.8.8

And then:

	2001:4860:4860::8888

This is Google DNS server, they are the IPv4 and IPv6 addresses of the same server. Only ping for less than 20 seconds to prevent the university from being blacklisted. What latency do you get? Does it vary a lot?

What is your DNS server? Try a: 

	cat /etc/resolv.conf

Reflect on the results and compare them with your lab partner.

### Eduroam ###

Start by clicking in the top right in Ubuntu and disabling both ethernet Adaptors. Connect to eduroam through your Wifi adaptor in Linux, then repeat all of the tests above. Is there any difference? Reflect on the results and compare them with your lab partner.

Open a terminal an type:

	ip a

What is your IP address? Is it IPv4, or IPv6? Is it private/public? Confirm your IPv6 predictions here:

	https://ipv6test.google.com/

Then go here:

	https://whatismyipaddress.com/

**Write your address on the board under the heading Eduroam**

Does it correctly resolve your location and IP?

Run a speed test at: 

	https://www.speedtest.net/

What is your upload and download speed? What latency is reported?


Try pinging:

	8.8.8.8

And then:

	2001:4860:4860::8888

This is the Google DNS server, they are the IPv4 and IPv6 addresses of the same server. Only ping for less than 20 seconds to prevent the university from being blacklisted. What latency do you get? Does it vary a lot?

What is your DNS server? Try a: 

	cat /etc/resolv.conf

Reflect on the results and compare them with your lab partner.

### Mobile Broadband ###

Lets start by starting up your personal hotspot on your mobile phone. This should be easy on iOS or Android. Please make sure you use a password. Repeat the steps above and connect to your mobile hotspot. 

Open a terminal and type:

	ip a

If you did not get an IPv6 address and are an android user, try enabling IPv6 here: https://nordvpn.com/blog/ipv6-enable-or-disable/#enable-disable-ipv6-on-android

What is your IP address? Is it IPv4, or IPv6? Is it private/public? Confirm your IPv6 predictions here:

	https://ipv6test.google.com/

Then go here:

	https://whatismyipaddress.com/

**Write your addresses on the board under the heading Mobile Broadband**

Does it correctly resolve your location and IP?

Run a speed test at: 

	https://www.speedtest.net/

What is your upload and download speed? What latency is reported?

Try pinging:

	8.8.8.8

And then:

	2001:4860:4860::8888

This is Google DNS server; they are the IPv4 and IPv6 addresses of the same server. Only ping for less than 20 seconds to prevent the university from being blacklisted. What latency do you get? Does it vary a lot?

What is your DNS server? Try a: 

	cat /etc/resolv.conf

Reflect on the results and compare them with your lab partner.

## IPv6 ##

While still connected to your phone's mobile broadband connection, open a terminal and type:

	sudo wireshark

Capture on your WiFi interface do some casual browsing as you capture traffic. Are you using IPv4, IPv6 or both? How do you think your phone works it out.

### IPv4/IPv6 Dual Stack ###

Right now, you should have an IPv4 and an IPv6 address similar to this diagram to the right. Use wireshark to capture this IPv4 and IPv6 traffic.

Fine one of each of the following 3 messages, read about each one and spend 2 minutes on each digging through the headers in wirshark to work out what is going on. 
* Neighbor Solicitation
* *  Link to read: https://docs.ruckuswireless.com/fastiron/08.0.60/fastiron-08060-l3guide/GUID-4B7AE145-E81A-4826-8A28-9545490C374B.html
* Neighbor Advertisement 
* Router Advertisement 
* *  Link to read: https://docs.ruckuswireless.com/fastiron/08.0.60/fastiron-08060-l3guide/GUID-F0EE47A1-63DF-42A2-98F1-08A5776EB539.html

Look closely at your IPv6 addresses. There should be two that are similar. What is the difference? Do your research on this. Use wireshark to work out which address is the source address in your outgoing communications.

### Link Local Addresses ###

You may be familiar with the idea of a MAC address being a link local address that is only relevant on the LAN. The analogy is not quite correct as MAC addresses work at the data link layer. The closest relative to IPv6 link-local addresses ais the 169.254.0.0/16 subnet. You often see this assigned when you boot up a computer and there is an active network interface but no DHCP server can be found. In IPv6, these link local addresses are always present and are assigned from the block fe80::/10. 

Have a look at your link-local address with an:

	ip a

Can you identify yours? Now I want you to try to identify the link-local address of your phone and ping it. To do this, look at the neighbor solicitation and neighbour advertisement messages. 

You may find that your dns server is your smarthphone.


### Loopbacks ### 

By now you should know that 127.0.0.1 is a special address reserved for self testing nad address is typically used by applications or services that need to communicate with themselves locally. Examples include such as testing client-server interactions or running network services on the same machine they are being accessed from.

Try :

	ping 127.0.0.1

Now try:

	ping ::1

### IPv6 Only ###

In this final section, we will look at the state of the internet through the lens of an IPv6 only connection. Delete your IPv4 address on your Linux box with:

	sudo ip addr del 172.20.10.2/28 dev wlx00c0ca967d99 (Note your IP and dev name will differ)

Now browse the internet and explore what works and what breaks. Capture in Wireshark and have a close look.

### Security ###

One of the promises of IPv6, is the elimination of NATs. This solves a number of networking headaches, but does it really mean that your machine is now directly connected to the Internet, without any of the firewall like protections of NAT.

Start by installing nmap

	sudo apt intstall nmap

Then install apache2

	sudo apt install apache2

Port scan yourself

	nmap ::1

Now trade IPv6 addresess with a friend. Port scan each others IPv6 addresses over the Internet. What did you find? What is going on?


```
  ____                            _   _               _        
 / ___|___  _ __  _ __   ___  ___| |_(_)_ __   __ _  | |_ ___  
| |   / _ \| '_ \| '_ \ / _ \/ __| __| | '_ \ / _` | | __/ _ \ 
| |__| (_) | | | | | | |  __/ (__| |_| | | | | (_| | | || (_) |
 \____\___/|_| |_|_| |_|\___|\___|\__|_|_| |_|\__, |  \__\___/ 
                                              |___/            
 _   _            __  __               _            _     
| |_| |__   ___  |  \/  |_   _ _ __ __| | ___   ___| |__  
| __| '_ \ / _ \ | |\/| | | | | '__/ _` |/ _ \ / __| '_ \ 
| |_| | | |  __/ | |  | | |_| | | | (_| | (_) | (__| | | |
 \__|_| |_|\___| |_|  |_|\__,_|_|  \__,_|\___/ \___|_| |_|
                                                          
__     ______  _   _ 
\ \   / /  _ \| \ | |
 \ \ / /| |_) |  \| |
  \ V / |  __/| |\  |
   \_/  |_|   |_| \_|
                     
```

To connect to the murdoch VPN you will have to be a member enrolled in one of the following units:

'''ICT291, ICT302, ICT369, ICT372, ICT535, ICT611 or added by a staff member.'''

##Setting up Azure multi-factor authentication:##
Before you can start using Murdoch's Cisco AnyConnect VPN service the Azure Multi-factor Authentication(MFA) component for your Murdoch AD account must be configured.

To configure your Azure MFA, go to https://aka.ms/mfasetup and login with your Murdoch staff/student number and password. 


You will be asked to supply more information to keep your account secure - click Next to proceed.

At '''Step 1''' you will be asked to select a default verification method and given the options of Authentication phone, Office phone or '''Mobile app'''.

Please select '''Mobile App''' and then check the '''Receive notifications for verification option'''

The Office phone method is not supported, and the Authentication phone method is not recommended

Proceed by clicking Set up - you will then be prompted to set up the Microsoft Authenticator App on your smart phone



## Install the Microsoft Authenticator App:##

Microsoft Authenticator is required to validate your credentials via your smart phone. To install this app search for Microsoft Authenticator in the App Store or Google Play and click install 

[[File:Ms authenticator app.png|550px]]

The app will prompt you to scan a QR code to complete setup. Using another computer, log in to [[https://aka.ms/mfasetup]] as per the Azure MFA Setup step, and click '''Set up Authenticator app'''

Scan the QR code or enter the 6 digit code and Microsoft Authenticator will complete setup

## Cisco AnyConnect Client Installation:##

Download the '''client installation package''', for your version of operation system.

The v4.8 is the most recent version available with home-use .exe files available in the ITS directory (v4.10 only has the .msi file).

Here's a link for the home-use licensed AnyConnect client v4.8:

https://murdochuniversity.sharepoint.com/:f:/r/sites/DITMS-Tech/StudentSupport/Cisco%20AnyConnect/AnyConnect4.8_Home-Use?csf#1&web#1&e#pCS04p

### Older Versions ###

[https://wwwcoms.murdoch.edu.au/vpn/download/its_packages/CiscoAnyConnect.exe?_ga#2.192395308.705040227.1596089756-1111608910.1595928656/ Cisco AnyConnect Client 4.6.02074 for Windows] Supported for only Windows 7, 8, 8.1, 10 for both x86(32-bit) and x64(64-bit)

[https://wwwcoms.murdoch.edu.au/vpn/download/its_packages/CiscoAnyConnect.pkg?_ga#2.192395308.705040227.1596089756-1111608910.1595928656/ Cisco AnyConnect Client 4.6.02074 for MacOS] Supported for only macOS 10.11, 10.12. 10.13 and 10.14

[https://wwwcoms.murdoch.edu.au/vpn/download/its_packages/CiscoAnyConnect-4.8.02045.pkg?_ga#2.230211226.705040227.1596089756-1111608910.1595928656/ Cisco AnyConnect Client 4.8.02045 for MacOS] Supported for only macOS 10.15. Any users on earlier versions of MacOS should use the previous version 4.6.02074.

[https://wwwcoms.murdoch.edu.au/vpn/download/anyconnect-linux64-4.6.02074-predeploy-k9.tar.gz?_ga#2.230211226.705040227.1596089756-1111608910.1595928656/ Cisco AnyConnect Client 4.6.02074 for Linux Red Hat & Ubuntu] Supported for only Linux Red Hat 6, 7 & Ubuntu 14.04 (LTS), 16.04 (LTS), and 18.04 (LTS)(64 bit only)

For IOS devices please go to the App Store and search for Cisco Anyconnect.

For Android devices please go to the Google Play Store and search for Cisco Anyconnect.

## Connecting to the VPN Service##


### Enter Credentials on your computer###


[[File:Client.jpg|550px]]

click Connect


[[File:ICT.PNG|550px]]

Change your Group to '''Murdoch_Unit_ICT'''

Enter your student number i.e. 31234567@student.murdoch.edu.au and your Murdoch password and press "OK" 


### Authorize on your second factor###

[[File:Approve signin.png|550px]]

You will prompted to enter a verification code, or to approve the signin. This will depending on how you have set the Azure MFA verification option:

'''Notify me through app:''' A prompt on your mobile device will ask you to approve or deny the sign in 

[[File:Mfacode.jpg|550px]]

'''Use verification code from app or token:''' Your app will display a 6 code digit that will need to be entered in to the AnyConnect client 
MFA Code

## Testing##
When you are successfully connected, you should be able to ping 10.51.32.251.

## FAQ##
'''Q: Will I be able to connect to VPN without access to my additional security verification option?'''

Without access to your secondary verification option, VPN access will not be possible.

'''Q: Can I change my additional security verification option?'''

Yes, but this requires access to your existing security verification option. If you no longer have access to this, you will need to contact the IT Service Desk for assistance

'''Q: I previously had access to custom VPN profiles, how do I access these? '''

You will need to contact the IT Service Desk for custom instructions.

'''Q: I have been using an alternate VPN client to connect, will I need to use AnyConnect with MFA? '''

Yes, other client access will stop working when the old VPN servers are retired so AnyConnect will be required.

'''Q: Do I need to install the Microsoft Authenticator App if I elect to receive my verification code by SMS? '''

No, however reliance on SMS/text code can be an issue if you are in an area with poor mobile reception.


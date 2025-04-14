```
 ____  _       _ _        _ 
|  _ \(_) __ _(_) |_ __ _| |
| | | | |/ _` | | __/ _` | |
| |_| | | (_| | | || (_| | |
|____/|_|\__, |_|\__\__,_|_|
         |___/              
  ____          _   _  __ _           _              _         _       
 / ___|___ _ __| |_(_)/ _(_) ___ __ _| |_ ___  ___  | |    ___| |_ ___ 
| |   / _ \ '__| __| | |_| |/ __/ _` | __/ _ \/ __| | |   / _ \ __/ __|
| |__|  __/ |  | |_| |  _| | (_| (_| | ||  __/\__ \ | |__|  __/ |_\__ \
 \____\___|_|   \__|_|_| |_|\___\__,_|\__\___||___/ |_____\___|\__|___/
                                                                       
 _____                             _   
| ____|_ __   ___ _ __ _   _ _ __ | |_ 
|  _| | '_ \ / __| '__| | | | '_ \| __|
| |___| | | | (__| |  | |_| | |_) | |_ 
|_____|_| |_|\___|_|   \__, | .__/ \__|
                       |___/|_|        
```

Much of this information is sourced from: https://letsencrypt.org/getting-started/

## Pre-requisites ##

Before starting to ensure that you have an A record pointing to the IP address of your server. To verify that you have met this prerequisite, you should be able to ssh from your local machine. For example, the following should be successful

	ssh -i pemkey.pem ubuntu@[yourdomain-name-goes-here.com]

I will also assume that you are running the Apache web server and have current access. You could use a web browser or from the CLI you could:

	wget http://[yourdomain-name-goes-here.com]

If these tests fail, go back to the Amazon EC2 server lab and the DNS lab and make sure these tests work before you proceed. Check that the firewall in your Amazon machine has port 22, 80 and 443 open.

## Obtaining your digital certificate from Let's Encrypt ##

You should, for testing purposes have TCP port 22, 80 and 443 available through the firewall. Once you have tested that your website is working over HTTP (port 80), it is time to get a certificate and enable it over HTTPS (port 443). Go to: 

	https://certbot.eff.org/

Select I'm using "Apache" on "Linux (snap)". This will provide you with the instructions that you can follow. Complete all the steps on the command prompt.

To confirm that your site is set up properly, visit your website in your browser and look for the lock icon. Click on the lock icon to see if you can tell who issued the certificate.


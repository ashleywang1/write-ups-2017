# picoCTF 2017 : keyz-20

**Category:** Cryptography
**Points:** 20
**Solves:**
**Description:**

> While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com
>
>
>  HINTS
>
> There are plenty of tutorials out there. This one covers key generation: <https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html>
>
> Then, use the web shell to copy/paste it, and use the appropriate tool to ssh to the server using your key


## Write-up

The hints reference (https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html), and the steps in there are basically exactly what you need to do. Another guide is below:
 
Guide: (https://help.ubuntu.com/community/SSH/OpenSSH/Keys)

My directions:

Prerequisite/Terminology: You are trying to SSH FROM one machine A to machine B. In this example, it's from your computer to the picoctf machine. Let's call machine A, your computer, your client. The picoctf server, B, is your remote host.


1.	Create a .ssh folder with very few permissions (see the guide). This is the **really important part**. If your .ssh file has worldwide READ permissions, then **none of the following will work** because the ssh program will think your keys were stolen.
	a.	```chmod 700 .ssh``` from the very beginning.
	b.	NOT ```chmod 600 .ssh``!!! This will make it impossible to ssh onto that machine!
2.	Generate a keypair on your client
``ssh-keygen -t rsa -b 4096```
This generates a public and private key. The public key file usually ends in .pub and the private keyfile either has no ending or ends in .ppk.
3.	Look at your public keyfile. You should see something like
	> ssh-rsa **<long string of numbers and letters and maybe some slashes>**
4.	In your remote host, add your public key to your authorized_keys file in .ssh folder.
> ```echo "**<your public key text>**" > /.ssh/authorized_keys```
5.	**Don't forget to actually add your private key** n both your client.  Add the private key into your ssh-agent using ```ssh-add```.


SOLUTION:

> ```ssh **<your_username>**@shell2017.picoctf.com```
>Congratulations on setting up SSH key authentication!
>Here is your flag: who_needs_pwords_anyways

## Other write-ups and resources

* none yet

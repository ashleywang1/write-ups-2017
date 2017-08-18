# picoCTF 2017 : internet-kitties-10

**Category:** Misc
**Points:** 10
**Solves:** 
**Description:**

> I was told there was something at IP shell2017.picoctf.com with port 28669. How do I get there? Do I need a ship for the port?
> 
> 
>  HINTS
> 
> Look at using the netcat (nc) command!
> 
> To figure out how to use it, you can run "man nc" or "nc -h" on the shell, or search for it on the interwebz


## Write-up

Netcat is a super useful hacker tool - it was originally used for network analysis. You can use it to open up TCP and UDP connections between two machines over any port. Uses include port forwarding, proxying, simple web server, and leaving an open backdoor for the hacker. [See more complex uses of netcat here](https://null-byte.wonderhowto.com/how-to/hack-like-pro-use-netcat-swiss-army-knife-hacking-tools-0148657/).

SOLUTION: ```nc shell2017.picoctf.com 12275```

RESULT:
>Yay! You made it!
>Take a flag!
>1e1ccf22b278d35b1977c76bb66c5e30

## Other write-ups and resources

* none yet

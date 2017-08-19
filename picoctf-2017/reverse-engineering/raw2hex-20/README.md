# picoCTF 2017 : raw2hex-20

**Category:** Reverse Engineering
**Points:** 20
**Solves:** 
**Description:**

> This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/900be7006255006d8d4e09164dba63c0 and turn that Raw2Hex!
> 
> 
>  HINTS
> 
> Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.


## Write-up

In the directory, we have the (read-protected) flag and an executable **raw2hex** file. Running that file results in:
>The flag is:??~Y?މJ?B>?

Looks like we have to take the output and run it through some conversion process to get the hex values. This is called a **hexdump**. One such tool that does this in linux is the command **xxd**, although you could write a script in python or perl or something too.

Running ```./raw2hex | xxd``` gives us:

>0000000: 5468 6520 666c 6167 2069 733a e519 e7aa  The flag is:....

>0000010: 7e59 3fde 891b d24a aa42 3ea4            ~Y?....J.B>.

The blocks of four on the left are the hex values that we want, and the text on the right is our "raw string" representation of those hex values. We don't want all of the hex values, just the ones that correspond to the flag. Each 'letter' on the right is represented by two 'hex digits' on the left (e.g. 'T' is '54'). So, ignoring the hex values that correspond to the text "The flag is:", we get

>0000000: 5468 6520 666c 6167 2069 733a **e519 e7aa**  The flag is:....

>0000010: **7e59 3fde 891b d24a aa42 3ea4**            ~Y?....J.B>.

Or, running ```./raw2hex | xxd -p```

>54686520666c61672069733a**e519e7aa7e593fde891bd24aaa423ea4**

SOLUTION:
>The flag is:e519e7aa7e593fde891bd24aaa423ea4

## Other write-ups and resources

* none yet

# picoCTF 2017 : hex2raw-20

**Category:** Reverse Engineering
**Points:** 20
**Solves:** 
**Description:**

> This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/9177bfe904b2fb486bf2063954b4b3cb and turn that Hex2Raw!
> 
> 
>  HINTS
> 
> Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.


## Write-up

Going to the problem directory and typing ```ls``` show 3 files: **flag, hex2raw, input**.

Running ```./hex2raw``` returns:
>Give me this in raw form (0x41 -> 'A'):
>1a558acddabd64bbccdd94903eafdf18
>
>You gave me:

Converting this via an [online converter](http://string-functions.com/hex-string.aspx) gives us:
>U??ڽd??ݔ?>??

That's pretty ugly, but let's give it a shot and copy and paste it as an answer anyway. This results in:
>That's not what I wanted...

The hint to this problem isn't particularly useful unless you understand that 'raw' basically means 'raw binary', the type of stuff you see when you open an executable file and see a jumbled mess. We're not looking for 0s and 1s 'binary'. We need to find a tool that converts from binary to hex and back. Note that converting a binary to human-readable hex is called **hexdump**. There's a tool that does that for you, but what we want is the *reverse*.

xxd (https://www.systutorials.com/docs/linux/man/1-xxd/) is one such tool that happens to be on all vim machines. Yay! You could write a python, perl, or C script to do this, but let's make it easy for ourselves and just use xxd. Looking at xxd's manual page sith ```man xxd```, there's one part that's particularly relevant to this problem:

>-r | -revert
>reverse operation: convert (or patch) hexdump into binary. If not writing to stdout, xxd writes into its output file without truncating it. Use the combination -r -p to read plain hexadecimal dumps without line number information and without a particular column layout...

Note: The **read plain hexadecimal dumps** is the unprintable binary **raw** stuff we want.

We're not working with files, but we *can* give xxd a standard input, or **stdin** by piping something into it. For example, ```echo 1a558acddabd64bbccdd94903eafdf18 | xxd -r -p``` results in
>U??ڽd??ݔ?>??

That looks right! Now we just need to pipe *that* into hex2raw.

SOLUTION:
```echo 1a558acddabd64bbccdd94903eafdf18 | xxd -r -p | ./hex2raw```
>You gave me:
>1a558acddabd64bbccdd94903eafdf18
>Yay! That's what I wanted! Here be the flag:
>ceb80093717fd7e9aae149dacc7ac9b3

## Other write-ups and resources

* none yet

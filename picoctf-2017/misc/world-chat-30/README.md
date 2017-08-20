# picoCTF 2017 : world-chat-30

**Category:** Misc
**Points:** 30
**Solves:** 
**Description:**

> We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:14747. Remember to use Ctrl-C to cut the connection if it overwhelms you!
> 
> 
>  HINTS
> 
> There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)


## Write-up

We start out by just connecting to the WorldChat with ```nc shell2017.picoctf.com 14747```. It's really confusing, but after running it a couple seconds, stopping it, then looking back on the logs while looking for "flag", you can see a message like ```15:16:14 flagperson: this is part 1/8 of the flag - ab4b```

We can pipe the WorldChat through a **grep** function that only looks for lines that match the regex "of the flag".

```nc shell2017.picoctf.com 14747 | grep "of the flag"```

```
15:16:14 flagperson: this is part 1/8 of the flag - ab4b
15:16:16 flagperson: this is part 2/8 of the flag - 181f
15:16:19 flagperson: this is part 3/8 of the flag - 3bc9
15:16:20 flagperson: this is part 4/8 of the flag - 2758
15:16:20 flagperson: this is part 5/8 of the flag - 9e0d
15:16:26 flagperson: this is part 6/8 of the flag - 79a4
15:16:28 flagperson: this is part 7/8 of the flag - 845a
15:16:31 flagperson: this is part 8/8 of the flag - 3ace
```

FLAG: ab4b181f3bc927589e0d79a4845a3ace

## Other write-ups and resources

* none yet

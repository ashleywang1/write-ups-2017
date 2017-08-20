# picoCTF 2017 : looooong-20

**Category:** Misc
**Points:** 20
**Solves:** 
**Description:**

> I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:14319?
> 
> 
>  HINTS
> 
> Use the nc command to connect!
> 
> I hear python is a good means (among many) to generate the needed input.
> 
> It might help to have multiple windows open


## Write-up

Connect with ```nc shell2017.picoctf.com 59858```

You're greeted with the prompt:
```To prove your skills, you must pass this test.
Please give me the 'W' character '581' times, followed by a single '4'.
To make things interesting, you have 30 seconds.
Input:
```

You definitely can't do this by hand, so you can use python.
```'W'*581+'4'```

Copy-and-pasting the output within 30 seconds gives you:
```You got it! You're super quick!
Flag: with_some_recognition_and_training_delusions_become_glimpses_ee260d1c785fd08f5d78753feae3c553
```

## Other write-ups and resources

* none yet

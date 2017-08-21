# picoCTF 2017 : so-random-75

**Category:** Cryptography
**Points:** 75
**Solves:** 
**Description:**

> We found sorandom.py running at shell2017.picoctf.com:33123. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?
> 
> Update (text only) 16:16 EST 1 Apr Running python 2 (same version as on the server)
> 
> 
>  HINTS
> 
> How random can computers be?


## Write-up

Looking at sorandom.py, we find to our delight that

```random.seed("random")```

Once we know the seed, we can regenerate every single random number, in order, that sorandom.py used. The conversion equation from the character **c** to the encrypted character **enc** is:

> enc = chr((ord(c) - ord('A') + random.randrange(0,26))%26 + ord(A))

The reverse equation from the encrypted character **enc** to **c** is:

> c = chr( ord(enc) - random.randrange(0,26) + n*26)
> where n is 0 or 1, and ord(c) >= ord('A')

The is only for the uppercase letters, but the concept is the same for both lowercase letters and digits. With this, we can write a script to un-randomize the flag. See the python script solution.py.

SOLUTION:
```FLAG:96109120ba8d1c844afe294c3cd1eb4c```

## Other write-ups and resources

* none yet

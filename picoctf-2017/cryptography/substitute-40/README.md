# picoCTF 2017 : substitute-40

**Category:** Cryptography
**Points:** 40
**Solves:** 
**Description:**

> A wizard (he seemed kinda odd...) handed me this. Can you figure out what it says?
> 
> 
>  HINTS
> 
> There are tools that make this easy this.


## Write-up

Looking at the text, there are two things that stand out. 1) The phrase 'MIT' show up a lot. It probably replaces the most common three-letter word 'the'. 2) There are numbers and dates in the text, that don't appear to have been changed or shifted in any way. This points to a substitution cipher.

Putting the text into an [online substitution cipher decoder](http://quipqiup.com/) with the guess that "MIT=THE", we get the cleartext paragraph that starts with

>THE FLAG IS IFONLYMODERNCRYPTOWASLIKETHIS.

## Other write-ups and resources

* none yet

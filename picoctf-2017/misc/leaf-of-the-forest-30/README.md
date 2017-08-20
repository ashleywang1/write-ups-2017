# picoCTF 2017 : leaf-of-the-forest-30

**Category:** Misc
**Points:** 30
**Solves:** 
**Description:**

> We found an even bigger directory tree hiding a flag starting at /problems/fbe763a61c09ffcd77f78551ba8a34c0. It would be impossible to find the file named flag manually...
> 
> 
>  HINTS
> 
> Is there a search function in Linux? Like if I wanted to 'find' something...


## Write-up

```find -iname "flag"``` results in
```./forest/tree2763a4/trunk764d/trunke6d5/trunk7905/trunk0008/trunk95d7/trunkcbe5/trunk2319/branchc790/flag```

```cat ./forest/tree2763a4/trunk764d/trunke6d5/trunk7905/trunk0008/trunk95d7/trunkcbe5/trunk2319/branchc790/flag``` results in

FLAG:
```395ba83a5a494eb04f43e15020577a75```

## Other write-ups and resources

* none yet

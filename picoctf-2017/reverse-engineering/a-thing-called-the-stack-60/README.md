# picoCTF 2017 : a-thing-called-the-stack-60

**Category:** Reverse Engineering
**Points:** 60
**Solves:** 
**Description:**

> A friend was stacking dinner plates, and handed you this, saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df
> 
> 
>  HINTS
> 
> Where is the return address saved on the stack?
> 
> Which commands actually affect the stack?


## Write-up

The return address is saved at the location of register EBP +4 (bytes). Think of every 4 bytes as a 'line' in memory that contains some value or register. The stack grows *downward*, which means that higher addresses are at the beginning of the stack, and lower addresses are towards the end.

```
foo:                            # ESP is pointing to the RET pointer when entering this function
    pushl %ebp                  # Push EBP to the stack, ESP dec by 4 bytes
    mov %esp, %ebp              # Update EBP with the value of ESP  (does nothing to ESP)
    pushl %edi                  # Push EDI to the stack, ESP dec by 4 bytes
    pushl %esi                  # Push ESI to the stack, ESP dec by 4 bytes
    pushl %ebx                  # Push EBX to the stack, ESP dec by 4 bytes
    sub $0x12c, %esp             # Subtract 0xF4 from ESP
    movl $0x1, (%esp)           # This and the next 3 instructions move values onto the stack without moving where ESP is pointing
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

On the second line, the difference between ESP and the Return pointer is 0x4 (since the Return pointer is 0x4 higher than EBP). The next three pushl instructions increment that difference by 0x4 each, for a total of 0xc. Finally, ESP goes down by 0x12C. In total, that's 0x13c.

FLAG: ```0x13c```

## Other write-ups and resources

* none yet

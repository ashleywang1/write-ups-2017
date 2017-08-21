#!/usr/bin/env python
import random,string

encflag = "BNZQ:20380043pc5p8u861tcy650q8xn8mf5d"
flag = ""
random.seed("random")
for enc in encflag:
	if enc.islower():
		tmp = ord(enc) - random.randrange(0,26)
		if tmp < ord('a'):
			flag += chr(tmp + 26)
		else:
			flag += chr(tmp)
	if enc.isupper():
		tmp = ord(enc) - random.randrange(0,26)
		if tmp < ord('A'):
			flag += chr(tmp + 26)
		else:
			flag += chr(tmp)
	if enc.isdigit():
		tmp = ord(enc) - random.randrange(0,10)
		if tmp < ord('0'):
			flag += chr(tmp + 10)
		else:
			flag += chr(tmp)
	if enc == ":":
		flag += ":"

print flag


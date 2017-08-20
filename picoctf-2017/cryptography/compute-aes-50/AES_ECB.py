#!/usr/bin/python
from Crypto.Cipher import AES
from base64 import b64decode

# Since both the key and the encrypted message are base64 encoded, we base64 decode them first
key = b64decode("BmVWeKy6Qd+LEUXnG81SJQ==")
ciphertext = b64decode("0hxb++cNGw5/mPbBGzFzmREFL9waMmCuHK0DmkqXzRYXvj6+AqKvvhDwP5e1CS/w")

# Then, we create a new AES object, with the key and AES mode as parameters
obj = AES.new(key, AES.MODE_ECB)

# We finally use the decrypt function to get the cleartext message
cleartext = obj.decrypt(ciphertext)

# Output to screen
print "[+] Flag : %s" % cleartext

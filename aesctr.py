#!/usr/bin/python

import Crypto.Cipher.AES
import Crypto.Util.Counter
import sys

# Functions to provide PKCS5 Padding
# Taken from http://stackoverflow.com/a/13893208/2748059
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

encrypt = False
decrypt = True

if len(sys.argv) != 5:
    print "Syntax: " + sys.argv[0] + " <input file> <output file> <16 byte key> + <16 byte IV>"
    sys.exit(1)

inFilename = sys.argv[1]
outFilename = sys.argv[2]
key = sys.argv[3]
iv = sys.argv[4]

if len(key) != 16:
    print "Key must be 16 bytes in length"
    sys.exit(1)

if len(iv) != 16:
    print "IV must be 16 bytes in length"
    sys.exit(1)

inFile = open(inFilename, "rb")
outFile = open(outFilename, "wb")
ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, counter=ctr)

while encrypt:
    chunk = inFile.read(16)
    if chunk:
        outFile.write(cipher.encrypt(pad(chunk)))
    else:
        break

while decrypt:
    chunk = inFile.read(16)
    if chunk:
        outFile.write(unpad(cipher.decrypt(chunk)))
    else:
        break

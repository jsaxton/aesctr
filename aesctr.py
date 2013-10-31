#!/usr/bin/python

import Crypto.Cipher.AES
import Crypto.Util.Counter
import sys

BLOCK_SIZE = 16

# TODO: Better argument parsing
if len(sys.argv) != 6:
    print "Syntax: " + sys.argv[0] + " [-d|-e] <input file> <output file> <key> <iv>"
    print "Key and IV are expected to be 128 bit hex strings (32 characters, no preceeding 0x)"
    print "-d flag is used to decrypt, -e flag is used to encrypt"
    sys.exit(1)

if sys.argv[1] == '-d':
    encrypt = False
    decrypt = True
elif sys.argv[1] == '-e':
    encrypt = True
    decrypt = False
else:
    print "First argument must be -d (decrypt) or -e (encrypt)"
    sys.exit(1)

inFilename = sys.argv[2]
outFilename = sys.argv[3]
key = sys.argv[4]
iv = sys.argv[5]

if len(key) != BLOCK_SIZE * 2:
    print "Key must be " + BLOCK_SIZE + " bytes in length"
    sys.exit(1)

if len(iv) != BLOCK_SIZE * 2:
    print "IV must be " + BLOCK_SIZE + " bytes in length"
    sys.exit(1)

inFile = open(inFilename, "rb")
outFile = open(outFilename, "wb")
ctr = Crypto.Util.Counter.new(BLOCK_SIZE*8, initial_value=long(iv, 16))
cipher = Crypto.Cipher.AES.new(key.decode("hex"), Crypto.Cipher.AES.MODE_CTR, counter=ctr)

while encrypt:
    chunk = inFile.read(BLOCK_SIZE)
    if chunk:
        outFile.write(cipher.encrypt(chunk))
    else:
        break

while decrypt:
    chunk = inFile.read(BLOCK_SIZE)
    if chunk:
        outFile.write(cipher.decrypt(chunk))
    else:
        break

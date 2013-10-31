aesctr
======

I have some systems at work that have an older version of openssl installed, and as such, these systems cannot encrypt or decrypt data using aes-128-ctr from the command line. Rather than upgrade openssl, I decided to write a simple python script instead.

Based off my limited testing, this script works in aes-128-ctr mode. It can easily be expanded to work with 192 and 256 bit block sizes as well. In addition, I should probably clean up the argument parsing, but the current implementation works well enough for my purposes.

Syntax 
======
./aesctr.py [-d|-e] <input file> <output file> <key> <iv>

Key and IV are expected to be 128 bit hex strings (32 characters, no preceeding 0x)

-d flag is used to decrypt, -e flag is used to encrypt

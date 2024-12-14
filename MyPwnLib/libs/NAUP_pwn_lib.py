from pwn import *

def x64_env():
    context(arch = 'amd64', os = 'linux')

def x86_env():
    context(os='linux', arch='i386')

def WindowsNewlineSet(r):
    r.newline = b"\r\n"

def debug_init():
    a=input('open debug?(y/n/srop)')
    if a=='y':
        context.log_level = 'debug'
        context.terminal = ['tmux', 'splitw', '-h']
    elif a=='srop':
        context.log_level = 'debug'
        context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']

def p(r):
    gdb.attach(r)

def p_c(r,cmd):
    gdb.attach(r,cmd)

def srop_p(r):
    gdb.attach(proc.pidof(r)[0])

def NAUPINFO(item,data):
    print("NAUPINFO @ {}: {}".format(item,data))

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

def chunk_decrypt(pos,fd):
    return fd ^ (pos >> 12)


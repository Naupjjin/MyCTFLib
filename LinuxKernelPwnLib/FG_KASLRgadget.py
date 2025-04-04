from pwn import *

i = 0
with open("./gadgets.txt", "rt") as f:
    with open("./gadgets_fg.txt", "wt") as f2:
        line = f.readline()
        while line != '':
            if not line.startswith('0x'):
                line = f.readline()
                continue
            i += 1
            if i % 0x100 == 0:
                print(f"Success process of {i} lines.")
            if int(line.split(' ')[0], 16) < 0xffffffff81200000:
                f2.write(line)
            line = f.readline()        
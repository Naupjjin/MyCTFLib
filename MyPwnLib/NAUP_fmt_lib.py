from pwn import *


class FMT_obj:
    
    def __init__(self):
        self.byte1 = 256
        self.byte2 = 256 ** 2
        self.byte4 = 256 ** 4
        self.byte8 = 256 ** 8

        self.fmt_num_list = []

    # generate fmt number list 1 byte (hhn)
    def GFN_1(self, num: int):
        prev_output = 0
        while num != 0:
            self.fmt_num_list.append(hex((self.byte1-prev_output+num) & 0xff))
            num = num >> 8
            prev_output = (self.byte1-prev_output+num) & 0xff

        return self.fmt_num_list
        

    # generate fmt number list 2 byte (hn)
    def GFN_2(self, num: int):
        prev_output = 0
        while num != 0:
            self.fmt_num_list.append(hex((self.byte2-prev_output+num) & 0xffff))
            num = num >> 16
            prev_output = (self.byte2-prev_output+num) & 0xffff

        return self.fmt_num_list
    
    # generate fmt number list 4 byte (n)
    def GFN_4(self, num: int):
        prev_output = 0
        while num != 0:
            self.fmt_num_list.append(hex((self.byte4-prev_output+num) & 0xffffffff))
            num = num >> 32
            prev_output = (self.byte4-prev_output+num) & 0xffffffff

        return self.fmt_num_list

    # generate fmt number list 8 byte (lln)
    def GFN_8(self, num: int):
        prev_output = 0
        while num != 0:
            self.fmt_num_list.append(hex((self.byte8-prev_output+num) & 0xffffffffffffffff))
            num = num >> 64
            prev_output = (self.byte8-prev_output+num) & 0xffffffffffffffff

        return self.fmt_num_list

    def gen_fmt_payload(list_addr, list_place):
        pass

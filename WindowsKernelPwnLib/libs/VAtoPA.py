def PAtoVA_4page_cal(address):
    PML4_offset = (address >> 39) & 0b111111111
    PDPT_offset = (address >> 30) & 0b111111111
    PD_offset = (address >> 21) & 0b111111111
    PT_offset = (address >> 12) & 0b111111111
    PhysicalAddress_offset = (address) & 0b111111111

    print("PML4_offset: ",hex(PML4_offset))
    print("PDPT_offset: ",hex(PDPT_offset))
    print("PD_offset: ",hex(PD_offset))
    print("PT_offset: ",hex(PT_offset))
    print("PhysicalAddress_offset: ",hex(PhysicalAddress_offset))
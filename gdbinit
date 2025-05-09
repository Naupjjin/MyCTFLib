#source ~/peda/peda.py
source /home/naup/pwndbg/gdbinit.py
source /home/naup/Pwngdb/pwngdb.py
source /home/naup/Pwngdb/angelheap/gdbinit.py

define hook-run
python
import angelheap
angelheap.init_angelheap()
end
end

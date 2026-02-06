all:
	gcc exploit.c -o exploit --static
extract:
	mkdir -p sysfile
	cd sysfile && sudo cpio -idmv < ../initramfs.cpio
pack:
	cd sysfile && sudo sh -c 'find . -print0 | cpio --null -ov -H newc > ../initramfs.cpio'
gunzip-cpio:
	gunzip initramfs.cpio.gz
cp-exploit:
	cp exploit sysfile/exploit

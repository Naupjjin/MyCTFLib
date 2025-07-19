# cheatsheet
> Author: 堇姬Naup

## cheatsheet
```sh
mkdir -p sysfile
mv ./initramfs.cpio ./initramfs.cpio.gz
gunzip initramfs.cpio.gz
cpio -idmv -D sysfile < initramfs.cpio
find . | cpio -o -H newc --owner root:root > ../new_initramfs.cpio
```

```sh
setsid /bin/cttyhack setuidgid 0 /bin/sh
```

```sh
find . | cpio -o --format=newc > ../initramfs.cpio
```

```sh
-gdb tcp::1234 \
-S

gdb -q -ex "target remote localhost:1234"
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
```

```sh
obj-m += naupdriver.o

KDIR =/home/naup96321/Desktop/mykernel/linux-5.11

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	rm -rf *.o *.ko *.mod.* *.symvers *.order
```

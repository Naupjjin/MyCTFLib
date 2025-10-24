import socket

class QemuMonitorCommand(GenericCommand):
    """
	Send a command to QEMU monitor via UNIX socket.
    
    -monitor unix:/tmp/qemu-monitor.sock,server,nowait
	by. naup
    """

    _cmdline_ = "qemu_monitor"
    _syntax_  = "qemu_monitor 'monitor_command_string'"

    def __init__(self):
        super(QemuMonitorCommand, self).__init__(self._cmdline_, gdb.COMMAND_OBSCURE)
        self.monitor_path = "/tmp/qemu-monitor.sock"

    def do_invoke(self, argv):
        if not argv:
            err("Usage: qemu_monitor 'command'")
            return

        cmd = " ".join(argv) + "\n"

        try:
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.connect(self.monitor_path)
                sock.sendall(cmd.encode())
                sock.settimeout(0.2)

                response = b""
                while True:
                    try:
                        data = sock.recv(4096)
                        if not data:
                            break
                        response += data
                    except socket.timeout:
                        break

                print(response.decode(errors="ignore").strip())

        except Exception as e:
            err(f"Failed to connect to QEMU monitor: {e}")

QemuMonitorCommand()

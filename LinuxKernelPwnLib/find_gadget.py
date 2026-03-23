import subprocess

result = subprocess.run(['objdump', '-M', 'intel', '-d', 'vmlinux'], capture_output=True, text=True)
lines = result.stdout.split('\n')

for i, line in enumerate(lines):
    if 'swapgs' in line:
        context = []
        for j in range(5):
            if i + j < len(lines):
                context.append(lines[i + j])
                if 'ret' in lines[i + j] or ('jmp' in lines[i + j] and 'return_thunk' in lines[i + j]):
                    print("Found potential swapgs gadget:")
                    for c in context:
                        print(f"  {c}")
                    print()
                    break
                if 'call' in lines[i + j]:
                    break

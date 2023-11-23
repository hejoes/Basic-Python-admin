import os
import subprocess

top_output = subprocess.run(["top", "-b", "-n", "1", "-o", "+%CPU", "-c", "-U", os.getlogin()], capture_output=True, text=True).stdout

# Extract the command name and CPU usage from each line
commands = []
for line in top_output.split("\n")[7:]:
    parts = line.split()
    if len(parts) < 9:
        continue
    command = parts[-1]
    cpu_usage = parts[8]
    commands.append((command, cpu_usage))

# Sort the commands by CPU usage
commands = sorted(commands, key=lambda x: float(x[1]), reverse=True)

if len(commands)>=5:
    for i in range(5):
        print(f'Application: {commands[i][0]}, CPU usage: {commands[i][1]}')
else:
    for command in commands:
        print(f'Application: {command[0]}, CPU usage: {command[1]}')

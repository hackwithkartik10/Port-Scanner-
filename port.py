import pyfiglet
port=pyfiglet.figlet_format("PORT SCANNER")
print(port)

import socket
target = input("Enter IP or domain: ")

print(f"Scanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    s.close()
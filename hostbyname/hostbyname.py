import socket as s
from sys import argv

path = argv[1]

hosts = []

with open(path, 'r') as file:
    lines = list(file)
    for line in lines:
        hosts.append(line.strip())
file.close()

try:
    for url in hosts:
        print(f'{url}: ', s.gethostbyname(url))

except s.gaierror:
    print('Exiting: each host should be on a new line.')
    raise SystemExit


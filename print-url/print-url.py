#!/usr/bin/env python3

from re import findall
from sys import stdin

data = stdin.read()

urls = findall(r'(https?://\S+)', data)

if urls:
    for url in urls:
    	print(url)
else:
	print("No URLS were found!")
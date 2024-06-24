#!/usr/bin/env python3

from sys import argv

title = argv[1]

title = title.lower().replace(" ", "-")

print(title)
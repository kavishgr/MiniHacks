#!/usr/bin/env python3

import re
from sys import stdin

def squeeze_chars(text, char='-'):
    pattern = re.escape(char) + r'{2,}'
    return re.sub(pattern, char, text)

title = stdin.read()
title = title.lower().replace(" ", "-")
title = squeeze_chars(title)
print(title)
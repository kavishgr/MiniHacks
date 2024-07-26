#!/usr/bin/env python3

import re
from sys import argv

def squeeze_chars(text, char='-'):
    pattern = re.escape(char) + r'{2,}'
    return re.sub(pattern, char, text)

title = argv[1]
title = title.lower().replace(" ", "-")
title = squeeze_chars(title)
print(title)
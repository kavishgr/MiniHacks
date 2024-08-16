#!/bin/bash

echo

date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S"

echo

system_profiler SPPowerDataType \
| grep -Ei 'charging|cycle|capacity|state' \
| head -n 4 \
| sed 's/^[t ]*//g'

#!/bin/bash

title=$(< /dev/stdin)
echo "$title" | tr ' ' '-' | tr -s '-' | tr '[:upper:]' '[:lower:]'

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import numpy as np

#===============================================================================
def main():
    if(len(sys.argv) < 2):
        print("walltimes2csv.py <out-file1> ... <out-fileN>")
        sys.exit(1)

    files = sys.argv[1:]
    keys = []
    values = []
    for fn in files:
        keys.append(fn.rsplit(".", 1)[0])
        content = open(fn).read()
        line = re.search("CP2K    (.*)\n", content).group(1)
        walltime = float(line.split()[5])
        values.append(walltime)

    print(", ".join(keys))
    print(", ".join(["%f"%v for v in values]))

#===============================================================================
main()
#EOF


#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import numpy as np

#===============================================================================
def main():
    if(len(sys.argv) < 2):
        print("libtest_analyse.py <out-file1> ... <out-fileN>")
        sys.exit(1)

    table = dict()
    files = sys.argv[1:]
    for fn in files:
        content = open(fn).read()
        flops = np.array(re.findall("\s(\d+) Mflops/rank", content), np.int)
        flops_max = np.amax(flops[1:])
        key = fn.rsplit(".", 1)
        table[key] = flops_max / 1000.0

    print(", ".join(sorted(table.keys())))
    print(", ".join([table[k] for k in sorted(table.keys())]))

#===============================================================================
main()
#EOF

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import numpy as np

#===============================================================================
def main():
    if(len(sys.argv) < 2):
        print("libtest2csv.py <ref_checksum> <out-file1> ... <out-fileN>")
        sys.exit(1)

    table = dict()
    reference = float(sys.argv[1])
    files = sys.argv[2:]
    for fn in files:
        content = open(fn).read()
        checksum = float(re.search("Final checksums\s+(.+?)\s+", content).group(1))
        assert(abs(checksum-reference) < 0.05)
        flops = np.array(re.findall("\s(\d+) Mflops/rank", content), np.int)
        flops_max = np.amax(flops[1:])
        key = fn.rsplit(".", 1)[0]
        table[key] = flops_max / 1000.0

    print(", ".join(sorted(table.keys())))
    print(", ".join(["%f"%table[k] for k in sorted(table.keys())]))

#===============================================================================
main()
#EOF


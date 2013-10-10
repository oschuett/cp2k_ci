#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import numpy as np

#===============================================================================
def main():
    if(len(sys.argv) < 4):
        print("libtest_analyse.py <ref_energy> <tolerance> <output_file>")
        sys.exit(1)

    table = dict()
    reference = float(sys.argv[1])
    tolerance = float(sys.argv[2])
    fn = sys.argv[3]
    content = open(fn).read()
    energy = float(re.search("ENERGY\| Total[^:]*:\s*(.+)\s", content).group(1))
    assert(abs(energy-reference) < tolerance)

#===============================================================================
main()
#EOF


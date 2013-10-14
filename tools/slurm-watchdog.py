#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import os
import time
import signal
import traceback
import subprocess
from os import path





#===============================================================================
def main():
    if(len(sys.argv) != 3):
        print "Usage: slurm-watchdog.py <parent-pid> <file-with-jobids>"
        sys.exit(1)

    pid = sys.argv[1]
    content = open(sys.argv[2]).read()

    jobids = []
    for line in content.strip().split("\n"):
        m = re.match(r"Submitted batch job (\d+)", line)
        jobids.append(m.group(1))

    print("slurm-watchdog: launched with jobids: %s"%str(jobids))
    sys.stdout.flush()

    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)

    log = open("watchdog.log", "w")

    log.write("slurm-watchdog: launched with jobids: %s\n"%str(jobids))
    log.flush()

    try:

        while(path.exists("/proc/"+pid)):
            time.sleep(1)

        for j in jobids:
            log.write("slurm-watchdog: scancel %s\n"%j)
            log.flush()
            subprocess.call(["scancel", j])

    except:
        log.write(traceback.format_exc())
        log.flush()

    finally:
        log.close()

#===============================================================================
main()

#EOF


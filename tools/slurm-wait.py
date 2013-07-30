#!/usr/bin/python
# -*- coding: utf-8 -*-

#from subprocess import 

import sys
import re
import time
from subprocess import Popen, PIPE


#===============================================================================
class Job(object):
    def __init__(self, jobid):
       self.jobid = jobid
       self.state = None

    #---------------------------------------------------------------------------
    def __repr__(self):
        return("Job(%s)"%self.jobid)

    #---------------------------------------------------------------------------
    def update_state(self):
        new_state = self.get_state()
        if(new_state != self.state):
            print("Job %s: %s"%(self.jobid,new_state))
            sys.stdout.flush()
        self.state = new_state

    #---------------------------------------------------------------------------
    def get_state(self):
        cmd =  ["squeue"]
        cmd += [r"--format=state:%T start:%S end:%e"]
        cmd += ["--noheader"]
        cmd += ["--jobs="+self.jobid]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        p.wait()

        #if(print [stdout]
        #if("Invalid job id specified" in stderr):
        #    return(None)
        return(stdout.strip())

#===============================================================================
def main():
    if(len(sys.argv) != 2):
        print "Usage: slurm-wait.py <file-with-jobids>"
        sys.exit(1)

    content = open(sys.argv[1]).read()

    jobs = []
    for line in content.strip().split("\n"):
        m = re.match(r"Submitted batch job (\d+)", line)
        jobs.append(Job(m.group(1)))

    running_jobs = list(jobs)
    while(len(running_jobs)>0):
        time.sleep(1)
        #print("Pooling...")
        for j in running_jobs:
            j.update_state()
            if(j.state == ""):
                print "Job %s has finished."%j.jobid
                running_jobs.remove(j)


main()

#EOF


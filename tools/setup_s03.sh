set +x
#source /opt/intel/bin/ifortvars.sh intel64
source /data/vjoost/valgrind-3.8.0/setup
source /opt/intel/composerxe-2011.3.174/bin/ifortvars.sh intel64
source /data/vjoost/gnu/gcc-4_7-branch/setup
source /data/vjoost/oprofile-0.9.8/setup
source /data/vjoost/openmpi-1.6.3/setup

# here the order matters :-(
source /etc/profile.d/modules.sh
module load intel-2013.0.079
module load openmpi-x86_64
module load cuda-5.5.22-x86_64

set -x

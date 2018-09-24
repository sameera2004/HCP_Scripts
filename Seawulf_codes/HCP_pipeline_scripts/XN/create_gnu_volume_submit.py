"""
	Developed by Sameera Abeykoon

	example: python create_gnu_volume_submit.py
        This will create gnu_volume_submit.sh script

"""
from __future__ import print_function
import os
import sys
#from builtins import input

def gnu_volume(sub_nu, nu_jobs):

	v = sub_nu + "_gnu_volume_submit.sh"
	g = open(v, 'w')

	g.write("#!/bin/bash\n\n")
	g.write("#Set the number of nodes and processes per node\n")
	g.write("#PBS -l nodes=1:ppn=28\n\n")

	#g.write("# set max wallclock time\n")
	g.write("# set max wallclock time\n")
	g.write("#PBS -l walltime=8:00:00\n\n")

	g.write("#PBS -q gpu\n\n")

	g.write("# set name of job\n")
	g.write("#PBS -N " + sub_nu + "_volumes\n\n")

	g.write("# use submission environment\n") 
	g.write("#PBS -V\n\n")

	g.write("# start job from the directory it was submitted")
	g.write("cd $PBS_O_WORKDIR\n\n")
	#cd /gpfs/software/Pipelines-3.24.0/Examples/Scripts

	g.write("module load shared\n")
	g.write("module load fsl/5.0.6\n")
	g.write("module load gradunwarp/1.0.2\n")
	g.write("module load HCP-Pipelines/3.24.0\n")
	g.write("module load freesurfer/5.3.0-HCP\n")
	g.write("module load libpng/1.6.28\n")
	g.write("module load libmng/2.0.3\n")
	g.write("module load nibabel/1.2.0\n")
	g.write("module load hdf5/1.8.4\n")
	g.write("module load netcdf/rpm/64/4.1.1-3\n")
	g.write("module load gnu-parallel/6.0\n\n")

	g.write("Subjlist=\""+sub_nu +"\"\n")

	g.write("parallel --jobs "+ nu_jobs + " < " + sub_nu + "_volume_subjob.txt")
        return

if __name__ == "__main__":
        # get the subject number
   	sub_nu = sys.argv[1]
        # get the number of jobs
        nu_jobs = sys.argv[2]
        gnu_volume(sub_nu, nu_jobs)   
        print (sub_nu + "_gnu_volume_submit.sh is ready")     

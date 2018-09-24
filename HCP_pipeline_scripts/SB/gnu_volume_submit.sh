#!/bin/bash 

#Set the number of nodes and processes per node
#PBS -l nodes=1:ppn=28

# set max wallclock time
#PBS -l walltime=8:00:00

#PBS -q gpu

# set name of job
#PBS -N 2264

# mail alert at (b)eginning, (e)nd and (a)bortion of execution
#PBS -m bea

# send mail to the following address
#PBS -M sameera.abeykoon@stonybrookmedicine.edu

# use submission environment 
#PBS -V

# start job from the directory it was submitted
cd $PBS_O_WORKDIR
#cd /gpfs/software/Pipelines-3.24.0/Examples/Scripts

module load shared
module load fsl/5.0.6
module load gradunwarp/1.0.2
module load HCP-Pipelines/3.24.0
module load freesurfer/5.3.0-HCP
module load libpng/1.6.28
module load libmng/2.0.3
module load nibabel/1.2.0
module load hdf5/1.8.4
module load netcdf/rpm/64/4.1.1-3
module load gnu-parallel/6.0

Subjlist="2264"
parallel --jobs 18 < ${Subjlist}_volume_subjob.txt

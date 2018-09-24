#!/bin/bash 

#set the number of nodes and processes per node
#PBS -l nodes=1:ppn=28

# set max wallclock time
#PBS -l walltime=2:00:00

#PBS -q short

# set name of job
#PBS -N PO_FS_3057

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
module load nibabel/1.2.0
module load hdf5/1.8.4
module load netcdf/rpm/64/4.1.1-3
module load libmng/2.0.3

# Set variable values that locate and specify data to process
Subjlist=${Subjlist}

sh /gpfs/projects/VanSnellenbergGroup/HCP_pipeline_codes/PostFreeSurferPipelineBatch_${Subjlist}.sh \
 >/gpfs/projects/VanSnellenbergGroup/SB_HCP_data/outputs/PO_Fsurfer_${Subjlist}.out 2>/gpfs/projects/VanSnellenbergGroup/SB_HCP_data/outputs/PO_Fsurfer_${Subjlist}.error

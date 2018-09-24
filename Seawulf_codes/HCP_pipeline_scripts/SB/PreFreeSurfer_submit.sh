#!/bin/bash 

#set the number of nodes and processes per node
#PBS -l nodes=1:ppn=28

# set max wallclock time
#PBS -l walltime=4:00:00

#PBS -q gpu

# set name of job
#PBS -N PFS_3057

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

# Set variable values that locate and specify data to process
Subjlist=${Subjlist}

#sh /gpfs/software/Pipelines-3.24.0/Examples/Scripts/PreFreeSurferPipelineBatch_SB_SpinEcho_FieldMap.sh $StudyFolder $Subjlist>/gpfs/home/sabeykoon/PFsurfer_50027.out 2>&1
sh /gpfs/projects/VanSnellenbergGroup/HCP_pipeline_codes/PreFreeSurferPipelineBatch_${Subjlist}.sh \
 >/gpfs/projects/VanSnellenbergGroup/SB_HCP_data/outputs/PFsurfer_${subjlist}.out 2>/gpfs/projects/VanSnellenbergGroup/SB_HCP_data/outputs/PFsurfer_${Subjlist}.error


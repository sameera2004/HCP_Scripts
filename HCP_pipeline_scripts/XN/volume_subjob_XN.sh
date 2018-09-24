#!/bin/sh

############################################################

# Developed by Sameera K. Abeykoon (August  2018)
# This will create Subject_number_volume_subjob.txt and
# Subject_number_gnu_volume_submit.sh
#############################################################

module load shared
module load anaconda/2

# Developed by Sameera K. Abeykoon (August  2018)

echo Enter the Subject number
read Subjlist

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${Subjlist}

readarray fMRI_list <${Subjlist}_scanlog_fMRI.txt 

echo -n "" > ${Subjlist}_volume_subjob.txt

for fMRI in "${fMRI_list[@]}"; do :;
   printf "sh /gpfs/software/Pipelines-3.24.0/Examples/Scripts/volume_processing/GenericfMRIVolumeProcessingPipelineBatch_${Subjlist}_${fMRI}.sh\ 
   >/gpfs/scratch/sabeykoon/HCP_data/outputs/GVP_${Subjlist}_${fMRI}.out \
   2>/gpfs/scratch/sabeykoon/HCP_data/outputs/GVP_${Subjlist}_${fMRI}.error\n" >> ${Subjlist}_volume_subjob.txt
done

# Get the length of the fMRI_list
jobs_nu=${#fMRI_list[@]}

#python create_gnu_volume_submit.py "gnu_volume(${Subjlist},${jobs_nu})" 
python create_gnu_volume_submit.py ${Subjlist} ${jobs_nu}

#!/bin/sh

# Developed by Sameera K. Abeykoon (August  2018)

module load shared
module load anaconda/2

echo Enter the Subject number list eg:0194 2264 2280
read -a sub_list

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${sub_list[*]}

# create link Fieldmaps
python hcp_link_XN.py \[${sub_list[*]}\]

# This will create XN_pre_subjob.txt
sh pre_subjob_XN.sh "${sub_list[@]}"

# This will create XN_free_subjob.txt
sh free_subjob_XN.sh "${sub_list[@]}"

# This will create XN_po_subjob.txt
sh po_subjob_XN.sh "${sub_list[@]}"
 
#echo -n "" > XN_free_subjob.txt

#for Subjlist in "${sub_list[@]}"; do :;
#   printf "sh /gpfs/software/Pipelines-3.24.0/Examples/Scripts/FreeSurferPipelineBatch_XN_B0_${Subjlist}.sh >/gpfs/scratch/sabeykoon/HCP_data/outputs/Freesurfer_${Subjlist}.out 2>/gpfs/scratch/sabeykoon/HCP_data/outputs/Freesurfer_${Subjlist}.error\n" >> XN_free_subjob.txt
#done

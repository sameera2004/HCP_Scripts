#!/bin/sh

# Developed by Sameera K. Abeykoon (August  2018)

if [ "$#" -eq  "0" ]
   then
     echo Enter the Subject number list eg:0194 2264 2280
     read -a sub_list
else
     sub_list=("$@")
fi

#echo Enter the Subject number list eg:0194 2264 2280
#read -a sub_list

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${sub_list[*]}

echo -n "" > XN_po_subjob.txt

for Subjlist in "${sub_list[@]}"; do :;
   printf "sh /gpfs/software/Pipelines-3.24.0/Examples/Scripts/PostFreeSurferPipelineBatch_XN_B0_${Subjlist}.sh \
 >/gpfs/scratch/sabeykoon/HCP_data/outputs/PO_Fsurfer_${Subjlist}.out 2>/gpfs/scratch/sabeykoon/HCP_data/outputs/PO_Fsurfer_${Subjlist}.error\n" >> XN_po_subjob.txt
done

echo "XN_po_subjob.txt is ready"

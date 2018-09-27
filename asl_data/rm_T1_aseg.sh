#!/bin/bash
# This script will rm wrong T1.nii and aseg.nii files from Anat folder
# Provide the subject number
sub_num=$1
echo $sub_num
cd /mnt/hcp01/scR21_asl/asl_results/$sub_num
echo $PWD

for i in {1..3}
do
 cd /mnt/hcp01/scR21_asl/asl_results/$sub_num
 echo $PWD 
 # remove T.nii and aseg.nii files (wrong orientation)
 rm day_$i/Anat/T1.nii
 rm day_$i/Anat/aseg.nii
 cd /mnt/hcp01/scR21_asl/cortical_par/$sub_num
 echo $PWD
 rm day_$i/mri/T1.nii
 rm day_$i/mri/aseg.nii
done   
                      

#for i in {1..3}
#do
# cd day_${i}/mri
# echo $PWD 
# mri_convert --in_type mgz --out_type nii --out_orientation ASR T1.mgz ./T1.nii.gz
# mri_convert --in_type mgz --out_type nii --out_orientation ASR aseg.mgz ./aseg.nii.gz
# cd ../..
# echo $PWD
#done


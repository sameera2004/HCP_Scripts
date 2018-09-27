#!/bin/bash
# This script will convert T1.mgz and aseg.mgz image files to T1.nii.gz and aseg.nii.gz
# You need to be in the Subject directory to run this command.Each subject has three days of ASL data
# that is allreday done the cortical parcellation. Each date data is in different folders(day_1, day_2 and day_3)


# NOTE
# SPM --out orientation is ASR
# dicm2nii --out orientation is RAS

# Provide the subject number
sub_num=$1
echo $sub_num
cd /mnt/hcp01/scR21_asl/cortical_par/$sub_num
echo $PWD

for i in {1..3}
#for i in {1,3}
do
 cd day_${i}/mri
 echo $PWD
 rm -rf *.nii
 rm -rf *.nii.gz 
 mri_convert --in_type mgz --out_type nii --out_orientation RAS T1.mgz ./T1.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation RAS aseg.mgz ./aseg.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation RAS aparc+aseg.mgz ./aparc_aseg.nii.gz
 # zip the T1 and aseg images and copy to asl data folders
 gunzip *.nii.gz
 cp T1.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat
 cp aseg.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat
 cp aparc_aseg.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat
 cd ../..
 echo $PWD
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


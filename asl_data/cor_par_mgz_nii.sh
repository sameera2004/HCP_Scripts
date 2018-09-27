#!/bin/bash

# Developed by Sameera K. Abeykoon (March 2018)

# use GNU Parallel to batch process all three days brain data using a set number of processors to 3.
# The output will be saved inside each day folders (day_1, day_2 and day_3)
# recon-all is a freesufer command to do the cortical parcellation of the brains
# (This will take about ~8hours)

echo "Doing the cortical parcellation parallely for all 3 days data"

ls day*.nii | sed 's/.nii//' | parallel --jobs 3 recon-all -s {} -i {}.nii -all -sd .

# Following loop will convert T1.mgz and aseg.mgz image files to T1.nii.gz and aseg.nii.gz
# You need to be in the Subject directory to run this command.Each subject has three days of ASL data
# that is allreday done the cortical parcellation. Each date data is in different folders(day_1, day_2 and day_3)
# It is using freesufer mri_convert command to convert mgz to nii.gz. We need ASR orientation, because ealier data
# (fMRI data) in that orientation.

wait # wait until all the background processes finish then contiune

for i in {1..3}
do
 cd day_${i}/mri
 echo $PWD 
 mri_convert --in_type mgz --out_type nii --out_orientation ASR T1.mgz ./T1.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation ASR aseg.mgz ./aseg.nii.gz
 cd ../..
 echo $PWD
done

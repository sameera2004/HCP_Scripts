#!/bin/bash

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

# make directory for asl data analysis
mkdir /mnt/hcp01/scR21_asl/asl_results/$sub_num/
# make directory for cortical parcellation
echo "Make subject dir in cortical_par folder"
mkdir /mnt/hcp01/scR21_asl/cortical_par/$sub_num

echo Enter First date DICOM data directory
read data1
echo "1st day data: ${data1}"

echo Enter Second date DICOM data directory
read data2
echo "2nd day data: ${data2}"

echo Enter Third date DICOM data directory
read data3
echo "3rd day data: ${data3}"

data_list="$data1 $data2 $data3"
arr=($data_list)
echo "data list: {$data_list}"

current_path="$pwd"
cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
echo "change directory to DICM2NII folder : {$PWD}"
for i in {1..3};do
        echo /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i
        echo ${arr[$((i-1))]}
	/mnt/jxvs01/pipelines/HCP/usr/local/MATLAB/R2016b/bin/matlab -nodisplay -r "dicm2nii('/mnt/jxvs01/incoming/Smoking_Cessation_Abi_Dargham/${arr[$((i-1))]}', '/mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i', 0); quit"
done

cd $current_path

#  TODO 
# goto asl folders and work on that copying them to cor-Par and then get it back

cd /mnt/hcp01/scR21_asl/asl_results/$sub_num/

echo "Current driectory : ${pwd}"
for i in {1..3};do
        cd day_$i/
        # Remove unwanted folders 
        if [  $i -eq 1 ] || [ $i -eq 3 ]; then 
	 rm *Resting*
	 rm *SpinEchoFieldMap*
	 rm *field_map*
        fi
        # make Anat ASL and REF folders for the data analysis
        mkdir Anat Asl Ref
        # copy the T1W_MPR_003.nii into cortical parcellation dir
        cp T1w_MPR_s003.nii /mnt/hcp01/scR21_asl/cortical_par/$sub_num/day_$i.nii
        mv T1w_MPR_s003.nii Anat/
        # move the ASL and REF data files to those folders
        mv *REF* ./Ref
        mv *pCASL* ./Asl
        cd ..
done    

# change dir to cor_par_ subject dir to do the cortical parcellation
cd /mnt/hcp01/scR21_asl/cortical_par/$sub_num
echo "Current directory : ${PWD}"
# use GNU Parallel to batch process all three days brain data using a set number of processors to 3.
# The output will be saved inside each day folders (day_1, day_2 and day_3)
# recon-all is a freesufer command to do the cortical parcellation of the brains
# (This will take about ~8hours)

echo "Doing the cortical parcellation parallely for all 3 days data"

#ls day*.nii | sed 's/.nii//' | parallel --jobs 3 recon-all -s {} -i {}.nii -all -sd .

# Following loop will convert T1.mgz and aseg.mgz image files to T1.nii.gz and aseg.nii.gz
# You need to be in the Subject directory to run this command.Each subject has three days of ASL data
# that is allreday done the cortical parcellation. Each date data is in different folders(day_1, day_2 and day_3)
# It is using freesufer mri_convert command to convert mgz to nii.gz. We need ASR orientation, because ealier data
# (fMRI data) in that orientation.

#wait # wait until all the background processes finish then contiune

#for i in {1..3}
#do
# cd day_${i}/mri
# echo $PWD 
# mri_convert --in_type mgz --out_type nii --out_orientation ASR T1.mgz ./T1.nii.gz
# mri_convert --in_type mgz --out_type nii --out_orientation ASR aseg.mgz ./aseg.nii.gz
# gunzip (*.gz)
# cp T1.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i
# cp aseg.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i 
# cd ../..
# echo $PWD
#done   

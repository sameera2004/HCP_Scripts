#!/bin/bash

# Developed by Sameera K. Abeykoon (MArch 19th 2018)

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

# make directory for asl data analysis
mkdir /mnt/hcp01/scR21_asl/asl_results/$sub_num/
# make directory for cortical parcellation
echo "Make subject number dir in cortical_par folder and asl_results"
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

# change to asl directory
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
        if [ -e T1w_MPR_s003.nii ]
        then
           cp T1w_MPR_s003.nii /mnt/hcp01/scR21_asl/cortical_par/$sub_num/day_$i.nii
           mv T1w_MPR_s003.nii Anat/
        elif [ -e T1w_MPR_norm.nii ]
        then
           cp T1w_MPR_norm.nii /mnt/hcp01/scR21_asl/cortical_par/$sub_num/day_$i.nii
           mv T1w_MPR_norm.nii Anat/
        else
           echo " Missing T1w_MPR_norm.nii or T1w_MPR_s003.nii data"
        fi


        # move the ASL and REF data files to those folders
        mv *REF* ./Ref
        mv *pCASL* ./Asl
        cd ..
done    

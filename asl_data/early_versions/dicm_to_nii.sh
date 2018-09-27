#!/bin/bash

echo Enter the Subject number
read sub_num

echo Enter First date DICOM data directory
read data1

echo Enter Second date DICOM data directory
read data2

echo Enter Third date DICOM data directory
read data3

data_list="$data1 $data2 $data3"
arr=($data_list)
echo $data_list

current_path="$pwd"
cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
echo $PWD
for i in {1..3};do
        echo /mnt/hcp01/nii_folder/$sub_num/day_$i
        echo ${arr[$((i-1))]}
	/mnt/jxvs01/pipelines/HCP/usr/local/MATLAB/R2016b/bin/matlab -nodisplay -r "dicm2nii('/mnt/jxvs01/incoming/Smoking_Cessation_Abi_Dargham/${arr[$((i-1))]}', '/mnt/hcp01/nii_folder/$sub_num/day_$i', 0); quit"
done

cd $current_path
echo $PWD

rm *Resting*
rm *SpinEchoFieldMap*
rm *field_map*

#mkdir Anat ASL REF
mkdir /mnt/hcp01/scR21_asl/cortical_par/$sub_num

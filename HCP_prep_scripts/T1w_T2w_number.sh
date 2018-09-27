#      Developed by Sameera Abeykoon
#      to rename T1w and T2w folders

echo "Enter the subject number example:50070 ?"
read sub_num

echo "Enter the subject dirctory path example: /mnt/hcp01/RDoC/50070 ? "
read sub_path

cd ${sub_path}/unprocessed/3T

#mv T1w* tmp
#mv T2w* tmp

# get the T1w and T2w data folders to an array
T1_array=($(find . -maxdepth 1 -type d -name "*T1w*"))
T2_array=($(find . -maxdepth 1 -type d -name "*T2w*"))

# get the number of T1w and T2w folders 
t1=${#T1_array[@]}
t2=${#T2_array[@]}

# go inside the tmp folder
cd tmp_T1w_T2w

# get the T1w and T2w data folders to an array
tmp_T1=($(find . -maxdepth 1 -type d -name "*T1w*"))
tmp_T2=($(find . -maxdepth 1 -type d -name "*T2w*"))

if [ ${#tmp_T1[@]} -eq 0 ]; then
	for i in "${tmp_T1[@]}"; do :
		cd ${i}
        	echo $PWD

        	let "t1++"
        	readarray -t array <<< "$(find . -maxdepth 1 -type f -name "*T1w*")"
        	file=${array[0]}

        	#file = ($(find . -maxdepth 1 -type f -name "*T1w*"))
        	mv ${file} ${sub_num}_3T_T1w_MPR${t1}.nii.gz
        
        	cd ../
        	echo $PWD
        	mkdir T1w_MPR${t1}
        	mv ${i}/* T1w_MPR${t1}
        	#rm -rf ${i}
	done
fi

if [ ${#tmp_T2[@]} -eq 0 ]; then
	for j in "${tmp_T2[@]}"; do :
        	cd ${j}
        	echo $PWD

        	let "t2++"
        	readarray -t array <<< "$(find . -maxdepth 1 -type f -name "*T2w*")"
        	file=${array[0]}
        	#file = ($(find . -maxdepth 1 -type f -name "*T1w*"))
        	mv ${file} ${sub_num}_3T_T2w_SPC${t2}.nii.gz

        	cd ../
        	echo $PWD
        	mkdir T2w_SPC${t2}
        	mv ${j}/* T2w_SPC${t2}
        	rm -rf ${j}

	done
fi
mv T1w* ../
mv T2w* ../

cd ../
rm -rf tmp_T1w_T2w

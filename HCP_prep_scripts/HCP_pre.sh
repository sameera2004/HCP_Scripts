# Developed by Sameera K. Abeykoon
#  This will run follwing HCP scripts to convert DICOM's to nii data
#  HCP_anatomy_prep.csh
#  HCP_fielmap_prep.csh and HCP_fMRI_prep.csh

echo "How many data collection sessions eg : 1 or 2 "?
read s_num
echo "Number of sessions :" ${s_num}

for ((i=1;i<=${s_num};i++)); do
	echo Enter the params file Eg : S3531_P32_JV_HCP_prep_script.params
	read params_file

	# get the anatomy data
	csh HCP_anatomy_prep.csh ${params_file}

	# get the fieldmap data
	csh HCP_fieldmap_prep.csh ${params_file}

	# get the fMRI data
	csh HCP_fMRI_prep.csh ${params_file}
        if [ ${s_num} -eq 2 ]; then
            if [ ${i} -eq 1 ]; then
            	sh T1w_T2w_mv_tmp.sh
            else 
                sh T1w_T2w_number.sh
            fi
        fi

#              Developed by Sameera K. Abeykoon
#  	       This will run the HCP_2_fieldmap_prep.csh 
#   	       HCP_2_fMRI_prep.csh  scripts to convert DICOM's to nii

echo Enter the params file Eg : S3531_P32_JV_HCP_prep_script.params
read params_file

# get the fieldmap data
csh HCP_2_fieldmap_prep.csh ${params_file}

# get the fMRI data
csh HCP_2_fMRI_prep.csh ${params_file}

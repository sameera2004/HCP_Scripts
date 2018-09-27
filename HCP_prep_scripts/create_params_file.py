"""
	Developed By: Sameera Abeykoon
	This will create the HCP params(example:
	S3071_V15_AAD_HCP_prep_script.params)
	input file for follwoing 3 c-shell scripts
	HCP_anatomy_prep.csh
	HCP_fieldMap_prep.csh  
	HCP_fMRI_prep.csh
""" 
import io
import sys
import os

# subject number example : 50022
# subject directory full path /mnt/hcp01/tnfcs/50022

# Enter the full path to the DICOM files, which copied from the
# SCAN_center 
# example /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3060_JV
#dcm_dir = raw_input("Enter the incoming data directory full path ? ")

# Enter the full path to the final data analysed folder"
#subjdir = raw_input("Enter the final subject directory(processed data) full path ? ")

def params_file(dcm_dir, subjdir):
    subjid = os.path.basename(subjdir)

    # get the data id given from the SCAN_center
    data_id = os.path.basename(dcm_dir)

    # get the current directory path
    cwd = os.getcwd()

    # save these details to the HCP_prep.params file
    f = open(data_id + "_HCP_prep_script.params", "w")

    f.write("set subjid = "+subjid+"\n")
    f.write("set subjdir = "+subjdir+"\n")
    f.write("set xnat_dir = "+dcm_dir+"\n")
    f.write("set dcm_dir = "+dcm_dir+"\n")
    f.write("set nii_dir = "+dcm_dir+"\n")
    f.write("set scanlog = "+cwd+"/"+data_id+"_scanlog.txt\n")
    f.write("set xnatmode = 0\n")
    f.write("set slicetime = 0\n")
    
    f.name
    print (data_id + "_HCP_prep_script.params\n")

    f.close()
    return

if __name__ == "__main__":
     subjdir = sys.argv[1]
     print ("Subject dir :" , subjdir)

     dcm_dir = sys.argv[2]
     print ("Dicom dir : " , dcm_dir)

     params_file(dcm_dir, subjdir)

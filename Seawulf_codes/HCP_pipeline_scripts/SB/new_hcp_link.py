"""
    Developed by : Sameera Abeykoon (June 11 2018)
    This script will save the NYSPI incoming correct fMRI data into correct folders
    The correct data maybe in /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/"subject_number"/nii
    eg : /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/3045/nii
    or MUX folder inside the subject number s ../XNAT_K01/horgconte/2264/12589/scans/10/MUX
"""

from __future__ import print_function
import numpy as np
import os, sys

# provide the Subject numbers
s_number=input("Enter the subject number ?")

# final Subject folder inside hcp01/tnfcs_PI
s_folder = s_number 

# get the Nifti data folders
#nii_path = "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" + s_number+ "/nii/" # get the dicm2nii nii.gz files

# scanlog file 
scan_file = s_number + "_scanlog.txt"
scan_folder = "/gpfs/projects/VanSnellenbergGroup/S_codes/scanlog/" + scan_file

# final unprocessed data folder
dest_path="/gpfs/scratch/sabeykoon/HCP_data/nyspi/" + s_folder + "/unprocessed/3T/"

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_folder, delimiter=" ", dtype=str, unpack=True)

# get the scanlog file unpacked data
for i, j in enumerate(s_data[4]):
    if 'fMRI' in j or 'T1w' in j or 'T2w' in j:
        # get the folder B0 filenumber  scanlog file (eg : 1)
        B0_no = s_data[6][i]
        
        B0_file = s_number + "_3T_GradientEchoFieldMap_" + str(B0_no) + ".nii.gz"
        
        dst = dest_path + "FieldMap/" + B0_file
        print ("dst", dst)
       
        print ("++++++++++++++++++++++++++++++++")
        src = dest_path + j  + "/" + s_number + "_3T_GradientEchoFieldMap.nii.gz"
        print ("src", src)
        
        fd_path = dest_path + j
        if os.path.isdir(fd_path):
        	if os.path.lexists(src):
          		os.remove(src)
        	os.symlink(dst, src)

    
	

from __future__ import print_function
import os, time, string
import dicom
import sys
import numpy as np

# Developed By Sameera K. Abeykoon (March , 2018)
# This will provide the filename(protocal name) and th
# folder name and if it's T1w or T2w it will provide the 
# more detils to use in scanlog text

#  Please provide the path to the data directory
# example: ipython create_scanlog_SB.py /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3046_V26_JV

# topdir=/mnt/jxvs01/incoming/JVS_K01_VanSnellenberg
# tobedone=S3046_V26_JV

path = sys.argv[1]

topdir,tobedone = os.path.split(path)
print ("Incoming data directory path", topdir)   
print ("Subject data directory ", tobedone)

# Files can come with different file extension
# DICOM has .dcm or .IMA
f_ext = (".dcm", ".IMA", ".ima")

c_folder = [ ]

for i in np.sort(os.listdir(path)):
        
        #if current_dir == topdir and i not in tobedone:
        #    continue
        # print ("Up folder name ", i)
        if os.path.isdir(path+"/"+i):
            print ("Current folder ", (path+"/"+i))
                        
            for fname in os.listdir(path+"/"+i):
                    if fname.endswith(tuple(f_ext)):
                        next_level = path + "/" + i + "/" + fname 
                        break
       
            splitup = next_level.split('/')
            
            list_no = len(os.listdir(path + "/" + i))
            print ("Number of files", list_no)

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            #TR = dcmhdr['0018', '0080'].value # Repetition Time
            #TE = dcmhdr['0018', '0081'].value # Echo Time
            
            # filename given example: fMRI_Resting_1_AP, T1W_MPR
            print ("filename", filename)
            #print ("Repetition Time  TR ", TR)
            #print ("Echo Time TE ", TE)
            
            # DICOM directory name (long number)
            mapoutname = str(splitup[6])
            print ("folder number", mapoutname)
            if 'T2w_SPC' in filename:
                a = float(dcmhdr['0019','1018'].value)/100000000 
                c = "%.6f" % (a)
                print ("c value ", c)

            if 'T1w_MPR' in filename:
                 a = float(dcmhdr['0019','1018'].value)/100000000
                 c = "%.6f" % (a)
                 print ("c value ", c)


            print ("+++++++++++++++++++++++++++++++++++++++")

"""
    Developed by : Sameera Abeykoon (June 11 2018)
    To fix the correct fielmap and T1w numbers - Two sessions
"""

from __future__ import print_function
import numpy as np
import os, sys
import pickle

# enter the first session scanlong file
scan1 = raw_input("Enter the 1st session scanlog file ?")

scan2 = raw_input("Enter the 2nd session scanlog file ?")

# unpack the scanlog txt file
s_data = np.genfromtxt(scan1, delimiter=" ", dtype=str, unpack=True)
s_data2 = np.genfromtxt(scan2, delimiter=" ", dtype=str, unpack=True)

spin_no = s_data[5][-1]

b0_no = s_data[6][-1]

for i, j in enumerate(s_data2[0]):
    print (s_data2[4][i])
    if 'Topup' in s_data2[4][i]:
        #print ("Topup")
        s_data2[5][i] = int(s_data2[5][i]) + int(spin_no)
    elif 'fieldmap' in s_data2[4][i]:
        #print ("fieldmap")
        s_data2[5][i] = int(s_data2[5][i]) + int(b0_no)
        #opup' not in s_data2[4][i] or 'fieldmap' not in s_data2[4][i]:
    else:
        #print ("fMRI")
        s_data2[5][i] = int(s_data2[5][i]) + int(spin_no)
        s_data2[6][i] = int(s_data2[6][i]) + int(b0_no)
    
cwd = os.getcwd() 
                   
#file_name = "/mnt/jxvs01/pipelines/HCP/HCP_prep/SB_prep/" + scan2
file_name = cwd + "/" + scan2
os.remove(file_name)

# save these details to the new sacnlog file
f = open(file_name, "w")

for i, j in enumerate(s_data2[0]):
    f.write(s_data2[0][i] + ' ' + s_data2[1][i] + ' ' + s_data2[2][i] + ' ' + s_data2[3][i] + ' ' + s_data2[4][i] + ' ' + s_data2[5][i] + ' ' + s_data2[6][i]+ ' ' + s_data2[7][i] + "\n" )

f.close()
            

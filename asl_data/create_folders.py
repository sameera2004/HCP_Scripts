"""
     Developed by : Sameera K. Abeykoon (January 2018)

     This will create folders for ASL data processing and
     Cortial Parcellation for all three days for rTMS study
    
     Reqiured to give the Subject number and the directory path
     Example:
     ipython create_folders.py 50024 /mnt/hcp01/scR21_asl
"""
     
from __future__ import print_function
import sys
import io
import os

def make_dir(my_path,subno):
    asl_path = my_path+"/asl_results/"+subno
    cor_path = my_path+"/cortical_par/"+subno
    if not os.path.isdir(asl_path):
        os.makedirs(asl_path)
    if not os.path.isdir(cor_path):
        os.makedirs(cor_path)
    for i in (asl_path, cor_path):
        os.makedirs(i+"/day_1")
        os.makedirs(i+"/day_2")
        os.makedirs(i+"/day_3")

if __name__ == "__main__":
    subno=sys.argv[1]
    print ("Subject number = ",subno)

    my_path = sys.argv[2]
    
    print (my_path)
    make_dir(my_path, subno)



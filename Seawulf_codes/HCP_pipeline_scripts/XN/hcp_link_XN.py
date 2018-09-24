from __future__ import print_function
import os
import sys

if len(sys.argv) > 1:
        s_list = sys.argv[1]
else:
        s_list = input("Enter the subject numbers as a list eg: [50045, 50056] " )

# provide the Subject numbers list
#s_list = input("Enter subject number eg:[0194, 2264] :? ")

s_list = eval(s_list)

for s_folder in s_list:
    # final data folder
    fd_folder = "/mnt/hcp01/tnfcs_PI/" + str(s_folder) + "/unprocessed/3T"
    new_folder = "/gpfs/scratch/sabeykoon/HCP_data/nyspi/" + str(s_folder) + "/unprocessed/3T"
    for l_dir in os.listdir(new_folder):
        if 'fMRI' in l_dir:
            l_path = new_folder + "/" + l_dir
            os.chdir(l_path)
            for f in os.listdir('.'):
                  if 'GradientEchoFieldMap' in f:
                         target = os.readlink(f)

                         t_1, t_2 = os.path.split(target)

                         # This creates a symbolic link on python in tmp directory
                         dst = new_folder + "/FieldMap/" + t_2
                         src = new_folder + "/" + l_dir + "/" + f
                         os.unlink(src)
                         os.symlink(src, dst)

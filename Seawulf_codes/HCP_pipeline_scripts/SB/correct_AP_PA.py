"""

	Developed by : Sameera Abeykoon
	This will create the fMRI.txt file - with list of fMRI tasks
        and AP_PA.txt file - with fMRI list with correct AP and PA 

"""

from __future__ import print_function
import numpy as np
import os, sys

def appa_fmri(scan_file, sub_no):	
    # unpack the scanlog txt file
    s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

    # Get a new filename to create AP and PA directions
    #filename = os.path.splitext(os.path.basename(scan_file))[0] + "_fMRI.txt"
    #ap_pa_file = os.path.splitext(os.path.basename(scan_file))[0] + "_AP_PA.txt"
    filename = sub_no + "_fMRI.txt"
    ap_pa_file = sub_no + "_AP_PA.txt"

    if os.path.exists(filename): os.remove(filename)
    if os.path.exists(ap_pa_file): os.remove(ap_pa_file)

    #  Write the fMRI data folder list
    with open(filename, 'a') as the_file:
    #        the_file.write(scan_file)
    #        the_file.write('\n')
            for i, j in enumerate(s_data[4]):
                 #if "fMRI" in j and not j.endswith("SBRef"):
                 if "fMRI" in j and "SBRef" not in j:
                        the_file.write(j)
                        the_file.write('\n')

    # Write the AP or PA direction of the FMRI data
    ap_file = open(ap_pa_file, "w")
    ap_file.write("# " + scan_file)
    ap_file.write('\n')
    for i, j in enumerate(s_data[4]):
    	if "fMRI" in j and "SBRef" not in j:
        	if int(s_data[7][i]) == 1:
                         ap_file.write(j + " " + "PA"+ '\n')
                else:
                         ap_file.write(j + " " + "AP" + '\n')
    return


if __name__ == "__main__":
   appa_fmri(scan_file, sub_no)
   # Enter the scanlog file name
   #scan_file = sys.argv[1]


#           Developed By: Sameera Abeykoon
       
#          This will create the params file and the scanlog files 
#          from the DICOM folders

# Enter the full path to the final data analysed folder (/mnt/hcp01/?)"
echo "Enter the final subject directory(processed data) full path ? "
read subjdir
echo "Final sub directory " ${subjdir}

echo "How many data collection sessions eg : 1 or 2 "?
read s_num
echo "Number of sessions :" ${s_num}

for ((i=1;i<=${s_num};i++)); do
        # Enter the full path to the DICOM files, which copied from the
        # SCAN_center 
        # example /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3060_JV
        echo "Enter the incoming data directory full path ? "
        read dcm_path
        echo "Dicom path :" ${dcm_path}
        # create params file
        #python create_params_file.py "params_file(${dcm_path}, ${subjdir})"
        python create_params_file.py ${subjdir} ${dcm_path}

	tobedone=${dcm_path##*/}
        topdir=${dcm_path%/*}

        echo "Subject data directory  " ${tobedone}

        # creating correct scanlog file
        project=${topdir##*/}

        python create_scanlog_wm.py ${dcm_path}
        #fi
done
  
if [ "$s_num" -eq 2 ];then
    python scanlog_number_fix_2_sessions.py
fi     

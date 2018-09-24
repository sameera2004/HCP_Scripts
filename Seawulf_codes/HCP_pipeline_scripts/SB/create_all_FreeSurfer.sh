#           Developed By: Sameera Abeykoon

#          This will create all the PreFreeSurfer, FreeSurfer, PostFreeSurfer
#          Scripts to process HCP structural data

module load shared
module load anaconda/2

# Enter the full path to data folder "
echo "Subject data path  eg: /gpfs/projects/VanSnellenbergGroup/SB_HCP_data " 
read datapath

# Enter the subject data dirctory [50068, 50089]
echo Enter the Subject number list eg:50045,50067
read -a sub_list
echo ${sub_list[*]}

#echo Enter the Subject number 50045
#read sub_list

#for Subjlist in "${sub_list[@]}"; do :;
# This will create PreFreeSurfer 
python create_PreFreeSurfer.py ${datapath} \[${sub_list[*]}\]  
#python create_PreFreeSurfer.py ${datapath} ${sub_list} 
       
# This will create FreeSufer
python create_FreeSurfer.py ${datapath} \[${sub_list[*]}\]
#python create_FreeSurfer.py ${datapath} ${sub_list}

# This will create PostFreeSufer
python create_PostFreeSurfer.py ${datapath} \[${sub_list[*]}\]
#python create_PostFreeSurfer.py ${datapath} ${sub_list}


#done

# 

# Developed by Sameera Abeykoon
# to rename T1w and T2w folders

echo "Enter the subject dirctory path example:/mnt/hcp01/RDoC/50070 ? "
read sub_path

cd ${sub_path}/unprocessed/3T
echo "Make the tmp_T1w_T2w folder"
mkdir tmp_T1w_T2w

mv T1w* tmp_T1w_T2w
mv T2w* tmp_T1w_T2w

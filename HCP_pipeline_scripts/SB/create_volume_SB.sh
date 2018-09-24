#  Developed by Sameera K. Abeykoon
# This will create all the Volume processing scripts

module load shared 
module load anaconda/2

python volume_SB_para.py

sh volume_subjob.sh
#python volume_subjob.py

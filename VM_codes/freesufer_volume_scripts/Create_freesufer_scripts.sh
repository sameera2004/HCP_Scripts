#########################################################

#        Developed by Sameera Abeykoon                  #
#        to create FreesuferPipeline_Batch sh           #

##########################################################

echo "Enter the subject dirctory path example:/mnt/hcp01/RDoC/50070 ? "
read sub_path

# get the basename for the subject dir
dir="${sub_path##*/}"
echo ${dir}

# get the dir name for the study
study="${sub_path%/*}"
echo ${study}

cp PreFreeSurferPipelineBatch_SB_AAD.sh PreFreeSurferPipelineBatch_SB_${dir}_AAD.sh
cp FreeSurferPipelineBatch_SB_AAD.sh FreeSurferPipelineBatch_SB_${dir}_AAD.sh
cp PostFreeSurferPipelineBatch_SB_AAD.sh PostFreeSurferPipelineBatch_SB_${dir}_AAD.sh

replace "Datadir" "${study}" -- PreFreeSurferPipelineBatch_SB_${dir}_AAD.sh FreeSurferPipelineBatch_SB_${dir}_AAD.sh PostFreeSurferPipelineBatch_SB_${dir}_AAD.sh
replace "Final_subject" "${dir}" -- PreFreeSurferPipelineBatch_SB_${dir}_AAD.sh FreeSurferPipelineBatch_SB_${dir}_AAD.sh PostFreeSurferPipelineBatch_SB_${dir}_AAD.sh


#sed -i -e 's/Datadir/'"$study"'/g' PreFreeSurferPipelineBatch_SB_${dir}_AAD.sh
#awk '{gsub(/Final_subject/,"${dir}")}' PreFreeSurferPipelineBatch_SB_${dir}_AAD.sh

#sed -i -e 's/Datadir/'"$study"'/g' FreeSurferPipelineBatch_SB_${dir}_AAD.sh
#sed -i -e 's/Final_subject/'"$dir"'/g' FreeSurferPipelineBatch_SB_${dir}_AAD.sh

#sed -i -e 's/Datadir/'"$study"'/g' PostFreeSurferPipelineBatch_SB_${dir}_AAD.sh
#sed -i -e 's/Final_subject/'"$dir"'/g' PostFreeSurferPipelineBatch_SB_${dir}_AAD.sh

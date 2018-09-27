#!/bin/tcsh
#edited by Aniqa for nyspi mri cluster

# Version 1.0 10/2/14 Gaurav Patel
# Converts non-multiband fMRI dicoms and places in appropriate HCP unprocessed directory.
# Then links appropriate spin echo/topup and gradient echo/B0fieldmap based on columns 6 and 7 in use_scan log
# Assumes existance of use_scan.log in subjdir, structured and named as follows (no header line)
#Scan number   GE_dicom_number   Time   Sequence_Name   Scan_Label              topup   b0fieldmap
#  1             s737            12:00  [from console]   T1w_MPR_1		1	1
#  2             s738            12:05  [from console]   T1w_MPR_2		1	1
#  3             s739            12:10  [from console]   T2w_SPC_1		1	1
#  4             s740            12:15  [from console]   RS_fMRI_1		1	1
#  5             s741            12:20  [from console]   Topup_AP		1
#  6             s742            12:25  [from console]   Topup_PA		1
#  7             s743            12:30  [from console]   Task_fMRI_faceplace_1  1       1
#  8             s744            12:35  [from console]   Task_fMRI_faceplace_2  1       1
#  9             s745            12:40  [from console]   B0_fieldmap		1
#
# Script should be able to handle arbitrary numbers of each scan type
# Types that will be processed are currently T1w_MPR, T2w_SPC, and fMRI.

set HCP_vers = 3_4
set HCP_dir = /mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples
set HCP_scripts_dir = ${HCP_dir}/subj_scripts_${HCP_vers}

set program = $0; set program = $program:t

if (${#argv} < 1) then
        echo "usage:    "$program" params_file"
        exit 1
endif

set params = $1
source $params

mkdir -p ${subjdir}/unprocessed
mkdir -p ${subjdir}/unprocessed/3T
mkdir -p scripts

# CONVERT DCM 2 NII AND PLACE fMRI DATA INTO HCP FILE STRUCTURE
set scanTypes = (fMRI)
foreach y (`echo $scanTypes`)
	set labelList = `cat $scanlog | grep $y | grep -v Topup | awk '{print $5}'`
	set dcmList = `cat $scanlog | grep $y | grep -v Topup | awk '{print $2}'`
        set topupList = `cat $scanlog | grep $y | grep -v Topup | awk '{print $6}'`
        set b0List = `cat $scanlog | grep $y | grep -v Topup | awk '{print $7}'`
	@ numscans = ${#dcmList}
	@ x = 1

	foreach currscan (`echo $labelList`)

		echo $currscan

		if ($currscan =~ *"SBRef") then 
		    set tempname = `echo $currscan | rev | cut -c 7- | rev`
		    set outdir =  ${subjdir}/unprocessed/3T/${tempname}
		else
		    set outdir =  ${subjdir}/unprocessed/3T/${currscan}		
		endif		

		if (! -d "$outdir") then
		    mkdir $outdir
		endif
		    
                if ( $xnatmode == 0 ) then
                        set dcm1 = `echo ${dcm_dir}/${dcmList[$x]}/* | awk '{print $1}'`
                else if ( $xnatmode == 1 ) then
                        set dcm1 = `echo ${xnat_dir}/${dcmList[$x]}/DICOM/* | awk '{print $1}'`
                else
                        set dcm1 = `echo ${xnat_dir}/${dcmList[$x]}/resources/DICOM/files/* | awk '{print $1}'`
                endif

		dcm2nii -a y -r n -x n -d n -e y -f n -g n -o ${outdir} ${dcm1} >! niitmp
		set niipath = `cat niitmp | grep Saving | awk '{print $2}'`
		mv $niipath ${outdir}/${subjid}_3T_${currscan}.nii
		pigz_mricron -f ${outdir}/${subjid}_3T_${currscan}.nii
		rm niitmp >& tmp

                set topupscan = ${topupList[$x]}
                foreach s ( AP PA )
			rm ${outdir}/${subjid}_3T_SpinEchoFieldMap_${s}.nii.gz >& tmp
                        ln -s ${subjdir}/unprocessed/3T/FieldMap/${subjid}_3T_SpinEchoFieldMap_${s}_${topupscan}.nii.gz ${outdir}/${subjid}_3T_SpinEchoFieldMap_${s}.nii.gz
                end

                set b0scan = ${b0List[$x]}
                echo $b0List[$x]
		rm ${outdir}/${subjid}_3T_GradientEchoFieldMap.nii.gz >& tmp
                ln -s ${subjdir}/unprocessed/3T/FieldMap/${subjid}_3T_GradientEchoFieldMap_${b0scan}.nii.gz ${outdir}/${subjid}_3T_GradientEchoFieldMap.nii.gz

                #set b0scan = ${b0List[$x]}
		#foreach s ( Magnitude Phase )
		#    rm ${outdir}/${subjid}_3T_GradientEchoFieldMap_${s}.nii.gz >& tmp
		#    ln -s ${subjdir}/unprocessed/3T/FieldMap/${subjid}_3T_GradientEchoFieldMap_${s}_${b0scan}.nii.gz ${outdir}/${subjid}_3T_GradientEchoFieldMap_${s}.nii.gz
		#end

		@ x = $x + 1
	end
end
rm tmp

#!/bin/tcsh
# edited by Aniqa for nyspi mri cluster

# Version 1.0 10/2/14 Gaurav Patel
# Converts fieldmap dicoms, numbers according to use scan log column 6,  and places in appropriate HCP unprocessed directory
# Assumes existance of use_scan.log in subjdir, structured and named as follows (no header line)
#Scan number   GE_dicom_number   Time   Sequence_Name   Scan_Label              topup   b0fieldmap
#  1             s737            12:00  [from console]   T1w_MPR_1		1	1
#  2             s738            12:05  [from console]   T1w_MPR_2		1	1
#  3             s739            12:10  [from console]   T2w_SPC_1		1	1
#  4             s740            12:15  [from console]   RS_fMRI		1	1
#  5             s741            12:20  [from console]	 Topup_AP 		1	
#  6             s742            12:25	[from console]	 Topup_PA		1	
#  7             s743            12:30  [from console]   Task_fMRI_faceplace_1	1	1
#  8             s744            12:35  [from console]   Task_fMRI_faceplace_2	1	1
#  9		 s745		 12:50	[from console]   B0_fieldmap		1
#
# Script should be able to handle arbitrary numbers of each scan type
# Types that will be processed are currently T1w_MPR, T2w_SPC, and fMRI.
set HCP_vers = 3_4
set HCP_dir = /mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples
set HCP_scripts_dir = ${HCP_dir}/Scripts

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

# CONVERT B0/TOPUP DCM 2 NII AND PLACE IN FIELDMAP DIR
set scanTypes = ( B0_fieldmap Topup_AP Topup_PA )
foreach y (`echo $scanTypes`)

	if ( $y == B0_fieldmap ) then 
		set scanname = GradientEchoFieldMap
	else if ( $y == Topup_AP ) then
		set scanname = SpinEchoFieldMap_AP
	else if ( $y == Topup_PA ) then
		set scanname = SpinEchoFieldMap_PA
	endif

        set outdir =  ${subjdir}/unprocessed/3T/FieldMap
        mkdir -p $outdir

	set dcmList = `cat $scanlog | grep $y | awk '{print $2}'`
	set mapList = `cat $scanlog | grep $y | awk '{print $6}'`
        @ numscans = ${#dcmList}
        @ x = 1
        while ($x <= $numscans)
		if ( $xnatmode == 0 ) then
                        set dcm1 = `echo ${dcm_dir}/${dcmList[$x]}/* | awk '{print $1}'`
                else if ( $xnatmode == 1 ) then
                        set dcm1 = `echo ${xnat_dir}/${dcmList[$x]}/DICOM/* | awk '{print $1}'`
		else    
                        set dcm1 = `echo ${xnat_dir}/${dcmList[$x]}/resources/DICOM/files/* | awk '{print $1}'`
                endif
		set mapnum = ${mapList[$x]}
#                echo "mri_convert -rt cubic -it dicom --out_orientation RAS ${dcm1} ${outdir}/${subjid}_3T_${scanname}_${mapnum}.nii.gz" >! scripts/mri_convert_${scanname}_${mapnum}.sh 
		
		dcm2nii -4 y -a y -r n -x n -d n -e y -f n -g n -o ${outdir} ${dcm1} >! niitmp
		set niipath = `cat niitmp | grep Saving | awk '{print $2}'`
		
		if ( $y == Topup_AP ||  $y == Topup_PA ) then
                        cp $niipath ${outdir}/2_${subjid}_3T_${scanname}_${mapnum}.nii
			pigz_mricron -f ${outdir}/2_${subjid}_3T_${scanname}_${mapnum}.nii
                        rm $niipath
                else if ( $y == B0_fieldmap ) then
                        mv $niipath ${outdir}/2_${subjid}_3T_${scanname}_${mapnum}.nii
                        pigz_mricron -f ${outdir}/2_${subjid}_3T_${scanname}_${mapnum}.nii
                endif
	#	rm niitmp
#                chmod 775 scripts/mri_convert_${scanname}_${mapnum}.sh
#                at -f scripts/mri_convert_${scanname}_${mapnum}.sh now
                @ x = $x + 1
        end
end

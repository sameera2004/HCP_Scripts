"""
Developed by Sameera Abeykoon

exampe: ipython create_PreFreeSurfer.py

"""
from __future__ import print_function
import os
import sys
from builtins import input

if len(sys.argv) > 1:
	data_path = sys.argv[1]
        sub_no = sys.argv[2]
else:
	data_path = input("Enter the data directory path eg:/gpfs/projects/VanSnellenbergGroup/SB_HCP_data " )
	sub_no = input("Enter the subject numbers as a list eg: [50045, 50056] " )

sub_no = eval(sub_no)
print ("Subject numbers ", sub_no)

y = []
g = []

for i in sub_no:
    u = str(i).strip()
    y.append(u)
    v = "PreFreeSurferPipelineBatch_" + str(u) + ".sh"
    g.append(open(v,'w'))

for i in range(len(y)):
    g[i].write("#!/bin/bash\n") 

    g[i].write("#~ND~FORMAT~MARKDOWN~\n")
    g[i].write("#~ND~START~\n")
    
    g[i].write("# # PreFreeSurferPipelineBatch.sh\n")
    
    g[i].write("# ## Copyright Notice\n")
    
    g[i].write("# Copyright (C) 2013-2016 The Human Connectome Project\n")
    
    g[i].write("# * Washington University in St. Louis\n")
    g[i].write("# * University of Minnesota\n")
    g[i].write("# * Oxford University\n")
    """
    # ## Author(s)
    #
    # * Matthey F. Glasser, Department of Anatomy and Neurobiology, 
    #   Washington University in St. Louis
    # * Timothy B. Brown, Neuroinformatics Research Group,
    #   Washington University in St. Louis
    #
    # ## Product
    #
    # [Human Connectome Project][HCP] (HCP) Pipelines
    #
    # ## License
    #
    # See the [LICENSE](https://github.com/Washington-University/Pipelines/blob/master/LICENSE.md) file
    #
    # ## Description:
    #
    # Example script for running the Pre-FreeSurfer phase of the HCP Structural 
    # Preprocessing pipeline
    #
    # See [Glasser et al. 2013][GlasserEtAl].
    #
    # ## Prerequisites
    #
    # ### Installed software
    #
    # * FSL (version 5.0.6)
    # * FreeSurfer (version 5.3.0-HCP)
    # * gradunwarp (HCP version 1.0.2) - if doing gradient distortion correction
    #
    # ### Environment variables
    #
    # Should be set in script file pointed to by EnvironmentScript variable.
    # See setting of the EnvironmentScript variable in the main() function
    # below.
    #
    # * FSLDIR - main FSL installation directory
    # * FREESURFER_HOME - main FreeSurfer installation directory
    # * HCPPIPEDIR - main HCP Pipelines installation directory
    # * CARET7DIR - main Connectome Workbench installation directory
    # * PATH - must point to where gradient_unwarp.py is if doing gradient unwarping
    #
    # <!-- References -->
    # [HCP]: http://www.humanconnectome.org
    # [GlasserEtAl]: http://www.ncbi.nlm.nih.gov/pubmed/23668970
    #
    #~ND~END~

    # Function: get_batch_options
    # Description
    # 
    #   Retrieve the following command line parameter values if specified
    #  
    #   --StudyFolder= - primary study folder containing subject ID subdirectories
    #   --Subjlist=    - quoted, space separated list of subject IDs on which
    #                    to run the pipeline
    #   --runlocal     - if specified (without an argument), processing is run
    #                    on "this" machine as opposed to being submitted to a
    #                    computing grid
    #
    #   Set the values of the following global variables to reflect command
    #   line specified parameters
    #
    #   command_line_specified_study_folder
    #   command_line_specified_subj_list
    #   command_line_specified_run_local
    #
    #   These values are intended to be used to override any values set 
    #   directly within this script file"""

    g[i].write("get_batch_options() {\n")
    g[i].write("   local arguments=(\"$@\")\n")

    g[i].write("    unset command_line_specified_study_folder\n")
    g[i].write("    unset command_line_specified_subj\n")
    g[i].write("    unset command_line_specified_run_local\n")

    g[i].write("    local index=0\n")
    g[i].write("    local numArgs=${#arguments[@]}\n")
    g[i].write("    local argument\n")

    g[i].write("    while [ ${index} -lt ${numArgs} ]; do\n")
    g[i].write("        argument=${arguments[index]}\n")

    g[i].write("        case ${argument} in\n")
    g[i].write("            --StudyFolder=*)\n")
    g[i].write("               command_line_specified_study_folder=${argument#*=}\n")
    g[i].write("               index=$(( index + 1 ))\n")
    g[i].write("               ;;\n")
    g[i].write("            --Subject=*)\n")
    g[i].write("               command_line_specified_subj=${argument#*=}\n")
    g[i].write("               index=$(( index + 1 ))\n")
    g[i].write("               ;;\n")
    g[i].write("            --runlocal)\n")
    g[i].write("               command_line_specified_run_local=\"TRUE\"\n")
    g[i].write("               index=$(( index + 1 ))\n")
    g[i].write("               ;;\n")
    g[i].write("            *)\n")
    g[i].write("               echo \"\"\n")
    g[i].write("               echo \"ERROR: Unrecognized Option: ${argument}\"\n")
    g[i].write("               echo \"\"\n")
    g[i].write("               exit 1\n")
    g[i].write("               ;;\n")
    g[i].write("       esac\n")
    g[i].write("    done\n")
    g[i].write("}\n")

    """# Function: main
    # Description: main processing work of this script"""
    g[i].write("main()\n")
    g[i].write("{\n")
    g[i].write("    get_batch_options \"$@\"\n")

    g[i].write("    # Set variable values that locate and specify data to process\n")
    g[i].write("    StudyFolder=\"" + data_path + "\" # Location of Subject folders (named by subjectID)\n")
    g[i].write("    Subjlist=\"" + str(y[i]) + "\"\n")
    g[i].write("    # Space delimited list of subject IDs\n")

    g[i].write("    # Set variable value that set up environment\n")
    g[i].write("    EnvironmentScript=\"/gpfs/software/Pipelines-3.24.0/Examples/Scripts/SetUpHCPPipeline.sh\" # Pipeline environment script\n")

    g[i].write("    # Use any command line specified options to override any of the variable settings above\n")
    g[i].write("    if [ -n \"${command_line_specified_study_folder}\" ]; then\n")
    g[i].write("         StudyFolder=\"${command_line_specified_study_folder}\"\n")
    g[i].write("    fi\n")

    g[i].write("    if [ -n \"${command_line_specified_subj}\" ]; then\n")
    g[i].write("         Subjlist=\"${command_line_specified_subj}\"\n")
    g[i].write("    fi\n")

    g[i].write("    # Report major script control variables to user\n")
    g[i].write("    echo \"StudyFolder: ${StudyFolder}\"\n")
    g[i].write("    echo \"Subjlist: ${Subjlist}\"\n")
    g[i].write("    echo \"EnvironmentScript: ${EnvironmentScript}\"\n")
    g[i].write("    # echo \"Run locally: ${command_line_specified_run_local}\"\n")

    g[i].write("    # Set up pipeline environment variables and software \")")
    g[i].write("    source ${EnvironmentScript}\n")

    """     # Define processing queue to be used if submitted to job scheduler
            # if [ X$SGE_ROOT != X ] ; then
            #    QUEUE="-q long.q"
            #    QUEUE="-q veryshort.q
            #QUEUE="-q long"
            #echo "$QUEUE"
            # fi

        # If PRINTCOM is not a null or empty string variable, then
        # this script and other scripts that it calls will simply
        # print out the primary commands it otherwise would run.
        # This printing will be done using the command specified
        # in the PRINTCOM variable
        # PRINTCOM=""
        # PRINTCOM="echo"

        #
        # Inputs:
        #
        # Scripts called by this script do NOT assume anything about the form of the
        # input names or paths. This batch script assumes the HCP raw data naming 
        # convention, e.g.
        #
        # ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_T1w_MPR1.nii.gz
        # ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR2/${Subject}_3T_T1w_MPR2.nii.gz
        #
        # ${StudyFolder}/${Subject}/unprocessed/3T/T2w_SPC1/${Subject}_3T_T2w_SPC1.nii.gz
        # ${StudyFolder}/${Subject}/unprocessed/3T/T2w_SPC2/${Subject}_3T_T2w_SPC2.nii.gz
        #
        # ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_FieldMap_Magnitude.nii.gz
        # ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_FieldMap_Phase.nii.gz

        # Scan settings:
        #
        # Change the Scan Settings (e.g. Sample Spacings and $UnwarpDir) to match your 
        # structural images. These are set to match the HCP-YA ("Young Adult") Protocol by default.
        # (i.e., the study collected on the customized Connectom scanner).

        # Readout Distortion Correction:
        # 
        # You have the option of using either gradient echo field maps or spin echo
        # field maps to perform readout distortion correction on your structural
        # images, or not to do readout distortion correction at all.
        #
        # The HCP Pipeline Scripts currently support the use of gradient echo field 
        # maps or spin echo field maps as they are produced by the Siemens Connectom 
        # Scanner. They also support the use of gradient echo field maps as generated
        # by General Electric scanners.
        # 
        # Change either the gradient echo field map or spin echo field map scan 
        # settings to match your data. This script is setup to use gradient echo 
        # field maps from the Siemens Connectom Scanner collected using the HCP-YA Protocol.

        # Gradient Distortion Correction:
        #
        # If using gradient distortion correction, use the coefficents from your 
        # scanner. The HCP gradient distortion coefficents are only available through
        # Siemens. Gradient distortion in standard scanners like the Trio is much 
        # less than for the HCP Connectom scanner."""

        # DO WORK """

    g[i].write("    #Cycle through specified subjects\n")
    g[i].write("    for Subject in $Subjlist ; do\n")
    g[i].write("            echo $Subject\n")

    g[i].write("            # Input Images\n")

    g[i].write("            # Detect Number of T1w Images and build list of full paths to \n")
    g[i].write("            # T1w images\n")
    g[i].write("            numT1ws=`ls ${StudyFolder}/${Subject}/unprocessed/3T | grep 'T1w_MPR.$' | wc -l`\n")
    g[i].write("            echo \"Found ${numT1ws} T1w Images for subject ${Subject}\"\n")
    g[i].write("            T1wInputImages=\"\"\n")
    g[i].write("            i=1\n")
    g[i].write("            while [ $i -le $numT1ws ] ; do\n")
    g[i].write("                    T1wInputImages=`echo \"${T1wInputImages}${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR${i}/${Subject}_3T_T1w_MPR${i}.nii.gz@\"`\n")
    g[i].write("                    i=$(($i+1))\n")
    g[i].write("            done\n")

    g[i].write("            # Detect Number of T2w Images and build list of full paths to\n")
    g[i].write("            # T2w images\n")
    g[i].write("            numT2ws=`ls ${StudyFolder}/${Subject}/unprocessed/3T | grep 'T2w_SPC.$' | wc -l`\n")
    g[i].write("            echo \"Found ${numT2ws} T2w Images for subject ${Subject}\"\n")
    g[i].write("            T2wInputImages=\"\"\n")
    g[i].write("            i=1\n")
    g[i].write("            while [ $i -le $numT2ws ] ; do\n")
    g[i].write("                    T2wInputImages=`echo \"${T2wInputImages}${StudyFolder}/${Subject}/unprocessed/3T/T2w_SPC${i}/${Subject}_3T_T2w_SPC${i}.nii.gz@\"`\n")
    g[i].write("                    i=$(($i+1))\n")
    g[i].write("            done\n")

    """            # Readout Distortion Correction:
                #
                #   Currently supported Averaging and readout distortion correction 
                #   methods: (i.e. supported values for the AvgrdcSTRING variable in this
                #   script and the --avgrdcmethod= command line option for the 
                #   PreFreeSurferPipeline.sh script.)
                #
                #   "NONE"
                #     Average any repeats but do no readout distortion correction
                #
                #   "FIELDMAP"
                #     This value is equivalent to the "SiemensFieldMap" value described
                #     below. Use of the "SiemensFieldMap" value is prefered, but 
                #     "FIELDMAP" is included for backward compatibility with the versions
                #     of these scripts that only supported use of Siemens-specific 
                #     Gradient Echo Field Maps and did not support Gradient Echo Field 
                #     Maps from any other scanner vendor.
                #
                #   "TOPUP"
                #     Average any repeats and use Spin Echo Field Maps for readout 
                #     distortion correction
                #
                #   "GeneralElectricFieldMap"
                #     Average any repeats and use General Electric specific Gradient 
                #     Echo Field Map for readout distortion correction
                #
                #   "SiemensFieldMap"
                #     Average any repeats and use Siemens specific Gradient Echo 
                #     Field Maps for readout distortion correction
                #
                # Current Setup is for Siemens specific Gradient Echo Field Maps
                #
                #   The following settings for AvgrdcSTRING, MagnitudeInputName, 
                #   PhaseInputName, and TE are for using the Siemens specific 
                #   Gradient Echo Field Maps that are collected and used in the 
                #   standard HCP-YA protocol.  
                #
                #   Note: The AvgrdcSTRING variable could also be set to the value 
                #   "FIELDMAP" which is equivalent to "SiemensFieldMap"."""
    g[i].write("            AvgrdcSTRING=\"TOPUP\"\n")

    """            # ----------------------------------------------------------------------
                # Variables related to using Siemens specific Gradient Echo Field Maps
                # ----------------------------------------------------------------------

                # The MagnitudeInputName variable should be set to a 4D magitude volume
                # with two 3D timepoints or "NONE" if not used
                # MagnitudeInputName="${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_FieldMap_Magnitude.nii.gz" """
    g[i].write("            MagnitudeInputName=\"NONE\"\n")

    """           # The PhaseInputName variable should be set to a 3D phase difference 
                # volume or "NONE" if not used
                # PhaseInputName="${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_FieldMap_Phase.nii.gz" """
    g[i].write("            PhaseInputName=\"NONE\"\n")

    """           # The TE variable should be set to 2.46ms for 3T scanner, 1.02ms for 7T
                # scanner or "NONE" if not using
                # TE="2.46" """
    g[i].write("            TE=\"NONE\"\n")

    """         # ----------------------------------------------------------------------
                # Variables related to using Spin Echo Field Maps
                # ----------------------------------------------------------------------

                # The following variables would be set to values other than "NONE" for
                # using Spin Echo Field Maps (i.e. when AvgrdcSTRING="TOPUP")

                # The SpinEchoPhaseEncodeNegative variable should be set to the 
                # spin echo field map volume with a negative phase encoding direction
                # (LR if using a pair of LR/RL Siemens Spin Echo Field Maps (SEFMs);
                # AP if using a pair of AP/PA Siemens SEFMS)
                # and set to "NONE" if not using SEFMs
                # (i.e. if AvgrdcSTRING is not equal to "TOPUP")
                #
                # Example values for when using Spin Echo Field Maps from a Siemens machine:
                #   ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_LR.nii.gz
                #   ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_AP.nii.gz
                # SpinEchoPhaseEncodeNegative="NONE" """
    g[i].write("            SpinEchoPhaseEncodeNegative=\"${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_AP.nii.gz\"\n")

    """         # The SpinEchoPhaseEncodePositive variable should be set to the 
                # spin echo field map volume with positive phase encoding direction
                # (RL if using a pair of LR/RL SEFMs; PA if using a AP/PA pair),
                # and set to "NONE" if not using Spin Echo Field Maps
                # (i.e. if AvgrdcSTRING is not equal to "TOPUP")
                # 
                # Example values for when using Spin Echo Field Maps from a Siemens machine:
                #   ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_RL.nii.gz
                #   ${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_PA.nii.gz
                # SpinEchoPhaseEncodePositive="NONE" """
    g[i].write("            SpinEchoPhaseEncodePositive=\"${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_SpinEchoFieldMap_PA.nii.gz\"\n")
    """         # Echo Spacing or Dwelltime of spin echo EPI MRI image. Specified in seconds.
                # Set to "NONE" if not used. 
                # 
                # Dwelltime = 1/(BandwidthPerPixelPhaseEncode * # of phase encoding samples)
                # DICOM field (0019,1028) = BandwidthPerPixelPhaseEncode
                # DICOM field (0051,100b) = AcquisitionMatrixText first value (# of phase encoding samples).
                # On Siemens, iPAT/GRAPPA factors have already been accounted for.
                #
                # Example value for when using Spin Echo Field Maps:
                #   0.000580002668012 """
    g[i].write("            DwellTime=\"0.00059\"\n")

    """         # Spin Echo Unwarping Direction
                # x or y (minus or not does not matter)
                # "NONE" if not used
                # 
                # Example values for when using Spin Echo Field Maps: x, -x, y, -y
                # Note: +x or +y are not supported. For positive values, DO NOT include the + sign
                ## MPH: Why do we say that "minus or not does not matter", but then list -x and -y as example values??"""
    g[i].write("            SEUnwarpDir=\"y\"\n")

    """         # Topup Configuration file
                # "NONE" if not used
                # TopupConfig="/mnt/jxvs01/pipelines/HCP/usr/local/fsl/src/topup/flirtsch/b02b0.cnf" """
    g[i].write("            TopupConfig=\"/gpfs/projects/VanSnellenbergGroup/S_codes/b02b0.cnf\"\n")

    """         # ----------------------------------------------------------------------
                # Variables related to using General Electric specific Gradient Echo 
                # Field Maps
                # ----------------------------------------------------------------------

                # The following variables would be set to values other than "NONE" for
                # using General Electric specific Gradient Echo Field Maps (i.e. when 
                # AvgrdcSTRING="GeneralElectricFieldMap")

                # Example value for when using General Electric Gradient Echo Field Map
                #
                # GEB0InputName should be a General Electric style B0 fieldmap with two 
                # volumes
                #   1) fieldmap in deg and
                #   2) magnitude, 
                # set to NONE if using TOPUP or FIELDMAP/SiemensFieldMap
                #
                #   GEB0InputName="${StudyFolder}/${Subject}/unprocessed/3T/T1w_MPR1/${Subject}_3T_GradientEchoFieldMap.nii.gz" """
    g[i].write("            GEB0InputName=\"NONE\"\n")

    g[i].write("            # Templates\n")
    g[i].write("            # Hires T1w MNI template\n")
    g[i].write("            T1wTemplate=\"${HCPPIPEDIR_Templates}/MNI152_T1_0.7mm.nii.gz\"\n")

    g[i].write("            # Hires brain extracted MNI template\n")
    g[i].write("            T1wTemplateBrain=\"${HCPPIPEDIR_Templates}/MNI152_T1_0.7mm_brain.nii.gz\"\n")

    g[i].write("            # Lowres T1w MNI template\n")
    g[i].write("            T1wTemplate2mm=\"${HCPPIPEDIR_Templates}/MNI152_T1_2mm.nii.gz\"\n")

    g[i].write("            # Hires T2w MNI Template\n")
    g[i].write("            T2wTemplate=\"${HCPPIPEDIR_Templates}/MNI152_T2_0.7mm.nii.gz\"\n")

    g[i].write("            # Hires T2w brain extracted MNI Template\n")
    g[i].write("            T2wTemplateBrain=\"${HCPPIPEDIR_Templates}/MNI152_T2_0.7mm_brain.nii.gz\"\n")

    g[i].write("            # Lowres T2w MNI Template\n")
    g[i].write("            T2wTemplate2mm=\"${HCPPIPEDIR_Templates}/MNI152_T2_2mm.nii.gz\"\n")

    g[i].write("            # Hires MNI brain mask template\n")
    g[i].write("            TemplateMask=\"${HCPPIPEDIR_Templates}/MNI152_T1_0.7mm_brain_mask.nii.gz\"\n")

    g[i].write("            # Lowres MNI brain mask template\n")                
    g[i].write("            Template2mmMask=\"${HCPPIPEDIR_Templates}/MNI152_T1_2mm_brain_mask_dil.nii.gz\"\n")

    g[i].write("            # Structural Scan Settings\n") 
    g[i].write("            #\n")
    g[i].write("            # Note that \"UnwarpDir\" is the *readout* direction of the *structural* (T1w,T2w)\n")
    g[i].write("            # images, and should not be confused with \"SEUnwarpDir\" which is the *phase* encoding direction\n")
    g[i].write("            # of the Spin Echo Field Maps (if using them).\n")
    g[i].write("            #\n")
    g[i].write("            # set all these values to NONE if not doing readout distortion correction\n")
    g[i].write("            # \n")
    g[i].write("            # Sample values for when using General Electric structurals\n")
    g[i].write("            #   T1wSampleSpacing=\"0.000011999\" # For General Electric scanners, 1/((0018,0095)*(0028,0010))\n")
    g[i].write("            #   T2wSampleSpacing=\"0.000008000\" # For General Electric scanners, 1/((0018,0095)*(0028,0010))\n")
    g[i].write("            #   UnwarpDir=\"y\"  ## MPH: This doesn't seem right. Is this accurate??\n")

    g[i].write("            # The values set below are for the HCP-YA Protocol using the Siemens \n")
    g[i].write("            # Connectom Scanner\n")

    g[i].write("            # DICOM field (0019,1018) in s or \"NONE\" if not used\n")
    g[i].write("            T1wSampleSpacing=\"0.0000074\"\n")

    g[i].write("            # DICOM field (0019,1018) in s or \"NONE\" if not used\n")
    g[i].write("            T2wSampleSpacing=\"0.0000021\"\n")

    g[i].write("            # z appears to be the appropriate polarity for the 3D structurals collected on Siemens scanners\n")
    g[i].write("            # or \"NONE\" if not used\n")
    g[i].write("            UnwarpDir=\"z\"\n")

    g[i].write("            # Other Config Settings\n")

    g[i].write("            # BrainSize in mm, 150 for humans\n")
    g[i].write("            BrainSize=\"150\"\n")

    g[i].write("            # FNIRT 2mm T1w Config\n")
    g[i].write("            FNIRTConfig=\"${HCPPIPEDIR_Config}/T1_2_MNI152_2mm.cnf\"\n")

    g[i].write("            # Location of Coeffs file or \"NONE\" to skip\n")
    g[i].write("            # GradientDistortionCoeffs=\"${HCPPIPEDIR_Config}/coeff_SC72C_Skyra.grad\"\n") 

    g[i].write("            # Set to NONE to skip gradient distortion correction\n")
    g[i].write("            GradientDistortionCoeffs=\"NONE\"\n")

    """         ###############################################################################################
                #  Modified not to use queue command in this script

                # Establish queuing command based on command line option 
                #if [ -n "${command_line_specified_run_local}" ] ; then
                #       echo "About to run ${HCPPIPEDIR}/PreFreeSurfer/PreFreeSurferPipeline.sh"
                # queuing_command="qsub ${QUEUE} -N PFS_50018"
                #elsea
                #       echo "About to use fsl_sub to queue or run ${HCPPIPEDIR}/PreFreeSurfer/PreFreeSurferPipeline.sh"
                #       queuing_command="${FSLDIR}/bin/fsl_sub ${QUEUE}"
                #fi

                # Run (or submit to be run) the PreFreeSurferPipeline.sh script
                # with all the specified parameter values"""

    g[i].write("            sh /gpfs/software/Pipelines-3.24.0/PreFreeSurfer/PreFreeSurferPipeline.sh \\\n")
    g[i].write("                    --path=\"$StudyFolder\" \\\n")
    g[i].write("                    --subject=\"$Subject\" \\\n")
    g[i].write("                    --t1=\"$T1wInputImages\" \\\n")
    g[i].write("                    --t2=\"$T2wInputImages\" \\\n")
    g[i].write("                    --t1template=\"$T1wTemplate\" \\\n")
    g[i].write("                    --t1templatebrain=\"$T1wTemplateBrain\" \\\n")
    g[i].write("                    --t1template2mm=\"$T1wTemplate2mm\" \\\n")
    g[i].write("                    --t2template=\"$T2wTemplate\" \\\n")
    g[i].write("                    --t2templatebrain=\"$T2wTemplateBrain\" \\\n")
    g[i].write("                    --t2template2mm=\"$T2wTemplate2mm\" \\\n")
    g[i].write("                    --templatemask=\"$TemplateMask\" \\\n")
    g[i].write("                    --template2mmmask=\"$Template2mmMask\" \\\n")
    g[i].write("                    --brainsize=\"$BrainSize\" \\\n")
    g[i].write("                    --fnirtconfig=\"$FNIRTConfig\" \\\n")
    g[i].write("                    --fmapmag=\"$MagnitudeInputName\" \\\n")
    g[i].write("                    --fmapphase=\"$PhaseInputName\" \\\n")
    g[i].write("                    --fmapgeneralelectric=\"$GEB0InputName\" \\\n")
    g[i].write("                    --echodiff=\"$TE\" \\\n")
    g[i].write("                    --SEPhaseNeg=\"$SpinEchoPhaseEncodeNegative\" \\\n")
    g[i].write("                    --SEPhasePos=\"$SpinEchoPhaseEncodePositive\" \\\n")
    g[i].write("                    --echospacing=\"$DwellTime\" \\\n")
    g[i].write("                    --seunwarpdir=\"$SEUnwarpDir\" \\\n")
    g[i].write("                    --t1samplespacing=\"$T1wSampleSpacing\" \\\n")
    g[i].write("                    --t2samplespacing=\"$T2wSampleSpacing\" \\\n")
    g[i].write("                    --unwarpdir=\"$UnwarpDir\" \\\n")
    g[i].write("                    --gdcoeffs=\"$GradientDistortionCoeffs\" \\\n")
    g[i].write("                    --avgrdcmethod=\"$AvgrdcSTRING\" \\\n")
    g[i].write("                    --topupconfig=\"$TopupConfig\" \\\n")
    g[i].write("                    --printcom=$PRINTCOM\n")

    g[i].write("    done\n")
    g[i].write("}\n")

    g[i].write("# Invoke the main function to get things started\n")
    g[i].write("main \"$@\"\n")
    print (" Created PreFreeSurferPipelineBatch_" + str(y[i]) + ".sh\n\n")

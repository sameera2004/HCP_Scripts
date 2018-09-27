from __future__ import print_function
import os
import sys
import io
"""

Modified by Sameera Abeykoon on January 2018

exampe: ipython volume_SB.py /mnt/hcp01/tnfcs
"""

#current_dir = sys.argv[1]

current_dir = raw_input("Enter final subject dir eg: /mnt/hcp01/RDoC :")
print (current_dir)

g = []

x = raw_input("Enter the Subject number as a list eg [50058, 50068] :")
x = eval(x)

#x = open('list_of_subjects_SB.txt','r')
y = []

for i in x:
    u = str(i).strip()
    y.append(u)
    v = "GenericfMRIVolumeProcessingPipelineBatch_" + str(u) + ".sh"
    g.append(open(v,'w'))
    

for i in range(len(y)):
    z = current_dir + '/' +  str(y[i]) + '/unprocessed/3T'
    print (z)
    g[i].write("#!/bin/bash\n")
    g[i].write("get_batch_options() {\n")
    g[i].write("    local arguments=(\"$@\")\n")
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
    g[i].write("                command_line_specified_study_folder=${argument#*=}\n")
    g[i].write("                index=$(( index + 1 ))\n")
    g[i].write("                ;;\n")
    g[i].write("            --Subject=*)\n")
    g[i].write("                command_line_specified_subj=${argument#*=}\n")
    g[i].write("                index=$(( index + 1 ))\n")
    g[i].write("                ;;\n")
    g[i].write("            --runlocal)\n")
    g[i].write("                command_line_specified_run_local=\"TRUE\"\n")
    g[i].write("                index=$(( index + 1 ))\n")
    g[i].write("                ;;\n")
    g[i].write("	    *)\n")
    g[i].write("		echo \"\"\n")
    g[i].write("		echo \"ERROR: Unrecognized Option: ${argument}\"\n")
    g[i].write("		echo \"\"\n")
    g[i].write("		exit 1\n")
    g[i].write("		;;\n")
    g[i].write("        esac\n")
    g[i].write("    done\n")
    g[i].write("}\n")
    g[i].write("get_batch_options \"$@\"\n")
    g[i].write("StudyFolder=\""+ current_dir+"\"\n")

    g[i].write("Subjlist=\"" + str(y[i]) + "\"\n")

    g[i].write("EnvironmentScript=\"${XHOME}/projects/Pipelines/Examples/Scripts/SetUpHCPPipeline.sh\"\n")
    g[i].write("if [ -n \"${command_line_specified_study_folder}\" ]; then\n")
    g[i].write("    StudyFolder=\"${command_line_specified_study_folder}\"\n")
    g[i].write("fi\n")
    g[i].write("if [ -n \"${command_line_specified_subj}\" ]; then\n")
    g[i].write("    Subjlist=\"${command_line_specified_subj}\"\n")
    g[i].write("fi\n")
    g[i].write("source ${EnvironmentScript}\n")
    g[i].write("echo \"$@\"\n")
    g[i].write("QUEUE=\"-q hcp_priority.q\"\n")
    g[i].write("if [[ -n $HCPPIPEDEBUG ]]\n")
    g[i].write("then\n")
    g[i].write("    set -x\n")
    g[i].write("fi\n")
    g[i].write("PRINTCOM=\"\"\n")
    g[i].write("Tasklist=\"\"\n")
    g[i].write("PhaseEncodinglist=\"\"\n")

    xx = []

    for j in os.listdir(z):
        if ('T1w_MPR' in j) or ('T2w_SPC' in j) or ('FieldMap' in j):
            continue

        xx. append(j)

    xx.sort()

    for j in xx:
        g[i].write("Tasklist=\"${Tasklist} " + j  + "\"\n")
        print (j[-1:])
        if int(j[-1])%2:
                 g[i].write("PhaseEncodinglist=\"${PhaseEncodinglist} y-\"\n")
                 # print "int odd"
        else:
                 g[i].write("PhaseEncodinglist=\"${PhaseEncodinglist} y\"\n")
                 #print "int even"
        """
        if (j[-1:]).isdigit():
           if int(j[-1])%2:
                 g[i].write("PhaseEncodinglist=\"${PhaseEncodinglist} y-\"\n")
                 print "int odd"
            else:
                 g[i].write("PhaseEncodinglist=\"${PhaseEncodinglist} y\"\n")
                 print "int even"
        else:
            g[i].write("PhaseEncodinglist=\"${PhaseEncodinglist} y+\"\n")
            print "str"
        """
            
    g[i].write("TaskArray=($Tasklist)\n")
    g[i].write("PhaseEncodingArray=($PhaseEncodinglist)\n")
    g[i].write("nTaskArray=${#TaskArray[@]}\n")
    g[i].write("nPhaseEncodingArray=${#PhaseEncodingArray[@]}\n")
    g[i].write("if [ \"${nTaskArray}\" -ne \"${nPhaseEncodingArray}\" ] ; then\n")
    g[i].write("    echo \"Tasklist and PhaseEncodinglist do not have the same number of elements.\"\n")
    g[i].write("    echo \"Exiting without processing\"\n")
    g[i].write("    exit 1\n")
    g[i].write("fi\n")
    g[i].write("for Subject in $Subjlist ; do\n")
    g[i].write("  echo $Subject\n")
    g[i].write("  i=1\n")
    g[i].write("  for fMRIName in $Tasklist ; do\n")
    g[i].write("    echo \"  ${fMRIName}\"\n")
    g[i].write("    UnwarpDir=`echo $PhaseEncodinglist | cut -d \" \" -f $i`\n")

    g[i].write("    fMRITimeSeries=\"${StudyFolder}/${Subject}/unprocessed/3T/${fMRIName}/${Subject}_3T_${fMRIName}.nii.gz\"  \n")
    g[i].write("    fMRISBRef=\"${StudyFolder}/${Subject}/unprocessed/3T/${fMRIName}/${Subject}_3T_${fMRIName}_SBRef.nii.gz\"\n")

    g[i].write("    DwellTime=\"0.00059\"\n")
    g[i].write("    DistortionCorrection=\"TOPUP\"\n")
    g[i].write("    BiasCorrection=\"SEBASED\"\n")
    g[i].write("    SpinEchoPhaseEncodeNegative=\"${StudyFolder}/${Subject}/unprocessed/3T/${fMRIName}/${Subject}_3T_SpinEchoFieldMap_AP.nii.gz\"\n")
    g[i].write("    SpinEchoPhaseEncodePositive=\"${StudyFolder}/${Subject}/unprocessed/3T/${fMRIName}/${Subject}_3T_SpinEchoFieldMap_PA.nii.gz\"\n")
    g[i].write("    MagnitudeInputName=\"NONE\"\n")
    g[i].write("    PhaseInputName=\"NONE\"\n")
    g[i].write("    GEB0InputName=\"NONE\"\n")
    g[i].write("    DeltaTE=\"NONE\"\n")
    g[i].write("    FinalFMRIResolution=\"2\"\n")
    g[i].write("    GradientDistortionCoeffs=\"NONE\"\n")
    g[i].write("    TopUpConfig=\"${HCPPIPEDIR_Config}/b02b0.cnf\"\n")
    g[i].write("    MCType=\"MCFLIRT\"\n")
    g[i].write("    if [ -n \"${command_line_specified_run_local}\" ] ; then\n")
    g[i].write("        echo \"About to run ${HCPPIPEDIR}/fMRIVolume/GenericfMRIVolumeProcessingPipeline.sh\"\n")
    g[i].write("        queuing_command=\"\"\n")
    g[i].write("    else\n")
    g[i].write("        echo \"About to use fsl_sub to queue or run ${HCPPIPEDIR}/fMRIVolume/GenericfMRIVolumeProcessingPipeline.sh\"\n")
    g[i].write("        queuing_command=\"${FSLDIR}/bin/fsl_sub ${QUEUE}\"\n")
    g[i].write("    fi\n")
    g[i].write("    ${queuing_command} ${HCPPIPEDIR}/fMRIVolume/GenericfMRIVolumeProcessingPipeline.sh \\\n")
    g[i].write("      --path=$StudyFolder \\\n")
    g[i].write("      --subject=$Subject \\\n")
    g[i].write("      --fmriname=$fMRIName \\\n")
    g[i].write("      --fmritcs=$fMRITimeSeries \\\n")
    g[i].write("      --fmriscout=$fMRISBRef \\\n")
    g[i].write("      --SEPhaseNeg=$SpinEchoPhaseEncodeNegative \\\n")
    g[i].write("      --SEPhasePos=$SpinEchoPhaseEncodePositive \\\n")
    g[i].write("      --fmapmag=$MagnitudeInputName \\\n")
    g[i].write("      --fmapphase=$PhaseInputName \\\n")
    g[i].write("      --fmapgeneralelectric=$GEB0InputName \\\n")
    g[i].write("      --echospacing=$DwellTime \\\n")
    g[i].write("      --echodiff=$DeltaTE \\\n")
    g[i].write("      --unwarpdir=$UnwarpDir \\\n")
    g[i].write("      --fmrires=$FinalFMRIResolution \\\n")
    g[i].write("      --dcmethod=$DistortionCorrection \\\n")
    g[i].write("      --gdcoeffs=$GradientDistortionCoeffs \\\n")
    g[i].write("      --topupconfig=$TopUpConfig \\\n")
    g[i].write("      --printcom=$PRINTCOM \\\n")
    g[i].write("      --biascorrection=$BiasCorrection \\\n")
    g[i].write("      --mctype=${MCType}\n")
    g[i].write("  echo \"set -- --path=$StudyFolder \\\n")
    g[i].write("      --subject=$Subject \\\n")
    g[i].write("      --fmriname=$fMRIName \\\n")
    g[i].write("      --fmritcs=$fMRITimeSeries \\\n")
    g[i].write("      --fmriscout=$fMRISBRef \\\n")
    g[i].write("      --SEPhaseNeg=$SpinEchoPhaseEncodeNegative \\\n")
    g[i].write("      --SEPhasePos=$SpinEchoPhaseEncodePositive \\\n")
    g[i].write("      --fmapmag=$MagnitudeInputName \\\n")
    g[i].write("      --fmapphase=$PhaseInputName \\\n")
    g[i].write("      --fmapgeneralelectric=$GEB0InputName \\\n")
    g[i].write("      --echospacing=$DwellTime \\\n")
    g[i].write("      --echodiff=$DeltaTE \\\n")
    g[i].write("      --unwarpdir=$UnwarpDir \\\n")
    g[i].write("      --fmrires=$FinalFMRIResolution \\\n")
    g[i].write("      --dcmethod=$DistortionCorrection \\\n")
    g[i].write("      --gdcoeffs=$GradientDistortionCoeffs \\\n")
    g[i].write("      --topupconfig=$TopUpConfig \\\n")
    g[i].write("      --printcom=$PRINTCOM \\\n")
    g[i].write("      --biascorrection=$BiasCorrection \\\n")
    g[i].write("      --mctype=${MCType}\"\n")
    g[i].write("  echo \". ${EnvironmentScript}\"\n")
    g[i].write("    i=$(($i+1))\n")
    g[i].write("  done\n")
    g[i].write("done\n")

    g[i].close()



























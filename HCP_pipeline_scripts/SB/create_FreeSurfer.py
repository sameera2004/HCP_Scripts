"""
Developed by Sameera Abeykoon

exampe: ipython create_FreeSurfer.py

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

print ("Subject numbers", sub_no)
sub_no = eval(sub_no)
print ("Subject numbers", sub_no)

y = []
g = []

for i in sub_no:
    u = str(i).strip()
    y.append(u)
    v = "FreeSurferPipelineBatch_" + str(u) + ".sh"
    g.append(open(v,'w'))

for i in range(len(y)):
    g[i].write("#!/bin/bash\n\n") 
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

    g[i].write("\n\n")
    g[i].write("get_batch_options \"$@\"\n")

    g[i].write("#Set variable values that locate and specify data to process\n")
    g[i].write("StudyFolder=\"" + data_path + "\" # Location of Subject folders (named by subjectID)\n")
    g[i].write("Subjlist=\"" + str(y[i]) + "\"\n")
    g[i].write("# Space delimited list of subject IDs\n")

    g[i].write("# Set variable value that set up environment\n")
    g[i].write("EnvironmentScript=\"/gpfs/software/Pipelines-3.24.0/Examples/Scripts/SetUpHCPPipeline.sh\" # Pipeline environment script\n")

    g[i].write("# Use any command line specified options to override any of the variable settings above\n")
    g[i].write("if [ -n \"${command_line_specified_study_folder}\" ]; then\n")
    g[i].write("      StudyFolder=\"${command_line_specified_study_folder}\"\n")
    g[i].write("fi\n")

    g[i].write("if [ -n \"${command_line_specified_subj}\" ]; then\n")
    g[i].write("      Subjlist=\"${command_line_specified_subj}\"\n")
    g[i].write("fi\n")

    g[i].write("    # Set up pipeline environment variables and software \")\n")
    g[i].write("    source ${EnvironmentScript}\n")

    """
    ########################################## INPUTS ########################################## 

    #Scripts called by this script do assume they run on the outputs of the PreFreeSurfer Pipeline

    ######################################### DO WORK ##########################################

    """
    g[i].write("#Cycle through specified subjects\n")
    g[i].write("for Subject in $Subjlist ; do\n")
    g[i].write("     echo $Subject\n")
    g[i].write("     #Input Variables\n")
    g[i].write("     SubjectID=\"$Subject\" #FreeSurfer Subject ID Name\n")
    g[i].write("     SubjectDIR=\"${StudyFolder}/${Subject}/T1w\" #Location to Put FreeSurfer Subject's Folder\n")
    g[i].write("     T1wImage=\"${StudyFolder}/${Subject}/T1w/T1w_acpc_dc_restore.nii.gz\" #T1w FreeSurfer Input (Full Resolution)\n")
    g[i].write("     T1wImageBrain=\"${StudyFolder}/${Subject}/T1w/T1w_acpc_dc_restore_brain.nii.gz\" #T1w FreeSurfer Input (Full Resolution)\n")
    g[i].write("     T2wImage=\"${StudyFolder}/${Subject}/T1w/T2w_acpc_dc_restore.nii.gz\" #T2w FreeSurfer Input (Full Resolution)\n")

    g[i].write("     sh /gpfs/software/Pipelines-3.24.0/FreeSurfer/FreeSurferPipeline.sh \\\n")
    g[i].write("        --subject=\"$Subject\" \\\n")
    g[i].write("        --path=\"$StudyFolder\" \\\n")
    g[i].write("        --t1=\"$T1wImage\" \\\n")
    g[i].write("        --t1brain=\"$T1wImageBrain\" \\\n")
    g[i].write("        --t2=\"$T2wImage\" \\\n")
    g[i].write("        --printcom=$PRINTCOM \n")                                

    g[i].write("    # The following lines are used for interactive debugging to set the positional parameters: $1 $2 $3 ...\n")

    g[i].write("    echo \"set -- --subject=\"$Subject\" \\\n")
    g[i].write("        --path=\"$StudyFolder\" \\\n")
    g[i].write("        --t1=\"$T1wImage\" \\\n")
    g[i].write("        --t1brain=\"$T1wImageBrain\" \\\n")
    g[i].write("        --t2=\"$T2wImage\" \\\n")
    g[i].write("        --printcom=$PRINTCOM\"\n")

    g[i].write("    echo \".${EnvironmentScript}\"\n")
    g[i].write("done\n")
    print (" Created FreeSurferPipelineBatch_" + str(y[i]) + ".sh\n\n")

    
   

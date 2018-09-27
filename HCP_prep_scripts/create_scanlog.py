from __future__ import print_function
import os, time, string
import dicom
import sys

# Modified By Sameera K. Abeykoon (January , 2018)

#  Please provide the path to the data directory
# example: ipython create_scanlog_SB.py /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3046_V26_JV

# topdir=/mnt/jxvs01/incoming/JVS_K01_VanSnellenberg
# tobedone=S3046_V26_JV

path = sys.argv[1]

topdir,tobedone = os.path.split(path)
print ("Incoming data directory path", topdir)   
print ("Subject data directory ", tobedone)

current_dir = topdir
past_dir = topdir
alldir = []

allstudy = []
allstring = []

mapoutlist = []
mapoutcont = []
mapouttype = []
mapoutlabel = []
mapoutsnum = []
mapoutextra = []

allfunc = []
allb0 = []
allap = []
allpa = []
allt1 = []
allt2 = []

while os.path.isdir(current_dir):
    breakout = 0
    for i in os.listdir(current_dir):

        if current_dir == topdir and i not in tobedone:
            continue
        next_level = current_dir + '/' + i
        if os.path.isdir(next_level):
            if next_level in alldir:
                continue
            else:
                past_dir = current_dir
                current_dir = next_level
                breakout = 1
                break
        elif next_level.endswith('.dcm'):

            splitup = next_level.split('/')

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            
            # filename given example: fMRI_Resting_1_AP, T1W_MPR
            print (filename)
            # print (dcmhdr['0020','0011'].value)
            
            # DICOM directory name (long number)
            mapoutname = str(splitup[6])
            # print ("mapout_name", mapoutname)
            studyname = str(splitup[5])

            if studyname not in allstudy:
                allstudy.append(studyname)
                allstring.append([])

            if studyname not in mapoutlist:
                mapoutlist.append(studyname)
                mapoutcont.append([])
                mapouttype.append([])
                mapoutlabel.append([])
                mapoutsnum.append([])
                mapoutextra.append([])

            mapindex = mapoutlist.index(studyname)

            if 'SpinEchoFieldMap_PA' in filename:

                a = float(dcmhdr['0019','1028'].value)
                b = float(str(dcmhdr['0051','100b'].value).split('*')[0])
                c = "%.15f" % (1/(a*b))
                # print (a, b, c)

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('Topup_PA')
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(c)
                                                
            elif 'SpinEchoFieldMap_AP' in filename:

                a = float(dcmhdr['0019','1028'].value)
                b = float(str(dcmhdr['0051','100b'].value).split('*')[0])
                c = "%.15f" % (1/(a*b))
                print (a, b,c)

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('Topup_AP')
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(c)

            elif 'T2w_SPC' in filename:

                a = float(dcmhdr['0019','1018'].value)/100000000 
                c = "%.6f" % (a)

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('T2w_SPC_')
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(c)

            elif 'T1w_MPR' in filename and len(filename) == 7:
                
                a = float(dcmhdr['0019','1018'].value)/100000000 
                c = "%.6f" % (a)

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('T1w_MPR_')
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(c)

            elif 'SBRef' in filename:

                aa = filename.split('_')
                # print ("aa", aa)
                
                if 'Resting' in aa:
                    a = 'RSFC'
                elif 'thalloc' in aa:
                    a = 'THL'
                elif 'PSD' in aa:
                    a = 'PSD'
                elif 'SOT' in aa:
                    a = 'SO'
                elif (a[-2])[:-1]=='MB':
                    a  = 'MB'
                
                if 'PA' in aa:
                    b = 'PA'
                elif 'AP' in aa:
                    b= 'AP'
                else:
                    print ("File is not AP or PA")

                c = filter(lambda x: x.isdigit(), filename)

                mapoutcont[mapindex].append(filenum)
                # print (a + '_fMRI_' + b + '_SBRef_' + str(c))
                if a == 'MB':
                   mapouttype[mapindex].append(a + '_fMRI_' + '_SBRef_' + str(c)) 
                else:
                   mapouttype[mapindex].append(a + '_fMRI_' + str(c) + '_SBRef_' + b)
           
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(0)

            elif 'fMRI' or 'FMRI' in filename and 'field' not in filename:

                aa = filename.split('_')

                if 'Resting' in aa:
                    a = 'RSFC'
                elif 'thalloc' in aa:
                    a = 'THL'
                elif 'PSD' in aa:
                    a = 'PSD'
                elif 'SOT' in aa:
                    a = 'SO'
                elif (aa[-1])[:-1]=='MB':
                    a  = 'MB'
                
                if 'PA' in aa:
                    b = 'PA'
                elif 'AP' in aa:
                    b= 'AP'
                else:
                    print ("File is not AP or PA")

                # get the digit fromthe filename
                c = filter(lambda x: x.isdigit(), filename)
                
                mapoutcont[mapindex].append(filenum)
                # print (a + '_fMRI_' + str(c) + '_' + b)
                if a == 'MB':
                   mapouttype[mapindex].append(a +'_fMRI_' + str(c)) 
                else:
                   mapouttype[mapindex].append(a + '_fMRI_' + str(c) +  '_' + b)
                mapoutlabel[mapindex].append(filename)
                mapoutsnum[mapindex].append(mapoutname)
                mapoutextra[mapindex].append(0)

            break

    if breakout:
        continue

    alldir.append(current_dir)

    if current_dir == topdir:
        break
    else:
        current_dir = topdir

for i in range(len(mapoutlist)):
    p = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutextra[i]))]
    q = [x for (y,x) in sorted(zip(mapoutcont[i], mapouttype[i]))]
    # print ("q", q)
    r = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutlabel[i]))]
    s = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutsnum[i]))]
    mapoutcont[i].sort()

    previousapecho = 0
    previouspaecho = 0
    previousb0echo = 0

    for j in range(len(mapoutcont[i])):
        if 'Topup_AP' in  q[j] and not previousapecho:
            allap.append(str(mapoutlist[i]) +'_'+ q[j])            
            previousapecho = allap.count(str(mapoutlist[i]) +'_'+ q[j])
            apscanfirst = 1
            continue

        if 'Topup_PA' in  q[j] and not previouspaecho:
            allpa.append(str(mapoutlist[i]) +'_'+ q[j])
            previouspaecho = allpa.count(str(mapoutlist[i]) +'_'+ q[j])
            pascanfirst = 1
            continue

    for j in range(len(mapoutcont[i])):
        if 'Topup_AP' in  q[j]:
            if apscanfirst:
                apscanfirst = 0
            else:
                allap.append(str(mapoutlist[i]) +'_'+ q[j])

            previousapecho = allap.count(str(mapoutlist[i]) +'_'+ q[j])

            allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + ' ' + str(previousapecho) + ' 2 ' + p[j])
            
        if 'Topup_PA' in  q[j]:
            if pascanfirst:
                pascanfirst = 0
            else:
                allpa.append(str(mapoutlist[i]) +'_'+ q[j])

            previouspaecho = allpa.count(str(mapoutlist[i]) +'_'+ q[j])

            allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + ' ' + str(previouspaecho) + ' 1 ' + p[j])
            
        if 'T1w_MPR_' in  q[j]:
            allt1.append(str(mapoutlist[i]) +'_'+ q[j])
            o = float(allt1.count(str(mapoutlist[i]) +'_'+ q[j]))/2
            if o.is_integer():
                n = q[j] + str(allt1.count(str(mapoutlist[i]) +'_'+ q[j])/2)

                allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + n + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' ' + p[j])

        if 'T2w_SPC_' in  q[j]:
            allt2.append(str(mapoutlist[i].split('/')[0]) +'_'+ q[j])
            o = float(allt2.count(str(mapoutlist[i]) +'_'+ q[j]))/2
            if o.is_integer():
                n = q[j] + str(allt2.count(str(mapoutlist[i]) +'_'+ q[j])/2)

                allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + n + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' ' + p[j])

        if 'fMRI' in q[j]:
            t = q[j].split('_')
            # take out 'PA' or 'AP' from the name using t.pop()
            if t.pop() == 'PA':
                allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + '_'.join(t) + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' 1')
            else:
                allstring[allstudy.index(str(mapoutlist[i]))].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + '_'.join(t) + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' 2')


for i in range(len(allstudy)):
    f = open(str(allstudy[i]) + '_scanlog.txt','w')
    k = 0
    for j in allstring[i]:
        k = k + 1
        f.write(str(k)+j+'\n')
    f.close()

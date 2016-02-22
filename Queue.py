import os
import glob
import time

start_time = time.time()
print start_time
QueueMasterFile = open("QueueMaster.txt", "r")
QMDict = {}
for lines in QueueMasterFile:
    (key, val) = lines.split("=")
    QMDict[key.strip()] = val.strip()
# print QMDict
DirContents = glob.glob(QMDict['Input_Folder'] +"\*.csv")
# print DirContents

FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess

executable = "D://ERE_QueueApplication//Executable//Proteus_V8.8//InputPreProcessingProj//bin//Debug//InputPreProcessingProj.exe "
args = QMDict['Input_Folder']+" "+ QMDict['Output_Folder']+" "+QMDict['Log_Folder']+" "+DirContents[0].split("\\")[-1]+" true false " + QMDict['Classification']
os.system(executable + args)
print DirContents[0].split("\\")[-1] + " for Identity Capture : Complete \n\n\n"

for x in range(1,len(DirContents)):
    args = QMDict['Input_Folder']+" "+ QMDict['Output_Folder']+" "+QMDict['Log_Folder']+" "+DirContents[x].split("\\")[-1]+" false false " + QMDict['Classification']
    os.system(executable + args)
    print DirContents[x].split("\\")[-1] + " for Identity Update : Complete\n\n\n"

print str((time.time() - start_time)/60.0) + " minutes elapsed."

raw_input("Press Enter to Exit.")

import csv,glob,os,shutil

mypath = "./TrainingData/*/*"
newpth = "./TrainingData_original/"
files = glob.glob(mypath)

index = 0


'''
with open('vatl.txt','r') as outfile:
    rows = outfile.readlines()
    for line in rows:
        filename = line.replace('\n','')
        if filename.find('ID') != -1:
            shutil.copyfile(mypath+filename,newpth+filename)
'''

for f in files:
    filename = f.split('\\')[2]
    shutil.copyfile(f,newpth+filename)
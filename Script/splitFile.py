import os,csv,glob

flag = 1
index = 0
prev = ''
current = 'train/'


with open('OfficalTrainingData/stage_2_train.csv','r',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for f in rows:
        if f[0] != 'ID':
            splitTxt = f[0].split('_')
            dtype = splitTxt[2] + '/'
            filename = splitTxt[0]+ "_" +splitTxt[1]+'.png'
            if prev != '':
                if prev == filename and flag == 1:
                    if f[1] != 0 and dtype != 'any':
                        os.rename('./OfficalTrainingData/train/'+filename,'./OfficalTrainingData_split/'+current+dtype+filename)
                        flag = 0
                elif prev != filename and flag == 1:
                    os.rename('./OfficalTrainingData/train/'+prev,'./OfficalTrainingData_split/'+current+'any/'+prev)
                    flag = 1
                    if f[1] != 0 and dtype != 'any':
                        os.rename('./OfficalTrainingData/train/'+filename,'./OfficalTrainingData_split/'+current+dtype+filename)
                        flag = 0
                elif prev != filename and flag == 0:
                    flag = 1
                    if f[1] != 0 and dtype != 'any':
                        os.rename('./OfficalTrainingData/train/'+filename,'./OfficalTrainingData_split/'+current+dtype+filename)
                        flag = 0

                if prev != filename:
                    index += 1
                if index == 4800:
                    current = 'vaild/'
            prev = filename
            
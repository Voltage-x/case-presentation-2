import csv

index = 0

prev = 'ID_0006600dd8'

with open('stage3_train_cls.csv','r',newline='') as clsfile:
    readerx = csv.reader(clsfile)
    with open('stage3_train_cls_m.csv','w+',newline='') as mxfile:
        writerx = csv.writer(mxfile)
        for f in readerx:
            if f[1] == 'filename':
                writerx.writerow(f)
            else:
                if f[10] != prev:
                    index = 0
                    writerx.writerow(f[:20]+[f[10]+'_'+str(index)])
                else:
                    index+=1
                    writerx.writerow(f[:20]+[f[10]+'_'+str(index)])
            prev = f[10]

                
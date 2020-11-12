import glob,pydicom

#train = open('train.txt','w+')
#val = open('val.txt', 'w+')
test  = open('val.txt','w+')

index = 0
prev = 'ID_0006600dd8'

#print(fileIndex)
'''
with open('stage3_train_cls_m.csv','r',newline='') as csvfile:
    rows = csv.reader(csvfile)
    train.write(prev+'\n')
    enable = 0
    for f in rows:
        if f[2] == 'ID_19a638306.png':
            enable = 1
        if enable == 1:
            val.write(f[2]+'\n')
'''

files = glob.glob('TestingData/*')

for f in files:
    ds = pydicom.read_file(f)
    test.write(ds.SOPInstanceUID+'.png\n')
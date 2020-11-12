import csv,glob,pydicom

files = glob.glob('TestingData/*')

classArr = ['epidural','intraparenchymal','intraventricular','subarachnoid','subdural']

with open('final.csv','w+',newline='') as outfile:
    writer = csv.writer(outfile)
    for f in files:
        ds = pydicom.read_file(f)
        dcmFilename = f.split('\\')[1]
        dcmFilename = dcmFilename.split('.')[0]
        pngFilename = ds.SOPInstanceUID + '.png'
        with open('fold_0_test_aug_10_train.csv','r',newline='') as csvfile:
            reader = csv.reader(csvfile)
            for r in reader:
                if r[7] == pngFilename and r[7] != 'filename':
                    if float(r[1]) < 0.4:
                        writer.writerow([dcmFilename,'healthy'])
                    else:
                        classIndex = -1
                        classScore = 0.0
                        for i in range(2,7):
                            #print(p[i])
                            if float(r[i]) > classScore:
                                classScore = float(r[i])
                                classIndex = i
                        writer.writerow([dcmFilename,classArr[classIndex-2]])
import csv,glob

mypath = "./TrainingData_nofold/*"
files = glob.glob(mypath)

index = 0

with open('stage3_train2.csv','w+',newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Unnamed: 0','filename','any','epidural','intraparenchymal','intraventricular','subarachnoid',
    #'subdural','patient_id','study_instance_uid','series_instance_uid','image_position','samples_per_pixel','pixel_spacing',
    #'pixel_representation','window_center','window_width','rescale_intercept','rescale_slope','slice_id'])
    for f in files:
        filename = f.split('\\')[2]
        dtype = f.split('\\')[1]
        if dtype == 'epidural':
            typerow = [1,1,0,0,0,0]
        elif dtype == 'intraparenchymal':
            typerow = [1,0,1,0,0,0]
        elif dtype == 'intraventricular':
            typerow = [1,0,0,1,0,0]
        elif dtype == 'subarachnoid':
            typerow = [1,0,0,0,1,0]
        elif dtype == 'subdural':
            typerow = [1,0,0,0,0,1]
        else:
            typerow = [0,0,0,0,0,0]
        with open('RSNA2019_Intracranial-Hemorrhage-Detection-master/2DNet/data/stage1_test_cls.csv', 'r', newline='') as csvfile:
            reader_ = csv.reader(csvfile)
            for fr in reader_:
                if fr[2] == filename:
                    writer.writerow(fr[1:3]+typerow+fr[3:])
                    break
        index+=1
        if(index % 100 == 0):
            print(index)
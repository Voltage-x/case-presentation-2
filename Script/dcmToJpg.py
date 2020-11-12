import os,glob,pydicom,csv

files = glob.glob('TestingData/*')

index = 0

'''
with open('stage4_test_cls.csv','w+',newline='') as csvfile:
    rows = csv.writer(csvfile)
    rows.writerow(['','filename','patient_id','study_instance_uid','series_instance_uid',
    'image_position','samples_per_pixel','pixel_spacing','pixel_representation','window_center',
    'window_width','rescale_intercept','rescale_slope'])
    for f in files:
        #print(f)
        ds = pydicom.read_file(f)
        #print(ds)
        filename = f.split('\\')[1]
        filename = filename.split('.')[0]+'.png'
        rows.writerow([index,ds.SOPInstanceUID+'.png',ds.PatientID,ds.StudyInstanceUID,ds.SeriesInstanceUID,
        ds.ImagePositionPatient,ds.SamplesPerPixel,ds.PixelSpacing,ds.PixelRepresentation,ds.WindowCenter,
        ds.WindowWidth,ds.RescaleIntercept,ds.RescaleSlope])
        index+=1
'''

with open('stage4_test_cls.csv','w+',newline='') as csvfile:
    rows = csv.writer(csvfile)
    rows.writerow(['','filename','patient_id','study_instance_uid','series_instance_uid',
    'image_position','samples_per_pixel','pixel_spacing','pixel_representation','window_center',
    'window_width','rescale_intercept','rescale_slope'])
    vaild_file = open('vatl.txt','r')
    xrow = vaild_file.readlines()
    for f in xrow:
        filename = './TrainingData_original/'+ f.split('.')[0] + '.dcm'
        ds = pydicom.read_file(filename)
        #print(ds)
        filename = f.split('.')[0] + '.png'
        rows.writerow([index,filename,ds.PatientID,ds.StudyInstanceUID,ds.SeriesInstanceUID,
        ds.ImagePositionPatient,ds.SamplesPerPixel,ds.PixelSpacing,ds.PixelRepresentation,ds.WindowCenter,
        ds.WindowWidth,ds.RescaleIntercept,ds.RescaleSlope])
        index+=1
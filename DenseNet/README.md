
#### Dependencies
- opencv-python==3.4.2
- scikit-image==0.14.0
- scikit-learn==0.19.1
- scipy==1.1.0
- torch==1.1.0
- torchvision==0.2.1

#### Required Equipment
- Ubuntu 18.04.5 LTS or newer
- CUDA Version 11.0 or newer
- Python 3 or newer

# 2D CNN Classifier


1. Put training data in  2DNet/data/train_dcm/
2. Put testing data in  2DNet/data/test_dcm/

##### No need to have different folder for each different classes, just put all image into the folder.
##### We already convert 6000 train image as 2DNet/data/train.csv and 600 test images as 2DNet/data/test.csv
##### If you want to use other data, please convert data to our .csv format, you can reference to script/generator.py and script/genSliceId.py to know how to convert.

3. go to 2DNet/src/
```
cd 2DNet/src/
```

4. convert dcm to png
```
python3 prepare_data.py -dcm_path ../data/train_dcm -png_path ../data/train_png
python3 prepare_data.py -dcm_path ../data/test_dcm -png_path ../data/test_png
```

5. train

```
python3 train.py -backbone DenseNet121_change_avg -img_size 256 -tbs 256 -vbs 128 -save_path DenseNet121_change_avg_256
```

After training,  the .pth files will be saved in src/data_test/DenseNet121_change_avg_256/
You need to put the .pth of specific epoch number to src/DenseNet121_change_avg_256/ and rename as model_epoch_best_0.pth

6. predict
```
python3 predict.py -backbone DenseNet121_change_avg -img_size 256 -tbs 4 -vbs 4 -spth DenseNet121_change_avg_256
```

7. The predict metadata will be save as src/DenseNet121_change_avg_256/prediction/fold_0_test_aug_10.csv




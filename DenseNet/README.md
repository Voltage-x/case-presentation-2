
#### Dependencies
- opencv-python==3.4.2
- scikit-image==0.14.0
- scikit-learn==0.19.1
- scipy==1.1.0
- torch==1.1.0
- torchvision==0.2.1

# 2D CNN Classifier

Prepare csv file:

download data.zip:  https://drive.google.com/open?id=1buISR_b3HQDU4KeNc_DmvKTYJ1gvj5-3

1. convert dcm to png
```
python3 prepare_data.py -dcm_path stage_1_train_images -png_path train_png
python3 prepare_data.py -dcm_path stage_2_test_images -png_path test_png
```

2. train

```
python3 train_model.py -backbone DenseNet121_change_avg -img_size 256 -tbs 256 -vbs 128 -save_path DenseNet121_change_avg_256
```

3. predict
```
python3 predict.py -backbone DenseNet121_change_avg -img_size 256 -tbs 4 -vbs 4 -spth DenseNet121_change_avg_256
```

After single models training,  the oof files will be saved in ./SingleModelOutput(three folders for three pipelines). 

After training the sequence model, the final submission will be ./FinalSubmission/final_version/submission_tta.csv

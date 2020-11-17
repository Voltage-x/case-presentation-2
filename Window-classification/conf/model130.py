workdir = './model/model130_total'
seed = 30
apex = True

n_fold = 1
epoch = 10
resume_from = None

batch_size = 28 #28 -> 1.4e-4
num_workers = 4
imgsize = (512, 512) #(height, width)
#imgsize = (224, 224) #(height, width)

loss = dict(
    name='BCEWithLogitsLoss',
    params=dict(),
)

optim = dict(
    name='Adam',
    params=dict(
        lr=6e-4,
    ),
)

model = dict(
    name='efficientnet-b0',
    pretrained='imagenet',
    n_output=6,
)


scheduler = dict(
    name='MultiStepLR',
    params=dict(
        milestones=[1,2,3,4,5,6],
        gamma=2/3,
    ),
)

#normalize = None
#normalize = {'mean': [0.485, 0.456, 0.406], 'std': [0.229, 0.224, 0.225],}
normalize = {'mean': [13.197, 7.179, -78.954,], 'std': [24.509, 55.063, 113.127,]}


crop = dict(name='RandomResizedCrop', params=dict(height=imgsize[0], width=imgsize[1], scale=(0.7,1.0), p=1.0))
crop_test = dict(name='RandomResizedCrop', params=dict(height=imgsize[0], width=imgsize[1], scale=(0.75,1.0), p=1.0))
resize = dict(name='Resize', params=dict(height=imgsize[0], width=imgsize[1]))
hflip = dict(name='HorizontalFlip', params=dict(p=0.5,))
vflip = dict(name='VerticalFlip', params=dict(p=0.5,))
contrast = dict(name='RandomBrightnessContrast', params=dict(brightness_limit=0.08, contrast_limit=0.08, p=0.5))
totensor = dict(name='ToTensor', params=dict(normalize=normalize))
rotate = dict(name='Rotate', params=dict(limit=30, border_mode=0), p=0.7)
rotate_test = dict(name='Rotate', params=dict(limit=25, border_mode=0), p=0.7)
#dicomnoise = dict(name='RandomDicomNoise', params=dict(limit_ratio=0.06, p=0.9))
#dicomnoise_test = dict(name='RandomDicomNoise', params=dict(limit_ratio=0.05, p=0.7))

window_policy = 4

data = dict(
    train=dict(
        dataset_type='CustomDataset',
        annotations='./src/preprocess/total.pkl',
        imgdir='./TotalData',
        imgsize=imgsize,
        n_grad_acc=1,
        loader=dict(
            shuffle=True,
            batch_size=batch_size,
            drop_last=True,
            num_workers=num_workers,
            pin_memory=False,
        ),
        transforms=[crop, hflip, rotate, contrast, totensor],
        dataset_policy=1,
        window_policy=window_policy,
    ),
    valid = dict(
        dataset_type='CustomDataset',
        annotations='./src/preprocess/val.pkl',
        imgdir='/data/rsna-intracranial-hemorrhage-detection/stage_2_train',
        imgsize=imgsize,
        loader=dict(
            shuffle=False,
            batch_size=batch_size,
            drop_last=False,
            num_workers=num_workers,
            pin_memory=False,
        ),
        transforms=[crop_test, hflip, rotate_test, contrast, totensor],
        dataset_policy=1,
        window_policy=window_policy,
    ),
    test = dict(
        dataset_type='CustomDataset',
        annotations='./src/preprocess/test.pkl',
        imgdir='./TestingData',
        imgsize=imgsize,
        loader=dict(
            shuffle=False,
            batch_size=batch_size,
            drop_last=False,
            num_workers=num_workers,
            pin_memory=False,
        ),
        transforms=[crop_test, hflip, rotate_test, contrast, totensor],
        dataset_policy=1,
        window_policy=window_policy,
    ),
)
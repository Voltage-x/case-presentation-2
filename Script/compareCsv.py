import csv

score = 0

threshold = 0.1

for xxx in range(8):
    score = 0
    with open('fold_0_test_aug_10_6000_Vaild.csv', 'r') as pred:
        pred_row = csv.reader(pred)
        for p in pred_row:
            if p[1] == 'any':
                continue
            with open('stage3_train_cls_m.csv', 'r') as origi:
                origi_row = csv.reader(origi)
                for o in origi_row:
                    if o[3] == 'any':
                        continue
                    classIndex = -1
                    classScore = 0.0
                    for i in range(2,7):
                        #print(p[i])
                        if float(p[i]) > classScore:
                            classScore = float(p[i])
                            classIndex = i
                    #print(p[7],o[2])
                    if p[7] == o[2]:
                        #print(float(p[1]))
                        if float(p[1]) > threshold and int(o[3]) == 1:
                            #print('123')
                            if int(o[classIndex+2]) == 1:
                                score+=1
                        elif int(o[3]) == 0:
                            score+=1
    print(threshold,score)
    threshold += 0.1
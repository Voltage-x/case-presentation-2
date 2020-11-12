import csv

score = 0

cat = ['any','epidural', 'intraparenchymal', 'intraventricular', 'subarachnoid', 'subdural']

with open('fold_0_val_aug_10.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for f in rows:
        index = 1
        if f[1] != 'any':
            for catIndex in range(1,7):
                if float(f[catIndex]) > float(f[index]):
                    index = catIndex
        #print(index)
        #print(f[7])
        with open('output.csv', 'r', newline='') as csvx:
            row2 = csv.reader(csvx)
            for fr in row2:
                if fr[1] != 'any':
                    if fr[0] == f[7]:
                        if fr[index] == 1:
                            print("xd")
                            score += 1

print(score)

        
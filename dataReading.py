import csv

with open("moneroData.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    for row in reader:
        print(row)


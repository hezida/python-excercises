import csv

with open('data.csv') as CSV_file:
    reader = csv.reader(CSV_file)
    l=[]
    for line in reader:
        arr = []
        for data in line:
            if "." in data:
                data = float(data)
            else:
                data = int(data)
            arr.append(data)
        l.append(arr)
print (l)
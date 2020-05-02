with open('data.csv') as CSV_file:
    l=[]
    for line in CSV_file:
        #line=line.strip()
        line = line.replace('\n', "")
        line = line.replace(" ", "")
        val = line.split(",")
        arr=[]
        for data in val:
            if "." in data:
                data = float(data)
            else:
                data = int(data)
            arr.append(data)
        l.append(arr)
        #l.append(val)
print(l)
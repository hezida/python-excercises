names = ["name1", "name2", 8]
colors = ["red", "blue", "white"]

print(names)
print(type(names))

print("second element is: {}".format(names[1]))

for num in range(1,10):
    print(num)

print(len(names))

#good1
for name in names:
    print(names)

#bad
for num in range(0, len(names)):
    print(num, names[num])

#good2
for num, name in enumerate(names):
    print(num, name)

#bad
i=0
for name in names:
    print(i, name)
    i+=1

print("--------------")

for i in range(6):
    print(i)

print("--------------")

#Looping over 2 colloections
#for name, coloer in izip(names, colors):
#    print(name, '-->', colors)
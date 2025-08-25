list1 = [3,5,34,25,7,5,24]
evenList = []
oddlist = []

for a in list1:
    if a % 2 == 0:
        evenList.append(a)
    else:
        oddlist.append(a)

print(evenList)
print(oddlist)
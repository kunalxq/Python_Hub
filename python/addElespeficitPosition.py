list = [4,5,6,8,7,70]

index = 3
insert = 50

list1 = []

for i in range (0, len(list)):
    if i == index:
        list1.append(insert)
    else:
        list1.append(list[i])

print(list1)
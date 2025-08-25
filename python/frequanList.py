list = [4,6,4,7,3,7,9]

dics = {}

for a in list:
    if a in dics:
        dics[a] += 1
    else:
        dics[a] = 1

print(dics)
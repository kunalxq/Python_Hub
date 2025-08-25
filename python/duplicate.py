a = [12,12,12,42,24,5,32,32]
b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)
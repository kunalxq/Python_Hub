a = [3,7,4,8,6,5,500]

for i in range (0, len(a)):
    for j in range (i+1, len(a)):
        if a[i] >= a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
print(a[-2])
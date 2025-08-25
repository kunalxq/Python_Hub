a = [12,34,-32,3,23,-12,-31]

countPos = 0
countNega = 0

for i in a:
    if i > 0:
        countPos += 1
    else:
        countNega += 1

print("positive=", countPos)
print("negative=", countNega)
a = [32,41,49,73,12,43]

eveCount= 0
oddCount = 0

for i in a:
    if i % 2 ==0:
        eveCount += 1
    else:
        oddCount += 1

print("even count:", eveCount)
print("odd count", oddCount)
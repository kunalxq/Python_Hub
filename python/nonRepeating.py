input = input("enter a string:")

count = {}

for char in input:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char in input:
    if count[char] == 1:
     print(char)
     break

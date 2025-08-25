# a = input("enter a string:")
# count = 0
# for char in a:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         count += 1
# print(count)

b = input("enter a string:")
c = "a,e,i,o,u,A,E,I,O,U"
count = 0
for char in b:
    if char not in c:
     count += 1
print(count)


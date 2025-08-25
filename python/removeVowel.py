# a = input("enter a string:")

# b = "a,e,i,o,u,A,E,I,O,U"
# c = ""
# for char in a:
#     if  char not in b:
#         c += char
# print(c)


a = input("enter a string:")
b = " "
c = ""
for char in a:
    if  char not in b:
        c += char
print(c)
input = input("enter a string:")

upper = 0
lower = 0 

for char in input:
    if 'A' <= char <='Z':
        upper += 1
    else:
        lower += 1
print("uppercase:",upper)
print("lowercase:",lower)
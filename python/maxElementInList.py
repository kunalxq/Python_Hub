a = [10, 11, 13, 42, 41]

# print(max(a))

max = a[0]

for num in a:
    if num > max:
        max = num
        print(max)


# for num in range (1, len(a)):
#     if a[num] < max:
#         max = a[num]
# print(max)
a = int(input("enter the num:"))
if a < 1:
    print("not prime number")
else:
    for i in range(2, a):
        if a % i == 0:
         print ("not prime")
         break
    else:
     print("prime number")
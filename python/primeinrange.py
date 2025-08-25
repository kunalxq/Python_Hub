num  = int(input("Enter a number: "))
num1 = 0
for num1 in range(2, num + 1):
    if num1 > 1:                  
        for i in range(2, num1): 
            if num1 % i == 0:    
                break
        else:                    
         print(num1)
n = int(input("Enter the Number of Terms = "))

a = 0
b = 1


if n == 0:
    print("Invalid!")

elif n == 1:
    print(0)

elif n == 2:
    print(0)
    print(1)

else:
    print(a)
    print(b)
    
    for i in range(1,n-1):
        c = a+b
        print(c)
        a = b
        b = c
        
        
        
        






import math
x = int(input("enter your number: "))
i=2
while i<x:
    if x%i==0:
        print(x, "is not a prime number")
        i+=1
        break
    else:
        print(x, "is a PRIME number")
        break

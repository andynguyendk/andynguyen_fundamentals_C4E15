import math
x = int(input("enter your number: "))
i=2; count = 0
while i<= x**0.5:
    if x%i==0:
        print(x, "is divisible by", i, "and", x//i)
        count +=1
    i+=1
if count == 0:
    print(x, "is a PRIME number")
else:
    print(x, "is NOT a prime number")

import math
x = int(input("enter your number: "))
digit = 0
while True:
    if x>(10**digit):
        digit += 1
    else:
        break
print("number of digits ", digit)
print(math.log10(x))

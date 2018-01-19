x1 = int(input("Enter 1st number: "))
x2 = int(input("Enter 2nd number: "))
comm = 1
for i in range(1, min(x1, x2)+1):
    if x1%i == 0 and x2%i ==0:
        comm = i
    else:
        pass
print("the largest common deniminator is: ",comm)

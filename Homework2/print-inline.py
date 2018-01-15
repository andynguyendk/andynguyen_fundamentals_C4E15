#combined all a,b,c,d

l = int(input("number of lines= "))
b = int(input("number of blocks in a line= "))
s = int(input("number of stars (in a block)= "))
x = int(input("number of x(s) (in a block)= "))

for i in range(l):
    if i%2==1:
        for i2 in range(b):
            for i3 in range(s):
                print("*", end ="")
            for i4 in range(x):
                print("x", end ="")
        print(" ")
    else:
        for i2 in range(b):
            for i3 in range(x):
                print("x", end ="")
            for i4 in range(s):
                print("*", end ="")
        print(" ")

x = int(input("enter a number: "))
print(int((1+x)*x/2))

total = 0
for i in range(x+1):
    total+=i

print(total)

total2 = 0
i2 = 0
while i2 <= x:
    total2 +=i2
    i2+=1
print(total2)

print(sum(range(0, x+1,1)))

from random import randint
x = randint(1,100)
count = 0
while count<7:
    ans = int(input("Guess your number: "))
    if ans < x:
        print("the number is greater than ", ans)
    elif ans > x:
        print("the number is smaller than ", ans)
    else:
        print("Congrats!")
        break
    count+=1

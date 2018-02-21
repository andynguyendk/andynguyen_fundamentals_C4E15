from random import randint, choice
import operator
ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv }
oper = [["+"] *4 + ["-"]*3 + ["*"]*2 + ["/"]*1]
x = randint(0,10)
y = randint(0,10)
error = [0,0,0,0,0,0,1,-1,+2,-2]
disp = ops[choice(oper)] + choice(error)
print("*" *10)
print("{0} {1} {2}= {3}".format(x, oper, y, disp))
print("*" *10)
ans = input("(Y/N)?: ")
if error == 0 and ans.lower() == "y":
    print("Yay")
elif error != 0 and ans.lower() == "n":
    print("Yay")
else:
    print("Nay")

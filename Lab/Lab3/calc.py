import operator
ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv }
x = float(input("x = ", ))
ope = input("Operation (+,-,*,/): ")
y = float(input("y = ", ))

if ope in ["+", "-", "*", "/"]:
    res = ops[ope](x,y)
    print("{0} {1} {2} = {3}".format(x,ope,y,res))
else:
    print("Operation not supported")

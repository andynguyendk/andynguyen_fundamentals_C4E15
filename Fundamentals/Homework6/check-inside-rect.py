def is_inside(x, y):
    if len(x) == 2 and len(y) == 4:
        if y[0]<=x[0]<= y[0]+y[2] and y[1]<=x[1]<=y[1]+y[3]:
            return(True)
        else:
            return(False)
    else:
        return("Wrong parameter count for function")

# x = is_inside([200, 120], [140, 60, 100, 200])
# print(x)

x = is_inside([100, 120], [140, 60, 100])
print(x)

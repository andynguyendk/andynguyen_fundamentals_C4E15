temp = input("temperature= ")
scale = input("F or C? ")
if scale == "F" or scale == "f":
    print(temp, "F =", round((int(temp)-32)*5/9,3), "C")
if scale == "C" or scale == "c":
    print(temp, "C =", round(int(temp)*9/5+32,3), "F")

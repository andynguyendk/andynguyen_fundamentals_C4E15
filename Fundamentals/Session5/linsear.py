seT = [12, 10, 13, 44, 33, 3454]

found = -1
while True:
    num = int(input("Enter a number: "))
    for i in range(len(seT)):
        if num != seT[i]:
            pass
        else:
            print("Found {0} at index {1}".format(num, i))
            break
    else:
        print("Not found")

maX = 100; miN = 0
print("Think of a number from 0 to 100 & I will guess it")
print('''If I'm right, type "c"''')
print('''If my guess is (S)maller than your number, type "s"''')
print('''If my guess is (G)reater than your number, type "g"''')
while True:

    ans = input("Is your number {0} ?".format((maX+miN)//2))
    if ans == "c":
        print("I knew it!")
        break
    elif ans == "s":
        maX = (maX+miN)//2
        continue
    elif ans == "g":
        miN = (maX+miN)//2
        continue
    else:
        print("I don't understand your input")
        break

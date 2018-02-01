size = [5,7,300,90,24,50,75]

print("Hello, my name is Andy & these are my sheep sizes")
print(size)

for i in range(4):
    print("One month has passed, now here is my flock")
    for i, siz in enumerate(size):
        size[i] = size[i] +50
    print(size)

    print("Now my biggest sheep has size {0}, let's shear it".format(max(size)))

    maXpos = size.index(max(size))
    size[maXpos] = 8
    print("After shearing, here is my flock")
    print(size)

total = 0
for i in range(len(size)):
    total += size[i]

print("My flock has size in total: ", total)
print("I would get {0} *$2 = *{1}".format(total, total*2))

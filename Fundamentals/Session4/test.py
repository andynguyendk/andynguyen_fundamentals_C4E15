# food1 = "thit cho"
# food2 = "pho"
# food3 = "bun dau"
# food4 = "tay gau"
# food5 = "thang co"
# food6 = "com rang"

# menu = []
# print(menu)
# menu = ["thit cho"]
# print(menu)
menu = ["Thit Cho", "Pho", "Tieu ho"]
# for i in range(len(menu)):
#     menu[i] = menu[i].lower()
# print(*menu)
menu2 = []
for i in range(len(menu)):
    menu2.append(menu[i].lower())
print(*menu2)

# print(menu)
# menu.append("bun dau")
# print(menu)

# print(*menu, sep=', ' , end="")
#
# for i in range(len(menu)):
#     print("{0} . {1}".format(i+1,menu[i]))

# for x, y in enumerate(menu, 1):
#     print("{0}.{1}".format(x,y))

# print(*enumerate(menu, 1))

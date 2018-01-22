shop = ["T-shirt", "Sweater"]
while True:
    resp = input("Welcome to our shop, what do you want? (C,R,U,D) ")
    if resp.lower() == "r":
        print(*shop, sep=", ")
    elif resp.lower() == "c":
        add = input("Enter new item: ")
        shop.append(add)
        print(*shop, sep=", ")
    elif resp.lower() == "u":
        update = int(input("Update position? "))
        new_item = input("New item? ")
        if update <= len(shop):
            shop[update -1] = new_item
            print("Our items:" *shop, sep=", ")
        else:
            print("Item slot is empty")
    elif resp.lower() == "d":
        delete = int(input("Delete position? "))
        if delete <= len(shop):
            shop.pop(delete-1)
            print("Our items:", *shop, sep=", ")
        else:
            print("Item slot is empty")
    else:
        break

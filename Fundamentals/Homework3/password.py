from getpass import getpass
print("welcome to superuser gateway")
att = 0
while att <3:
    username = input("Username: ")
    if username == "admin":
        password = getpass("Password: ")
        if password == "blahblah":
            print("Welcome ",username)
            break
        else:
            print("Wrong password!!")
    else:
        print("User does not exist!!")
    att +=1
else:
    print("Maximum 3 attempts only are allowed!")

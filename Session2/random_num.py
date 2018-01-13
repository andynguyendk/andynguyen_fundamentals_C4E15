from random import randrange

mood = randrange(0,100)
sad = '''adadsa'''
norm = """(-.-)"""
happy = '''ᵔ.ᵔ'''
print(mood)
if mood<30:
    print (sad)
elif mood<60:
    print (norm)
else:
    print (happy)

import random
from random import shuffle
wordlist = ["analogy", "anagram", "stupid fuck"]
while True:
    word = random.choice(wordlist)
    char = list(word)
    shuffle(char)
    print("Here's your shuffle:")
    print(char)
    for i in range(10):
        guess = input("What's the word? ")
        if guess == word:
            print("Bingo!")
            break
        elif guess == "i.give.up":
            print("Ok, loser")
            break
        else:
            print("No, try again")
            continue
    break

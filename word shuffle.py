import random

print("-Word shuffle-")

word = "ANACONDA"

word_list = list(word)

shuffled = random.shuffle(word_list)

print(word_list)

answer = input("Discover the correct word: ").upper()

if answer != "ANACONDA":
    print("All wrong buddy!")

else:
    print("Congrats!")


print("Welcome to the word search!")

alphabet_tuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

print("Tur_le")

letter = input("Enter a letter in order to complete the word: ")

if letter.upper() != "T":
    print("Hmmm try again later!")

else:
    print("Correct! Try a harder one.")
    print("Pi_geon")
    letter1 = input("Enter a letter in order to complete the word: ")
    if letter1.upper() != "G":
        print("Too bad, u lost!")

    else:
        print("Woah, you beat the game!")
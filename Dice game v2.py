import random
def game():
    print("Welcome to the dice game! Reach a total > 15 to win.")

    total = 0
    rolls = []

    for i in range(3):
        roll = random.randint(1, 6)
        rolls.append(str(roll))
        total += roll
        print(f"Roll {i + 1}: {' + '.join(rolls)} = {total}")

    if total >= 15:
        print(f"Total: {total}. You won, lucky!")
    else:
        print(f"Total: {total}. You lose!")


game()

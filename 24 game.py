import random


print("24 Game")
rounds = 4

for n in range(0, rounds):
    cards = [random.randint(1, 9) for i in range(4)]
    print(f"\nRound {n}")
    print(f"cards: {cards}")

    print("Use all 4 cards to obtain  24.")
    c1 = input("1st Card Value: ")
    op1 = input("Operator (+, -, *, /): ")
    c2 = input("2nd Card Value: ")
    op2 = input("Operator: ")
    c3 = input("3rd Card Value: ")
    op3 = input("Operator: ")
    c4 = input("4th Card Value: ")

    expression = f"{c1}{op1}{c2}{op2}{c3}{op3}{c4}"

    try:
        input_nums = ([int(c1), int(c2), int(c3), int(c4)])
        if input_nums != cards:
            print("Error: You must use the cards provided!")
            continue

        result = eval(expression)
        print(f"Result: {expression} = {result}")

        if result == 24:
            print("Success! You got 24!")
        else:
            print(f"Missed it! {result} is not 24.")

    except Exception:
        print(f"Invalid input or math error")

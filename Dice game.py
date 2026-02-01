import random

print("Welcome to the dice game you will get to roll the dice 3 times to pass the nmber 15")

faces = [1, 2, 3, 4, 5, 6]

enter = random.choice(faces)

try:
    print(faces)
    enter1 = random.choice(faces)
    print(f'{enter} + {enter1}')
    enter2 = random.choice(faces)
    print(f'{enter} + {enter1} + {enter2}')
    ans = enter + enter1 + enter2
    print(f"your total is {ans}")
    if ans < 15:
        print("You lose")

    else:print("You won, lucky!")




except:
    print("Something went wrong!")

num = 3

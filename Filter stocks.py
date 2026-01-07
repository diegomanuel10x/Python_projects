import random

# This program will send out a message dependent on what the result of the stock change is.
# The program starts with 12 users, we will slowly cut down until we get at least 1 person to subscribe
# at most 2 people will subscribe.

list = ["Rise", "Fall"]
num_of_clients = 12
list_1 = random.choice(list)

print("""Hey, This application will send you and email that will predict whether stocks rise or fall.
 You will get a free trial in which we predict 3 stocks, after that if 
 you would like to continue, you can subscribe.\n""")

i=3
while i <= 3:
    first_batch = num_of_clients//2
    print("The stock will rise.\n" * first_batch)
    print("The stock will fall.\n" * first_batch)
    i += 1

#This part of the progran will filter out half of the users since the program guesses and doesnt actually know
#Now we will repeat this program with the users that we got correct until we get all 3 trials correct
#In order to get at least 1 subscriber
if list_1 == "Rise":
    print("The stocks rose.\n#########################################################################################")
    i = 3
    while i <= 3:
        first_batch = num_of_clients // 4
        print("The stock will rise.\n" * first_batch)
        print("The stock will fall.\n" * first_batch)
        i += 1

elif list_1 == "Fall":
    print("The stocks fell.\n#########################################################################################")
    i = 3
    while i <= 3:
        first_batch = num_of_clients // 4
        print("The stock will rise.\n" * first_batch)
        print("The stock will fall.\n" * first_batch)
        i += 1

if list_1 == "Rise":
    print("The stocks rose.\n#########################################################################################")
    i = 3
    while i <= 3:
        first_batch = num_of_clients-11
        print("The stock will rise.\n" * first_batch)
        print("The stock will fall.\n" * first_batch)
        i += 1



elif list_1 == "Fall":
    print("The stocks fell.\n ########################################################################################")
    i = 3
    while i <= 3:
        crunch = num_of_clients % 10
        first_batch = crunch
        print("The stock will rise.\n" * first_batch)
        print("The stock will fall.\n" * first_batch)
        i += 1

if list_1 == "Rise":
    print("The stocks rose.\n You should consider subscribing :)")

elif list_1 == "Fall":
    print("The stocks fell.\n You should consider subscribing :)")






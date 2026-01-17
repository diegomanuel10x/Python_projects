print("To do list!")

print("\nHey welcome to your to do app!")

To_do = str(input("Enter the activities that you would like to accomplish: "))

list1 = To_do.split()

for i in list1:
    print(f'The following are your to_dos {list1}')
    do = input(f"Have you done {i} (y/n)?: ")
    print(do)

    if do == "y".lower():
        print("Excellent job!")

    elif do == "n".lower():
        print("Get it done!")

    else:
        print("Great job!")

    

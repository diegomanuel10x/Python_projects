height = input("Enter the height for your pyramid: ")

try:
    height = int(height)

    for i in range(1, height + 1):
        print("#" * i)

except ValueError:
    print("Invalid! Please enter a numeric integer.")

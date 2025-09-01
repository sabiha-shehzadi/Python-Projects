import random

while True:
    choice = input("Enter your choice to get a roll (y/n): ")
    if choice.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print({dice1, dice2})
    elif choice.lower() == "n":
        print("no roll was requested!")
        break
    else:
        print("invalid choice!")
        print("Please enter 'y' or 'n'.")
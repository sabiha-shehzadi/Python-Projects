import random #import the random library to use randint

while True: # as we dont know about the iterations
    choice = input("Enter your choice to get a roll (y/n): ")
    if choice.lower() == "y": # for better useability
        dice1 = random.randint(1, 6) # starting and ending parameters 
        dice2 = random.randint(1, 6)
        print([dice1, dice2]) # use tuple or list instead of sets
    elif choice.lower() == "n":
        print("no roll was requested!")
        break # will stop while loop 
    else:
        print("invalid choice!")
        print("Please enter 'y' or 'n'.")

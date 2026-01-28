import random 

randomNumber = random.randint(1, 100)
max_chances= 10
chance= 0

def print_chances(chances):
    print(f"You have {max_chances - chances} chances left.")

while chance <= max_chances:
    try:
     userGuess = int(input("Enter your guess (between 1 and 100): "))
    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 100.")
        continue
    if userGuess == randomNumber:
        print(f"Congratulations! You've guessed the correct number {randomNumber} in {chance} chances.")
        break
    elif userGuess > randomNumber:
        print("Too high! Try again.")
        print_chances(chance)
    else:
        print("Too low! Try again.")
        print_chances(chance)
    chance += 1
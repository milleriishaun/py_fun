import random
number = random.randint(0, 10)

while True:
    try:
        userinput = int(input("Guess a number between 1 and 10: "))
        if userinput == number:
            print("\nYou got the number!")
            break
        elif userinput < number:
            print("Too low!")
        elif userinput > number:
            print("Too high!")
    except ValueError:
        print("Please enter a number!")
    except:
        print("An unknown character was entered...")

print("\nThank you for playing. Game Over.")
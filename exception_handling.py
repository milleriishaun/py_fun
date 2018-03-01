'''
# Create a custom Exception
# Though not done commonly
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog's name: ")

    if any(char.isdigit() for char in dogName):

        raise DogNameError

except DogNameError:
    print("Your dog's name can't contain a number")
'''

while True:
    try:
        num1, num2 = input("Enter 2 values to divide: ").split()
        quotient = int(num1)/int(num2)

        print("{} / {} = {}".format(num1, num2, quotient))

    except ZeroDivisionError:
        print("You can't divide by zero")

    except ValueError:
        print("Enter two integers(separated by a space)")

    else:
        print("You didn't raise an exception")

    finally:
        print("I execute no matter what")


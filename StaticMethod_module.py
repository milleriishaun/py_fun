# created own specific module
from getSum import getSum

# benefit of using from:
# print("Sum: ", getSum(1,2,3,4,5))
# rather than
# print("Sum: ", getSum.getSum(1,2,3,4,5))


# Static variables
# Static Methods
# Make own Modules
# Exeption Handling

# Static Method: allow access without having to initialize a class
# (this means you can execute these methods without creating an object)
# (also used as utility methods,)
# (also used when it nonsensical for a real_world object to have method)
# (which means the method needs to exist even though there is not object)
'''
class Sum:

    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:

            sum += i

        return sum
    
def main():
    print("Sum: ", Sum.getSum(1,2,3,4,5))


main()
'''

class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1
    
    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    Spot = Dog("Spot")
    Spot.getNumOfDogs()
    Doug = Dog("Doug")
    Spot.getNumOfDogs()
    Doug.getNumOfDogs()
    print("Sum: ", getSum(1,2,3,4,5))



main()
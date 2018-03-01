class Animal:

    def __init__(self, birthType="Unknown",
                appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    # getter method
    @property
    def birthType(self):
        return self.__birthType
    
    # setter method
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance
    
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Magic method... string magic method
    # get the class' real name using type(self).__name__
    # then you don't have to choose __blooded, but when user prints object
    # all info thrown into these {}, then format, then puts to screen
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__,
                self.birthType, self.appearance, self.blooded)

class Mammal(Animal):

    def __init__(self, birthType="born alive",
                appearance="fair or fur",
                blooded="warm-blooded",
                nurseYoung=True):
        
        # call init method inside of Animal from inside Mammal class
        # but can't get nurseYoung because it is not in Animal
        Animal.__init__(self, birthType, appearance, blooded)

        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung
    
    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overwrite magic string method
    def __str__(self):
        return super().__str__() + " and"\
                "it is {} they nurse their young".format(self.nurseYoung)

# Another class inheritance
class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive",
                appearance="dry scales",
                blooded="cold blooded"):
        
        Animal.__init__(self, birthType, appearance, blooded)
    
    # operator overloading/function overloading:
    # in python, dont need it b/c you don't need to define
    # the datatypes of the values you're passing through,
    # instead use splat.
    def sumAll(self, *args):
        
        sum = 0

        for i in args:

            sum += 1
    
        return sum

# Polymorphism: (in python, this works differently than other langs)
# functions are going to accept any object and are going to expect
# that that object is going to provide the needed method to execute

# If you call on a method for an object, the method needs
# to first exist for that execution to work

# Statically typed:
# in most languages, you define the type when you DECLARED the variable
# int x = "String" (this would fail, but in Python, doesn't matter)
# In Python, variables are Dynamically Defined
# This means that type is defined when the value is ASSIGNED
# getBirthType is a method that exists outside of Animal class,
# but it finds different object to run the function on.(polymorphism)
# If method exists when you call on an object, 
# (if birthType exist inside an object, it doesn't matter type of object)
# no matter what the object type, it will work.
# For other languages, there is no Dynamically Defined Variables
def getBirthType(theObject):
        print("the {} is {}".format(type(theObject).__name__,
                                    theObject.birthType))

def main():

    animal1 = Animal("born alive")

    print(animal1.birthType)

    print(animal1)

    print()
    mammal1 = Mammal()

    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print(mammal1)

    reptile1 = Reptile()

    print(reptile1.birthType)

    print(reptile1)

    print("Sum: {}".format(reptile1.sumAll(1,2,3,4,5)))

    getBirthType(mammal1)
    getBirthType(reptile1)




main()
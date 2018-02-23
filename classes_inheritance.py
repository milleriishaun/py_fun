import random
import sys
import os
import timeit

class Animal:
    name = ""
    height = 0
    weight = 0
    sound = 0 # the "" means private

    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = height
        self.sound = sound # the "" means private

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name # the passed name is valid

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height # the passed name is valid

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight # the passed name is valid

    def set_sound(self, sound):
        self.sound = sound

    def get_sound(self):
        return self.sound # the passed name is valid

    # polymorphism
    def get_type(self):
        print("Animal")
    
    def toString(self):
        return "{} is {}cm tall and {}kgs and says {}".format(self.name,
        self.height,
        self.weight,
        self.sound)

cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

# Inheritance... making a new class, you can inherit from the parent class
class Dog(Animal):
    owner = ""
    #overwrite the contructor
    def __init__(self, name, height, weight, sound, owner):
        self.owner = owner # every dog has an owner, but not every animal
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.owner = owner
    
    def get_owner(self):
        return self.owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {}cm tall and {}kgs and says {}. His owner is {}.".format(self.name,
        self.height,
        self.weight,
        self.sound,
        self.owner)

    # method overloading:
    # can perform different tasks based on the passed in attributes
    # we do not require attributes to be sent to our function iw/how_many=none
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)
    
chonchito = Dog('Choncho', 20, 50, 'Woof', 'Shaun')
print(chonchito.toString())

# Polymorphism:
# refer to objects as their superclass,
# and automatically have the correct functions called,
# automatically.
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(chonchito)

chonchito.multiple_sounds(4)
chonchito.multiple_sounds()

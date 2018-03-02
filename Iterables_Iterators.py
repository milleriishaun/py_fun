# Iterables
# Iterators
# List Comprehensions
# Generator Functions
# Generator Expressions

# Iterables: it is an object with a method(like __iter__)
# stored sequence of values; list of values
# 

# With Generators, Iterables can act as
# an obj that produces one value at a time

# Iterator: it is an object with a method(like __next__)

sampStr = iter("Sample")

print("Char: ", next(sampStr))
print("Char: ", next(sampStr))

# Add the iterator behavior to a custom class
# Alphebet, iterator through a string
class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]
    
alpha = Alphabet()

for letter in alpha:
    print(letter)


# Iterate through keys... b/c Dict is a iterable
# See that shaun.keys() was never needed
shaun = {"fName": "Shaun", "lName": "Miller"}

for key in shaun:
    print(key, shaun[key])
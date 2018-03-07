# 1
# splitting into many variables
# def solve_eq(equation):
    # x, add, num1, equal, num2 = equation.split()
# 
    # num1, num2 = int(num1), int(num2)
# 
    # return num2 - num1
# 
# print("In the equation, x + 1 = 5, x is", solve_eq("x + 1 = 5"))

# 2
# Return True or False
# then use that result in another funct

# 3
# Using the splat operator(*args)

# 4 string of characters is within list
randList = ["string", 444, 4.3]
first3 = randList[0:3]
print("string" in first3)

# 5
# Bubble Sort
# check if first item is > second item
# if so, switch index of the number
# import random
# import math
# 1. An outer loop decreases in size each time
# 2. The goal is to havethe largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so, swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

# numList = []
# for x in range(5):
#     numList.append(random.randrange(1, 10))
# i = len(numList) - 1
# while i > 0:
#     j = 0
#     while j < i:
#         print("\nIs {} > {}".format(numList[j], numList[j+1]))
#         if numList[j] > numList[j + 1]:
#             print("Switch")
#             temp = numList[j]
#             numList[j] = numList[j + 1]
#             numList[j + 1] = temp
#         else:
#             print("Don't Switch")
#         j += 1
#         for k in numList:
#             print(k, end = ", ")
#         print()
#     print("END OF ROUND")
#     i -= 1
# for k in numList:
#     print(k, end = ", ")
# print()

# 6
# List1.insert(5, 10)
# List1.remove(10)
# List1.pop(2)

# 7
# List COmprehension
# evenList = [i*2 for i in range(10)]

# for i in evenList:
#     print(i)

# 8
# multi-List Comprehension
# import math
# numList = [1,2,3,4,5]

# listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
#                 for m in numList]

# for i in listOfValues:
#     print(i)

# print()

# 9
# Lists of lists
# multiDList = [[0] * 10 for i in range(10)]
# [outside][inside]
# multiDList[0][1] = 10
# print(multiDList)

# 10
# Dictionaries

# 11
# File IO(practice reading data)
# myFile.read()
# myFile.readline()
# myFile.readlines()
# myFile.closed()
# myFile.name()
# myFile.mode()

# 12
# os modules
# import os
# os.rename("mydata.txt", "mydata2.txt")
# os.remove("mydata.txt", "mydata2.txt")
# os.mkdir("mydirectory")
# os.chdir("mynewdirectory")
# os.chdir("..")
# os.rmdir("mynewdirectory")

# 13
# Max and min of a tuple
# Adding more indices to the tuple

# 14
# def __str__(self):
# Use return "{}".format(type(self).__name__)

# 15
# overwrite function using super in class of a class
# def __str__(self):
    # return super().__str__() + " and it is {} they nurse".format(self.nurseYoung)

# 16
# call superclass for init of a subclass
# class Animal:
#     def __init__(self, birthType="Unknown",
#                 appearance="Unknown",
#                 blooded="Unknown"):

#         self.birthType = birthType
#         self.appearance = appearance
#         self.blooded = blooded

# class Reptile(Animal):
#     def __init__(self, birthType="born in an egg or born alive",
#                 appearance="dry scales",
#                 blooded="cold blooded"):
        
#         Animal.__init__(self, birthType, appearance, blooded)


# def main():
#     animal1 = Animal("born alive")

#     print(animal1.birthType)

#     reptile1 = Reptile()

#     print(reptile1.birthType)
#     print(reptile1)

# main()

# 17
# using except IndexError:

# 18
# Custom Exceptions
# class dogNameError(Exception):
#     def __init__(self):
#         Exception.__init__(self, *args, **kwargs)

# try:
#     dogName = input("What is your dog's name: ")
#     if any(char.isdigit() for char in dogName):
#         raise dogNameError # or raise NameError

# except dogNameError:
#     print("Your dog'sname can't contain a number")

# 19
# except ZeroDivisionError:

# 20
# except:
# else:
# finally:

# 21
# except FileNotFoundError as ex:
    # print("That file was not found")
    # print(ex.args)

# 22
# dynamically created function
# (function within a function)

# 23
# making a list of functions
# Datastructures

# 24
# function that returns False or True

# 25
# annotations and return types
# def random_funct(name: str, age: int, weight: float) -> str:
# print(random_funct("Shaun", 41, 160))
# print(random_funct.__annotations)

# 26
# lambda arg1, arg2: expression using args

# 27
# adding to a list, rather than appending
# import random
# flipList = []
# for i in range(1, 101):
#     flipList += random.choice(['H', 'T'])

# 28
# map
# print(list(map(dbl_num, onToTen)))

# 29
# filter
# print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# 30
# reduce
# from functools import reduce
# print(reduce((lambda x, y: x+y), range(1, 6)))

# 31
# for loop in for loop list comprehension

# 32
# list comprehension within list comprehension

# 33
# generators, only returns calculation when asked
# def for i in range(2, num):
#     if (num % i) == 0:
#         return False
#     return True

# def gen_primes(max_number):
#     for num1 in range(2, max_number):
#         if isprime(num1):
#             yield num1

# prime = gen_primes(50)

# print("Primes: ", next(prime))
# print("Primes: ", next(prime))
# print("Primes: ", next(prime))
# print("Primes: ", next(prime))
# print("Primes: ", next(prime))

# 34
# Generator Expressions
# (surrounded with parens)
# double = (x * 2 for x in range(10))

# print("Double: ", next(double))
# print("Double: ", next(double))

# for num in double:
#     print(num)

# 35
# Threading example

# 36
# import threading
# time.strftime
# thread = threading.Thread(target=executeThread, args=(i,))
# thread.start()
# threading.activeCount()
# threading.enumerate()

# 37
# 
import random
import math

randList = ["string", 1.234, 28]

# list of values 0 to 9
oneToTen = list(range(10))
print(oneToTen)

# strings are lists of characters
# lists can contain more than individual characters
randList = randList + oneToTen

# print first item of list
print(randList[0])

print("List Length: ", len(randList))

# use slice to get first 3 items(not including 4th)
first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# repeat a print of the item
print(first3[0] * 3)

print("string" in first3)

print("Index of string: ", first3.index("string"))

print("How many strings: ", first3.count("string"))

first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
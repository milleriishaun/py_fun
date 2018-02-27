import random
import math

numList = []

for x in range(5):
    numList.append(random.randrange(1, 10))

numList.sort()

for k in numList:
    print(k, end = ", ")
print()

numList.reverse()

for k in numList:
    print(k, end = ", ")
print()

# at index 5, which doesn't exist, put in value 10
numList.insert(5, 10)

for k in numList:
    print(k, end = ", ")
print()

numList.remove(10)

for k in numList:
    print(k, end = ", ")
print()

# remove an item at a specific index(2nd index)
numList.pop(2)

for k in numList:
    print(k, end = ", ")
print()


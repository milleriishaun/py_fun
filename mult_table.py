import random
import math


'''
# example of list comprehension
evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)

print()

oddList = [i*2 + 1 for i in range(10)]

for i in oddList:
    print(i)
'''

'''
# use multiple different calculations to make our list
# generate list of lists
numList = [1,2,3,4,5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()
'''

'''
# this makes 10 lists of lists of len(10)
multiDList = [[0] * 10 for i in range(10)]

print(multiDList)

multiDList[0][1] = 10

print(multiDList[0][1])

testList = [0]*5
# will this make a testList of len(5)?

print(testList)
# it does. Which is interesting.
# So that's how you identify how many indices.
# I used to simply use for x in range to define how many indices,
# because afterwards you an use append to add another index.
'''

'''
listTable = [[0]*10 for i in range(10)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)
    
for x in range(4):
    for y in range(4):
        print(listTable[x][y], end = " || ")
    print()
'''


# Generate a multiplication table
# Try 1
multTable = [[0]*10 for x in range(10)]

for x in range(1, 10):
    for y in range(1, 10):
        multTable[x][y] = x * y

for x in range(1, 10):
    for y in range(1, 10):
        print(multTable[x][y], end = ", ")
    print()

'''
# Pro's Try
# Create the multidimensional list
multTable = [[0]*10 for i in range(10)]

# Increment wit outer for loop
for i in range(1, 10):
    # increment with inner for
    for j in range(1, 10):
        # Assign with value to the cell
        multTable[i][j] = i*j

# Output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end = ", ")
    print()

'''
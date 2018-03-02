# Want to test this stuff to see if it is working correctly

# Map funtion:
# Allows us to execute a function on each item on a list

oneTo10 = range(1, 11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y: x + y), [1, 2, 3,], [1, 2, 3]))

print(aList)


# Filter:
# select items from a list based ona  function
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))


# This is how you use reduce
# Receives a list and returns a single result
from functools import reduce
# Adding up a some values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))

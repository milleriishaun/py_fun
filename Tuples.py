myTuple = (1,2,3,4,5,8)

print("1st Value: ", myTuple[0])

print(myTuple[0:3])

print("Tuple Length: ", len(myTuple))

moreFibs = myTuple + (13, 21, 34)

print("34 in Tuple: ", 34 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55, 89, 144]
aTuple = tuple(aList)

aList = list(aTuple)

print("Min: ", min(aTuple))
print("Max: ", max(aTuple))


# List comprehension
# does: launch an expression against an iterable, then condition for iterable
# while powerful, try not to make ones that are hard to understand

print(list(map((lambda x: x * 2), range(1, 11))))

print([2 * x for x in range(1, 11)])

print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

print([x for x in range(1, 11) if x % 2 != 0])

# Try 1, failure!(though it looked like success at first)
# Generate 50 values
# Take to the power of 2
# Return multiples of 8
print([x * x  for x in range(50) if (x * x) % 8 == 0])

# Pro's try
print([i ** 2 for i in range(50) if i % 8 == 0])

# Try 2, actually less complex
print([x * x for x in range(50) if x % 8 == 0])

print([x * y for x in range(1, 3) for y in range(11, 16)])

# list conprehension within list comprehension
# Generate a list of 10 values
# Multiply them by 2
# Return multiples of 8

print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# PROBLEM
# Generate a list of 50 random values between 1 and 1000
# And return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension

# Try 1, success, very easy(though he said it was hard)
import random
print([x for x in [random.randint(0, 1000) for y in range(50)] if x % 9 == 0])

# Pro's Try
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

# Actual correct way, Try 2
print([x for x in [random.randint(1, 1000) for i in range(50)] if x % 9 == 0])

# Another example:
# Create a multi-dimensional list using list comprehension
multiList = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print([col[1] for col in multiList])

# how to print the diagonals:
print([[diag[x] for x in range(len(multiList))] for diag in multiList])

for x in range(3):
    for diag in multiList:
        print(diag[x])

print([[row[x] for row in multiList] for x in range(len(multiList))])


# for row in range(len(multiList)):
#     for col in multiList:
#         print(col[row])



print(multiList[1][2])
print(multiList[1])
print(multiList)


print(multiList[0][0])
print(multiList[1][1])
print(multiList[2][2])
print()

# print([multiList for x in [multiList[y] for y in range(len(multiList[]))] in range(len(multiList))])
for y in range(3):
    print([multiList[x][x] for x in range(len(multiList))][y])
# the above doesn't even work since y is not being read

print([multiList[x][x] for x in range(len(multiList))])


# give up on this
# print([[multiList[x][x] for x in range(len(multiList))][y] for y in range(3)])



# for row in range(len(multiList)):
#     for col in range(len(multiList[row])):
#         print(multiList[row][col])

# print([multiList[col][row] for row in range(len(multiList))

# Real way to print the diagonals
# Well... this is the way that he wanted to have it done
# Personally I find it weird to have a list in the output
print([multiList[i][i] for i in range(len(multiList))])


# Solve for x
# x + 4 = 9
# x will always be the 1st value received and you only
# will deal with addition

'''
# Try 1
def solvex(string):
    list1 = []
    list1 = string.split()
    print(string)
    num2 = int(list1[4])
    num1 = int(list1[2])
    return "x = " + str(num2 - num1)

print(solvex("x + 4 = 9"))
'''

# Pro's Attempt
# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))

# Recursive Function example
def factorial(num1):
    if num1 <= 1:
        return 1
    else:
        result = num1 * factorial(num1 - 1)
        return result

x = int(input("Enter number to find factorial: "))
print("{}! = {}".format(x, factorial(x)))

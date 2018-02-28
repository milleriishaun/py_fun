# 1, 1, 2, 3, 5, 8
# Creating a Fibonacci recursive funct, Try 1, failed
'''
# Create a function for one fibonacci addition
def fibo(num1):
    if num1 <= 1:
        return 1
    else:
        list1 = [0]*num1
        list1.append(list1[num1-2] + list1[num1 - 1])
        num1 -= 1
        if result <= 1:
            return list1
        else:
            return fibo(num1)
'''

'''
# Try 2, Success!
# REMEMBER that a recursive function is like
# Fn = Fn-2 + Fn-1
def fibo(num1):
    # Add two previous values in the list
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        result = fibo(num1 - 2) + fibo(num1 - 1)
        return result

# Recall that addition, using next 2 in list, to get 3rd

# Finish the function when index number
# which matches the input number, is reached
x = int(input("Fibonachi of number: "))

# print the results
print("Fibonacci of {} is {}".format(x, fibo(x)))

# figure out how to define values
for i in range(x+1):
    print("{}".format(fibo(i)), end = "")
    if i < x:
        print(", ", end = "")
print('\nAll done!')
'''


# Pro's try
# 1, 1, 2, 3, 5, 8, 13

# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

# print(fib(3))

# 1st: result = fib(2) + fib(1): 2 + 1
# 2nd: result = (fib(1) + (fib(0)) + fib(0)) : 1 + 0

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        results = fib(n - 1) + fib(n - 2)
        return results

print(fib(3))
print(fib(4))
print(fib(5))

# Ask how many numbers they want
numFibValues = int(input("How many Fibonacci
    values should be found: "))

# loop while calling for each new number
i = 1

while i < numFivValues:

    fibValue = fib(i)

    print(fibValue)

    i += 1

# Print the result and increment
print("All done")




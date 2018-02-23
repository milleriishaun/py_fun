# Enter Calculation: 5 *6
# 5 * 6 = 30

# Store the user input of 2 numbersand the operator
num1, symbol, num2 = input("Enter Calculation: ").split()

#convert he stirns into integers
num1 = int(num1)
symbol = str(symbol)
num2 = int(num2)

# if + then we need to provide output based on addition

if symbol == '+':
    sum2 = num1 + num2
    outputt = sum2
elif symbol == '*':
    mult = num1 * num2
    outputt = mult
else:
    print("Unknown Symbol used")

# print the result
print("{} {} {} = {}".format(num1, symbol, num2, outputt))
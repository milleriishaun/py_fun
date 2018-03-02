# Advanced Functions
# Functions as Objects
# Function Annotations
# Lambda Anonymous Functions,
# Map
# Filter
# Reduce
# Bunch of Problems

def mult_by_2(num):
    return num * 2

# assign function to a name(variable)
times_two = mult_by_2

# pass a 4 into variable
print("4 * 2 =", times_two(4))

# can pass a function within another function
def do_math(func, num):
    return func(num)

print("8 * 2 = ", do_math(mult_by_2, 8))






# Dynamically defined Functions
def get_func_mult_by_num(num):
    # create a function within a funct
    def mult_by(value):
        return num * value
    # Return a function within a funct
    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 = ", generated_func(10))

# Embed our function into a data structure
listOfFuncs = [times_two, generated_func]

print("5 * 9 =", listOfFuncs[1](9))
# Generator functions... giving one value at a time
# returns a result generator everytime it is called, and you'll spend
# or resume during execution of your program to create results over time.
# We want to do this when we are trying to get a large number of results
# but we dont want to slow down our program by making all those results at the same time.
# This is called Threading.

# Use Generator to calc primes, and get the next prime
# instead of getting all the numbers at the same time and slowing the PC
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):

        if isprime(num1):
            # This makes it a generator
            yield num1

# reference to the generator
prime = gen_primes(50)

# go next, pass in prime... each time called, gen's a new prime number
# yield is like return, but using a generator
# using yield is better because it allows the iteration without
# doing a data dump. This allows the getting of a lot of data during excecution
# Not everything is running at the same time here.
# instead, it only runs the next iteration when it is called
# Using next is how it runs best... it is called each time through
# the next magic method
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))

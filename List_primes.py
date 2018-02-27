# We want to return a list of primes
# A prime can only be divided by 1 and itself
# 5 is a prime, dividing by 1 and 5 = positive factor, no remainder
# 6 is not prime, divisible by 1, 2, 3, 6

# Input the max prime
# Use a for loop and check if modulus == 0... if True... get prime
# make many small functions, it is better than one long function
'''
# Pro's method
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_primes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        # here is something I can do, using if is_prime(num1)
        # the 'if' statement automatically assumes you want 'True'.
        # num1 is also appended directly, where I had to convert to $.

        if is_prime(num1):
            list_of_primes.append(num1)
    
    return list_of_primes

max_num_to_check = int(input("Search for primes up to: "))

list_of_primes = get_primes(max_num_to_check)

for prime in list_of_primes:
    print(prime)
'''


# My rendition of pro's method(no peeking)
# We want to return a list of primes
# A prime can only be divided by 1 and itself
# 5 is a prime, dividing by 1 and 5 = positive factor, no remainder
# 6 is not prime, divisible by 1, 2, 3, 6

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    
    return True

def get_primes(max_num):
    list_of_primes = []
    for x in range(2, max_num):
        # remember that x here is the actual value we want.
        # Unnecessary True statement
        if is_prime(x) == True:
            list_of_primes.append(x)
        # remember the else and the continue statement are unnecessary.
         else:
             continue
    return list_of_primes

stored_primes = get_primes(int(input("Search for primes up to: ")))

# remember that prime is just a placeholder, which takes each index.
# prime is not always a number, but it can also store index values to a list.
for prime in stored_primes:
    print(prime)

# Try 1, success!
# though I did have to look up list comprehension
# Also had to review how to use filter
import random
list1 = [random.randint(0, 1000) for x in range(100)]
print(list(filter((lambda x: x % 2 == 0), list1)))


# Pro's Try
# Generate a random list with randint between 1 and 1000

# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))
# Use modulus to find multiples of 9
print(list(filter((lambda x: x % 9 == 0), randList)))




# Turns out I was pretty close and that I could get a lot done
# I was close andd the list comprehension that i used was appropriate
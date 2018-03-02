# Anonymous functions using Lambda
# Lambda is similar to "def"
# but def assigns a function to a name
# Lambda simply returns the function, no name
# though you can assign a lambda funct to a name

# format is: lambda arg1, arg2, .... : expression which uses the args
sum = lambda x, y: x + y
# lambda is typically used when you need a small function but you
# don't want to junk up your code with many temporary funtion names
# and increase name conflicts in your code

print("Sum: ", sum(4, 5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote: ", can_vote(19))

powerList = [lambda x: x ** 2,
            lambda x: x ** 3,
            lambda x: x ** 4]

for func in powerList:
    print(func(4))


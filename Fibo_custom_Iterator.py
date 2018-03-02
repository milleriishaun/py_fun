# Problem
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# Sample output:
# Fib: 1
# Fib: 2
# Fib: 3
# Fib: 5

'''
# Try 1, success, but barely
# sloppy and uncertain
import time

class fibo:

    def __init__(self, userInput=0):
        self.list1 = [0]
        self.index = -1
        self.userInput = userInput
        self.stopped = False

    def __iter__(self):
        return self

    def __next__(self):

        def calc_fibo():
            if self.index > 0:
                val = self.list1[self.index-1] + self.list1[self.index]
            else:
                val = 1
            return val

        if (self.index >= self.userInput):
            self.stopped = True
            return StopIteration

        self.index += 1
        (self.list1).append(calc_fibo())

        time.sleep(1)
        print("Fib: ", self.list1[self.index])
        

def main():
    user = int(input("Calculate Fibonacci(#): "))
    k = fibo(user)

    # k is treated as a list
    # x is treated as each index in the list
    # print(x) is print-calling every index of the list, but the list does not end
    # I need a way for the list calling to end
    # ...
    # this seems to work... but idk why
    # it is stuck in a loop but I'm not sure which
    # it prints out the x even though it says stopped iteration
    # that means it's stuck in the loop made by the for x in k
    # Therefore, it is good that it is going through k as a list
    # But it is not good that it is printing when the iter has stopped
    # OKAY, figured it out!
    # What happened was that I did not know I could call next from the
    # main function. To figure out why it actually was working,
    # I would say hat the loop was stuck because it wouls alswasy call
    # the magic methods when a new instance was creaeted.
    # The iter would not stop but __next__ would stop.
    # the next(k) allows me to control how long I can actually stay within
    # the calling of the whole
    # this is wrong:
    # for x in k:
    #     if k.stopped == True:
    #         break
    # this is right:
    for x in range(user+1):
        next(k)


main()
'''



# Pro's Try
# actually, this as a Fibonacci generator is wrong
# but it is a very sophisticated way of solving.
# I'll practice this until I get it right, because then I can use
# the strategy for other things.
'''
class FibGenerator:

    def __init__(self):
        self.first = 0
        self.second = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        # this is pretty smart... I should have thought of something
        # like this!
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum
def main():

    fibSeq = FibGenerator()
    user = int(input("How many Fibonacci solutions?: "))
    for x in range(user):
        print("Fibonacci: ", next(fibSeq))

main()
'''


'''
# Try 2, my rendition, no peeking, still a fail!!!!(maybe worse)
# This one I will try until I get right
# Problem
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# Sample output:
# Fib: 1
# Fib: 2
# Fib: 3
# Fib: 5

class generate:

    def __init__(self):
        self.list1 = [0]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.last = self.index
        if self.last == -1:
            self.last = 0
            self.first = 1
        else:
            self.first = 0
        self.index += 1
        self.current = self.index

        self.list1.append(self.list1[self.last] + self.list1[self.current]+ self.first)
        print("Fib: ", self.list1[self.current+1])


def main():
    call_gen = generate()
    userInput = int(input("Fibonacci of which number?: "))
    for x in range(userInput):
        next(call_gen)

main()
'''

# FIXED THE PROBLEM, BUT SOLUTION IS UGLY.(not much I can do here, but I'll try different ways of running this)
# ... hmmm let's fix this problem!
# Try 3, please get right this time... it is engrained
# (well I thought it was, but it seems that I am just copying from memory)
# the only way I know how to improve this is by going and adding the if states
class generate:

    def __init__(self):
        self.index = 0
        self.list1 = [0, 1]
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            fibNum = 0
            self.index += 1
            return fibNum
        elif self.index == 1:
            fibNum = 1
            self.index += 1
            return fibNum
        else:
            fibNum = (self.list1[self.index - 2] + self.list1[self.index - 1])
        self.index += 1
        self.list1.append(fibNum)
        return fibNum
    
def main():
    call = generate()
    user = int(input("How many Fibonacci solutions?: "))
    for x in range(user):
        print("Fibonacci: ", next(call))

main()

# Problem
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example output:
# Heads : 46
# Tails : 54



'''
# Try 1, success!, but looks a bit messy
import random
tosses = int(input("How many tosses?: "))
list1 = []
i = 0
j = 0
cointoss = {'heads': (lambda: 'Heads'),
            'tails': (lambda: 'Tails')}
for x in range(tosses):
    list1.append(cointoss[random.choice(list(cointoss.keys()))]())

for x in list1:
    if x == 'Heads':
        i += 1
    elif x == 'Tails':
        j += 1
    else:
        print("Wrong index")

print("Heads : {}".format(i))
print("Tails : {}".format(j))
'''


'''
# Pro's Try, which is so much cleaner

# for random choice
import random

# Create the list
flipList = []

# Populate the list with 100 Hs and Ts
for i in range(100):
    flipList += random.choice(['H', 'T'])

# Output the results
print("Heads :", flipList.count('H'))
print("Tails :", flipList.count('T'))
'''

'''
# Try 2, smallest I can think of right now
import random
list1 = ['H', 'T']
toss = ''
heads = 0
tails = 0
for x in range(100):
    toss = random.choice(list1)
    if toss == 'H':
        heads += 1
    else:
        tails += 1

print('Heads : ', heads)
print('Tails : ', tails)
'''

# Try 3, doing the function like Pro does
# wow it is very very similar!
import random

list1 = []

for x in range(100):
    list1 += random.choice(['H','T'])

print("Heads : {}".format(list1.count('H')))
print("Tails : {}".format(list1.count('T')))

import random
import sys
import os

grocery4 = ['Juice', "tomato", 'grapes']

print('First Item: ', grocery4[0])

print(grocery4)

grocery4[0] = "Green Juice"

print('Actual First Item: ', grocery4[0])

print(grocery4)
grocery4.insert(0, 'Toothpaste')
print(grocery4[0:5])
print(grocery4[0:4])

grocery4.append('Soap')

print(grocery4[0:5])

print(grocery4.extend(['more', 'and more']))

print(grocery4)

print(grocery4[0:7])

print('Number index of more: ', grocery4.index('more'))

other_events = ['Wash Car', 'Pick up', 'ash check']
to_do = [other_events, grocery4]
print(to_do)
print(to_do[1][0])
print('\n' *3, grocery4)
grocery4.append('Onions')
print(grocery4)

print(to_do)

grocery4.insert(1, 'Pickle')

# sorted() creates a new list
# sort() changes the old list, mutating it, and you cannot go back

print('\n'*2)
print("1 ", grocery4)
print("2 ", grocery4)
print("3 ", sorted(grocery4))
print("4 ", grocery4)
grocery4.sort() # Not printed
print("5 ", grocery4)

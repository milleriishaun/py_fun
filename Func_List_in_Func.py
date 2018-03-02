# Problem
# Create a function that recerives a list and a function
# The function passed will reuturn True or False if a list
# calue is odd.
# The surrounding function will return a list of odd numbers


'''
# Try 1, Success, but ugly!
def oddOrNot(list2):
    
    print()
    print("Are the values odd?\n")

    list3 = list(list2)
    for x in range(len(list3)):
        if list3[x] % 2 == 0:
            list3[x] = str(list3[x]) + ": False"
        elif list3[x] % 2 != 0:
            list3[x] = str(list3[x]) + ": True"
        else:
            print("???")
    
    for x in range(len(list3)):
        print(list3[x])
    
    return list3

def oddFinder(oddList, func):

    list1 = oddList
    list2 = tuple(oddList)

    for i in list1:
        if i % 2 == 0:
            list1.remove(i)
    
    return str(list1) + " is a truncated list of odd values\n"\
            "{} shows which values are odd".format(str(func(list2)))

list_of_vals = [324,5433,3,34,6325,6,34]
print(oddFinder(list_of_vals, oddOrNot))
'''


# Problem
# Create a function that recerives a list and a function
# The function passed will reuturn True or False if a list
# calue is odd.
# The surrounding function will return a list of odd numbers

'''
# Pro's Try
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list1, func):

    oddList = []
    print(list1)
    for i in list1:
        
        if func(i):

            oddList.append(i)
                
    return oddList
another_list = range(1, 22)
print(another_list)

# This is not a list, but he is using range to pass the list through
# the function which is kind of smart...
# What I did was turn it into an immutable tuple.
aList = range(1, 20)
print(aList)
print(change_list(aList, is_it_odd))
'''
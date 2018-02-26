# Random Access Memory: RAM


# first way of solving this problem
userinput = input("Enter the string of words: ")
# take out exterior extra spaces
userinput = userinput.strip()

list1 = userinput.split()
print("1st Acronym: ", end = "")
for x in range(0, len(list1)):
    capital = list1[x].capitalize()
    capital = capital[0]
    print(capital, end = "")

# Second way of solving this problem
print('\n')
print("2nd Acronym: ", end = "")
for x in list1:
    print(x[0].capitalize(), end = "")

print('\n')
# Third way of solving this problem
list2 = []
list2.append(userinput[0].capitalize())
for x in range(0, len(userinput)):
    if userinput[x] == " ":
        list2.append(chr(int(ord(str(userinput[x+1].capitalize())))))
list2string = "".join(list2)

print("3rd Acronym: ", list2string)

'''
# This is how the pro does it
# Ask for a string
orig_string = input("Convert to Acronym: ")

# Convert the string to uppercase
orig_string = orig_string.upper()

# Convert the string into a list
stringlist = orig_string.split()

# Cycle through the list
# REMEMBER, not all for loops have to use range
# This for loop uses x as a holder variable for each item in the list
# x can be treated as a list itself and put square brackets to find the letter
for x in stringlist:

    # Get the 1st letter' of the word and eliminate the newline
    print(x[0], end = "")

# Add a newline
print('\n')
'''
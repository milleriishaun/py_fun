# Receive an upercase string
# hide it's meaning by turning it into a string
# of unicodes
# then convert unicode back into string
'''
# This is my rendition
# Enter a string to hide in uppercase
while True:
    # recycle these lists for every new user input
    unicodes = []
    newstring = []
    try:
        # Get user input
        userinput = input("Enter a string in uppercase: ")
        inputcheck = 0

        # Verify user input
        for x in range(0, len(userinput)):
            if (ord(userinput[x]) >= 65) and (ord(userinput[x]) <= 90):
                inputcheck = "good input: "
                print("good input: ", userinput[x])
                continue
            elif (ord(userinput[x]) >= 97) and (ord(userinput[x]) <= 122):
                inputcheck = "bad input: "
                print("bad input: ", userinput[x])
                break
            else:
                inputcheck = "unknown character input"
                print("unknown character input: ", userinput[x])
                break

        # Check our conditions to cycle to next while loop
        if inputcheck == "good input: ":
            print("Inputs look good")
        elif inputcheck == "bad input: ":
            print("bad input: ", userinput[x])
            continue
        elif inputcheck == "unknown character input":
            print("unknown character input: ")
            continue
        else:
            print("something is not right with input")
            continue

        print('\n')
        # Convert the string into a string of unicodes
        for y in range(0, len(userinput)):
            unicodes.append(ord(userinput[y]))
            print("number: " + str(unicodes[y]))

        print("These are the unicodes: ", unicodes)
        print('\n')

        # Convert the string of unicodes into a string
        for z in range(0, len(userinput)):
            newstring.append(chr(ord(userinput[z])))
            print("letter: " + newstring[z])
        
        print("This is the list of strings: ", newstring)

        # Form the string from the list. Strings are immutable, not lists.
        reformed_string = ''.join(newstring)
        print("The list turned back into string: ", reformed_string)

        # Verify that the list is still available for other use.
        print("The list of strings is still here: ", newstring)
        print('\n')
    
    # Should have a except block for a value difference
    except ValueError:
        print("Wrong string format was stated")
        break
    # Can't hurt to have a catch-all except block
    except:
        print("Catch-all")
        break
'''

'''
# This is my second rendition, though
# instructional skeleton was not clear
# Receive an upercase string
# hide it's meaning by turning it into a string
# of unicodes
# then convert unicode back into string

# Enter a string to hide in uppercase: Hide
string = ""
need_list = []

# Secret Message: 35647890
message = 35647890

# Original Message : HIDE
original_message = "HIDE"

print("Secret Message: ", end ="")
# Cycle through each character in the string
for x in range(0, len(original_message)-1, 2):
# Store each character code in a new string
    string = str(ord(original_message[x])) + str(ord(original_message[x+1]))
# Print "Secret Message : 56349078"
    print(string, end = "")

secret_message = "56349078"
# Cycle through each character code 2 at a time by incrementing by 2 each time
print('\n')
p=0
for y in range(0, len(secret_message)-1, 2):
    # Get the 1st and 2nd for the 2 digit number
    need_list.append(secret_message[y] + secret_message[y+1])
    print("this: ", chr(int(need_list[p])))
    print(need_list)
    p += 1
'''

'''
# This is the pro's rendition

# Receive an upercase string
# hide it's meaning by turning it into a string
# of unicodes
# then convert unicode back into string

# Input "Enter a string to hide in uppercase"
norm_string = input("Enter a string to hide in uppercase: ")
secret_string = ""

# Cycle through each character in the string
for char in norm_string:

    # Store each character code in a new string
    secret_string += str(ord(char))

# Print "Secret Message : 56349078"
print("Secret Message: ", secret_string)

# Cycle through each character code 2 at a time by incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string)-1, 2):

    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]

    # Convert the code into characters and add them to a new string
    norm_string += chr(int(char_code))

# Print Original Messageg: HIDE
print("Original Message: ", norm_string)

'''

# Program rewrite for both lower case and uppercase
while True:
    # recycle these lists for every new user input
    unicodes = []
    newstring = []
    try:
        # Get user input
        userinput = input("Enter a string: ")
        inputcheck = 0

        # Verify user input
        for x in range(0, len(userinput)):
            if (ord(userinput[x]) >= 65) and (ord(userinput[x]) <= 90) or (ord(userinput[x]) >= 97) and (ord(userinput[x]) <= 122):
                inputcheck = "good input: "
                print("good input: ", userinput[x])
                continue
            else:
                inputcheck = "unknown character input: "
                print("unknown character input: ", userinput[x])
                break

        # Check our conditions to cycle to next while loop
        if inputcheck == "good input: ":
            print("Inputs look good")
        elif inputcheck == "unknown character input":
            print("unknown character input: ")
            continue
        else:
            print("something is not right with input")
            continue

        print('\n')
        # Convert the string into a string of unicodes
        for y in range(0, len(userinput)):
            unicodes.append(ord(userinput[y]))
            print("number: " + str(unicodes[y]))
            unicodes[y] = str(unicodes[y])

        # Form the string from the list. Strings are immutable, not lists.
        reformed_unicode = ''.join(unicodes)
        print("This is the secret message: ", reformed_unicode)
        print("These are the unicodes: ", unicodes)
        print('\n')

        # Convert the string of unicodes into a string
        for z in range(0, len(userinput)):
            newstring.append(chr(ord(userinput[z])))
            print("letter: " + newstring[z])
        
        print("This is the list of strings: ", newstring)

        # Form the string from the list. Strings are immutable, not lists.
        reformed_string = ''.join(newstring)
        print("The list turned back into string: ", reformed_string)

        # Verify that the list is still available for other use.
        print("The list of strings is still here: ", newstring)
        print('\n')
    
    # Should have a except block for a value difference
    except ValueError:
        print("Wrong string format was stated")
        break
    # Can't hurt to have a catch-all except block
    except:
        print("Catch-all")
        break
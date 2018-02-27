# Caesar's Cipher

# Second attempt
input1 = input("Enter string to Caesar encode: ")
input1 = input1.strip()
input2 = int(input("Enter the number to shift by(1-26): "))

def caesar_encrypt(string, shift_val):
    input_string = string
    list1 = []
    shift_amt = shift_val
    for x in input_string:
        char_x = ord(x)
        char_x += shift_val
        if x.isalpha() == True:
            if (65 <= ord(x) <= 90) and ((char_x) > 90):
                x = chr(ord(x) - 26)
            elif (65 <= ord(x) <= 90) and ((char_x) < 65):
                x = chr(ord(x) + 26)
            elif (97 <= ord(x) <= 122) and ((char_x) > 122):
                x = chr(ord(x) - 26)
            elif (97 <= ord(x) <= 122) and ((char_x) < 97):
                x = chr(ord(x) + 26)
            else:
                print(chr(char_x), end = "")
                list1.append(chr(char_x))
        else:
            list1.append(x)
    secret = ''.join(list1)
    return secret, shift_amt

def caesar_decrypt(string, shift_val):
    input_string = string
    list2 = []
    for x in input_string:
        char_x = ord(x)
        char_x -= shift_val
        if x.isalpha() == True:
            if (65 <= ord(x) <= 90) and ((char_x) > 90):
                x = chr(ord(x) - 26)
            elif (65 <= ord(x) <= 90) and ((char_x) < 65):
                x = chr(ord(x) + 26)
            elif (97 <= ord(x) <= 122) and ((char_x) > 122):
                x = chr(ord(x) - 26)
            elif (97 <= ord(x) <= 122) and ((char_x) < 97):
                x = chr(ord(x) + 26)
            else:
                print(chr(char_x), end = "")
        else:
            print(x, end = "")
            list2.append(x)
    decoded_message = ''.join(list2)
    return decoded_message

secret, shift_amt = caesar_encrypt(input1, input2)
print('\n' + "Caesar encrypted code: ", secret)
print('\n')

print('\n'+"Decoding Caesar encoding: ", secret)
decoded_message = caesar_decrypt(secret, shift_amt)
print('\n'+"Caesar decrypted message: ", decoded_message)


'''
def caesar_decrypt(string, shift_val):
    input_string = string
    input_shift = shift_val
    input_string += shift_val
    for x in input_string:
        if x.isalpha() = True:
            if (65 <= ord(x) <= 90) and ((ord(x) + input_shift) > 90):
                x = chr(ord(x) - 26)
            elif (65 <= ord(x) <= 90) and ((ord(x) + input_shift) < 65):
                x = chr(ord(x) + 26)
            elif (97 <= ord(x) <= 122) and ((ord(x) + input_shift) > 122):
                x = chr(ord(x) - 26)
            elif (97 <= ord(x) <= 122) and ((ord(x) + input_shift) < 97):
                x = chr(ord(x) + 26)
        else:
        print(x, end = "")
'''

'''
# This is how the pro did it and he had a smaller scope
# I made it harder for myself in allowing 52 character shift
# Receive the message to encrypt and number of shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))


# Prepare the secret_message
secret_message = ""

# Cycle through each character in the message
for char in message:

    # If it isn't a letter, then keep it as it is
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            if char_code < ord('A'):
                char_code += 26

    # Do the same for lowercase characters
        else:
            if char_code > ord('z'): 
                char_code -= 26
            if char_code < ord('a'): 
                char_code += 26
    # Convert from code to letter and add to message
        secret_message += chr(char_code)
    
    else:
        secret_message += char
    
print("Encrypted: ", secret_message)

key = -key

orig_message = ""
# Same as above but change all secret_messages to orig_message
# Cycle through each character in the message
for char in secret_message:

    # if it isn't a letter, then keep it as it is
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            if char_code < ord('A'):
                char_code += 26

    # Do the same for lowercase characters
        else:
            if char_code > ord('z'): 
                char_code -= 26
            if char_code < ord('a'): 
                char_code += 26
    # Convert from code to letter and add to message
        orig_message += chr(char_code)
    
    else:
        orig_message += char
    
print("Encrypted: ", orig_message)
'''
samp_string = "This sis a very important string"

# Print how long the string is
print("Len :", len(samp_string))

# Print Green four times right after each other
print("Green" * 4)

# Print the string one letter at a time
for char in samp_string:
    print(char)

# Print the string in pairs of letter
for i in range(0, len(samp_string)-1,2):
    print(samp_string[i] + samp_string[i+1])

# A-Z have unicodes 65-90
# a-z have unicodes from 97-122
print("A =", ord("A"))
print("65 =", chr(65))

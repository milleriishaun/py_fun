# Receive an upercase string
# hide it's meaning by turning it into a string
# of unicodes
# then convert unicode back into string

# Enter a string to hide in uppercase
while True:
    try:
        userinput = input("Enter a string in uppercase: ")
        inputcheck = 0
        for x in userinput:
            if (userinput[x] >= 65) and (userinput[x] <= 90):
                inputcheck = "good input"
                continue
            elif (userinput[x] >= 97) and (userinput[x] <= 122):
                inputcheck = "bad input"
            else:
                inputcheck = "unknown character input"
            if inputcheck == "bad input":
                print("bad input")
                break
            elif inputcheck == "unknown character input":
                print("unknown character input")
                break
            else:
                print("something is not right")
                break
        # Convert the string into a string of unicodes
        for y in userinput:
            userinput[y] = ord(userinput[y])
            print(userinput[y])

        # Conver the string o funicodes into a string
        for z in userinput:
            userinput[z] = chr(userinput[z])
            print(userinput[z])
            break
    except ValueError:
        print("Wrong string format was stated")
    except:
        print("Something went wrong with your input")

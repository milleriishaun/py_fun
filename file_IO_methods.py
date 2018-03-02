# 1. Create a file named mydata2.txt
# 2. Use what you learned in part 8 to find out
# how to open a file without "with" (Open in try)
# 3. Catch FileNotFoundError
# 4. In else print contents
# 5. In fanally
# 6. Open nonexistent file mydata3.txt
'''
# Try 1, success
try:
    file = open("mydata2.txt", "w", encoding="utf-8")
    file.write("Something is in\nthe file now,\nand it wants to\nplay")
    file = open("mydata2.txt", encoding="utf-8")
    list1 = file.read().splitlines()
except FileNotFoundError:
    print("Well, see the file has not been made yet...")
else:
    for x in list1:
        print(x)
finally:
    del file
    file = open("mydata3.txt", "w")
'''


'''
# Try 2, Success
try:
    file = open("mydata2.txt", "w", encoding="utf-8")
    file.write("Something is in\nthe file now,\nand it wants to\nplay")
    file = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError:
    print("Well, see the file has not been made yet...")

else:
    while True:
        list1 = file.readline()
        if not list1:
            break
        print(list1, end="")

finally:
    file.close()
    del file
    
    print("BARK BARK")

file = open("mydata3.txt", "w")
'''


# Pro's Rendition

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# use 'as' to access data and methods in the exception class
except FileNotFoundError as ex:
    print("The file was not found")

    print(ex.args)

else:
    print("File: ", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")

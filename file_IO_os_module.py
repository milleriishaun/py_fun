import os

with open("mydata.txt", mode = "w", encoding = "utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

print(myFile.mode)
with open("mydata.txt", encoding = "utf-8") as myFile:
    
    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

# simple os modules that are provided, updates within yoru operating system
os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

os.mkdir("mydir")

# change into new directory... like cd
os.chdir("mydir")

# current working directory
print("Current Directory: ", os.getcwd())

# move up one directory
os.chdir("..")

print("Current Directry: ", os.getcwd())
os.rmdir("mydir")


'''
import os

# simple example
with open("mydata2.txt", "w", encoding = "utf-8") as myFile:
    myFile.write("Bob\nSagat\nand\nCompany")

with open("mydata2.txt", encoding = "utf-8") as myFile:
    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break
        
        print("Line", lineNum, " : ", line, end = "")

        lineNum += 1
'''


'''
# Try myself, Try 1, Success!, just need practice

import os

with open("data.txt", "w", encoding = "utf-8") as f:
    f.write("There are many\nWords in this list\nOf words")

with open("data.txt", encoding = "utf-8") as f:
    lineNum = 1
    
    while True:
        line = f.readline()
        words = []
        total = 0
        if not line:
            break
        else:
            words = line.split()
            print(words)
            for x in words:
                total += len(x)
            # instead of using total
            # could have used:
            # for x in words:
                # for y in x:
                    count += 1
            
            print("Line ", lineNum, ": ", line.strip(), ": avg: ", total/(len(words)))
            lineNum += 1
'''


# Pro's Try
import os

with open("mydata2.txt", "w", encoding = "utf-8") as myFile:
    myFile.write("Bob is great\nSagat is not\nand\nCompany")

with open("mydata2.txt", encoding = "utf-8") as myFile:
    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break
        
        print("Line", lineNum)

        # split()
        wordList = line.split()

        # len()
        print("Number of Words: ", len(wordList))

        # loop count characters in the word list
        charCount = 0

        # double for loop was better than what I did
        for word in wordList:
            for char in word:
                charCount += 1
        
        # Divide character count / len word list
        avgNumChars = charCount/len(wordList)

        print("Avg Word Length: {:.2}".format(avgNumChars))

        lineNum += 1

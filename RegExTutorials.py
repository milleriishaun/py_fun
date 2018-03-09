# Regular Expressions
# locate and change strings!
# work nearly exactly the same in other languages

# Regular Expressions(Regex) are used to
# 1. Search for a specific string in a large amounts of data
# 2. Verify that a string has the proper format (Email, Phone #, etc.)
# 3. Find a string and replace it with another string correctly
# 4. Format data into the proper form for importing for example

# import re

# search and replace
# if re.search("ape", "The ape was at the apex"):
#     print("There is an ape")

# findall and print them
# putting a '.' after one of the 'ape', match any one character or any one space!
# notice with '.' you also get the space that comes after 'ape'
# allApes = re.findall("ape", "The ape was at the apex")

# for i in allApes:
#     print(i)

# theStr = "The ape was at the apex"

# for i in re.finditer("ape.", theStr):
#     # creates a tuple contianing the (start, end) positions.
#     locTuple = i.span()

#     print(locTuple)

#     print(theStr[locTuple[0]:locTuple[1]])

# animalStr = "Cat rat mat pat"

# allAnimals = re.findall("[Crmfp]at", animalStr)

# for i in allAnimals:
#     print(i)

# someAnimals = re.findall("[c-mC-m]at", animalStr)

# for i in someAnimals:
#     print(i)

# owlFood = "rat cat mat pat"

# pattern objects
# regex = re.compile("[cr]at")

# owlFood = regex.sub("owl", owlFood)

# print(owlFood)

# randStr = "Here is \\stuff"

# # Use r... raw string
# # doesnt work
# print("Find \\stuff :", re.search("\\stuff", randStr))
# # Does work
# print("Find \\stuff :", re.search("\\\\stuff", randStr))
# print("Find \\stuff :", re.search(r"\\stuff", randStr))

# randStr2 = "F.B.I. I.R.S. CIA"

# # Match a period(.) using a backslash, because regex hurts it
# print("Matches: ", len(re.findall(".\..\..\.", randStr2)))

# randStr3 = '''This is a long
# string that goes
# on for many lines
# '''

# print(randStr3)

# # remove the new lines
# regex = re.compile("\n")

# print(randStr3)

# # Removes the new lines, and replaces with a space
# randStr3 = regex.sub(" ", randStr3)

# print(randStr3)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# regex numbers
# matches anything 0 to 9:
# \d : [0-9]
# matches anything but the numbers 0 to 9:
# \D : [^0-9]

# randStr4 = "12345"

# print("Matches: ", len(re.findall("\d{2}", randStr4)))

# numStr = "123 12345 123456 1234567"

# Match 5, 6, or 7 numbers in a row
# print("Matches: ", len(re.findall("\d{5,7}", numStr)))



# Match any single letter and number
# \w : [a-zA-Z0-9_]
# \w : [^a-zA-Z0-9_]

# phNum = "412-555-1212"

# if re.search("\w{3}-\w{3}-\w{4}", phNum):
#     print("It is a phone number")

# Check a valid first name
# if re.search("\w{2,20}", "Ultraman"):
#     print("Valid name")

# shortcut for working with white space
# \s : [\f\n\r\t\v]
# \S : [^\f\n\r\t\v]

# if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    # print("Valid full name")

# Plus sign matches one or more characters
# print("Matches: ", len(re.findall("a+", "a as ape bug")))

# Problem
# Rules:
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numers,  plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

# Try 1, failed
# email = "numberonehero@gmail.com"
# print("Matches: ", len(re.findall("\w{1-20}@\w{2-20}.\w{2,3}", email)))

# Pro's try... works of course
# emaillist = "db@aol.com m@.com @apple.com db@.com numberonehero@gmail.com"

# print("Email Matches: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emaillist)))


# Try 2, success!
# x = "agdfgaf@gmail j@fjj.com JEIIii1123@gmail.com akfjsdfkFEFDF@fail.s"
# str2 = re.finditer("[A-Za-z0-9_.%+-]{1,20}@[A-Za-z0-9.-]{2,20}\.[A-Za-z]{2,3}", x)
# for i in str2:
#     r = i.span()
#     print(r)
#     print("{}:{}".format(r[0], r[1]))

# SUMMARY of REGEX

# if research("REGEX", yourString)
# print("Matches: ", len(re.findall("REGEX", yourString)))
# regex = re.compile("REGEX") # create a pattern method like regex.sub
# yourString = regex.sub("substitution", yourString)

# how do you match for zero or more?
# use *

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# [ ]  : Match what is in the brackets
# [^ ] : Match anything not in the brackets
# .    : Match any 1 character or space
# +    : Match 1 or more of what proceeds
# \n   : Newline
# \d   : Any 1 number
# \D   : Anything but a number
# \w   : Same as [a-zA-Z0-9_]
# \W   : Same as [^a-zA-Z0-9_]
# \s   : Same as [\f\n\r\t\v]
# \S   : Same as [^\f\n\r\t\v]
# {5}  : Match 5 of what proceeds the curly brackets
# {5,7}: Match values that are between 5 and 7 in length

# Tutorial 2 about REGEX
'''
import re

randStr = "cat cats"

# match one or more using "+"
# match for zero or one of whatever proceeds it, "s?"

regex = re.compile("[cat]+s?")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# how do you match for zero or more?
# use *

randStr = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]*")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

# New Problem!
# create a regex that grabs each line of a string
randStr = Just some words
and some more\r
and more

regex = re.compile("[\w\s]+[\r]?\n")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

# Difference between Greedy and Lazy matching
# astricks is greedy... grabs biggest match possible
# rather than grabbing the first match
# To fix it, make it lazy... meaning grab the smallest match possible
# by adding ?
# can use subexpressions too ()
# can use largest possible match using +? or {n,}?... practice.
# lazy = grab the smallest match possible
# greedy = grab the largest match possible

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"
regex = re.compile("<name>.*?</name>")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)


# Word boundaries to define where matches start and end
# \b matches the start and the end of the word
# r for raw string
# want ape but not apex
randStr = "ape at the apex"
regex = re.compile(r"\bape\b")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i)


# String boundaries
# ^ : Beginning of the string
# $ : End of the string
# * means zero or more of the symbol before... which is are characters
randStr = "@ Get this string"
regex = re.compile(r"[^@\s].*")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i)


# Target each line in multiline string using ^
randStr = Ape is big
Turtle is slow
Cheetah is fast

regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i)



# Sub-expressions: pat of a large expression
# getting a block of what we want from what we have using parens
# used the 412 to find the start position of what we wanted
randStr = "My number is 412-555-1212"
regex = re.compile(r"412-(.*)")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i)

# Sub-expressions: pat of a large expression
# getting a block of what we want from what we have using parens
# used the 412 to find the start position of what we wanted
randStr = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i)



randStr = "My number is 412-555-1212"
regex = re.compile(r"412-(.*)-(.*)")
matches = re.findall(regex, randStr)
print(len(matches))

# first match
print(matches[0][0])
print(matches[0][1])

'''
# Tutorial 3 About REGEX


# SUMMARY of REGEX

# import re

# if re.search("REGEX", yourString)
# print("Matches: ", len(re.findall("REGEX", yourString)))
# regex = re.compile("REGEX") # create a pattern method like regex.sub
# yourString = regex.sub("substitution", yourString)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# [ ]  : Match what is in the brackets
# [^ ] : Match anything not in the brackets
# ( )  : Return surrounded submatch
# .    : Match any 1 character or space
# +    : Match 1 or more of what proceeds
# ?    : Match 0 or 1
# *    : Match 0 or More
# *?   : Lazy match the smallest match
# \b   : Word boundary
# ^    : Beginning of String
# $    : End of String
# \n   : Newline
# \d   : Any 1 number
# \D   : Anything but a number
# \w   : Same as [a-zA-Z0-9_]
# \W   : Same as [^a-zA-Z0-9_]
# \s   : Same as [\f\n\r\t\v]
# \S   : Same as [^\f\n\r\t\v]
# {5}  : Match 5 of what proceeds the curly brackets
# {5,7}: Match values that are between 5 and 7 in length
# ($m) : Allow ^ on multiline string

# Back References, Look Ahead, Look Behind, Negtive Look Ahead, Negative Look Behind
# # regex

# randStr = "the cat cat fell out the window"


# matches = re.findall(re.compile(r"(\b\w+)\s+\1"), randStr)

# print("Matches: ", len(matches))

# for i in matches:
#     print(i)


# this is to get the right number withhout the references
# randStr = "<a href='#'><b>The Link</b></a>"


# matches = re.findall(re.compile(r"<b>(.*?)</b>"), randStr)
# print(randStr)

# randStr = re.sub(re.compile(r"<b>(.*?)</b>"), r"\1", randStr)

# print(randStr)

# print("Matches: ", len(matches))

# for i in matches:
#     print(i)



# this is to get the right number with the references
# randStr = "412-555-1212"

# regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")

# randStr = re.sub(regex, r"(\1)\2", randStr)

# print(randStr)

# Problem
# Pro's Try... really smart guy
# randStr = "https://www.youtube.com/ https://www.google.com/"

# regex = re.compile(r"(https?://([\w.]+/))")

# print(regex)

# randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

# print(randStr)




# # Try 1, my real attempt, close but failed

# # randStr = "https://www.youtube.com/ https://www.google.com/"

# # # Failed regex
# # # regex = re.compile(r"(https?://([\w.*?])/)")

# # # correct-ish regex below
# # regex = re.compile(r"(https?://([\w.]+/+))")

# # randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

# # print(randStr)





# # # Lookaheads match patterns but don't return
# # randStr = "One two three four"

# # # practice using split using regex
# # # matches = re.split(r'\s', randStr)
# # # this is a lookahead
# # regex = re.compile(r"\w+(?=\b)")
# # # this is a lookbehind
# # # regex = re.compile(r"\w+(?<=\b)")

# # matches = re.findall(regex, randStr)
# # print(matches)

# # for i in matches:
# #     print(i)


# # Try 1, off by 1 + in the group( )
# # Lookbehinds match patterns but don't return
# randStr = "1. Bread 2. Apples 3. Lettuce"

# # practice using split using regex
# # matches = re.split(r'\s', randStr)
# # this is a lookahead
# # regex = re.compile(r"\w+(?=\b)")
# # this is a lookbehind
# regex = re.compile(r"(?<=\d\.\s)\w+")

# matches = re.findall(regex, randStr)
# print(matches)

# for i in matches:
#     print(i)




# # Try 1, close, only got one expression the first time
# # Lookbehinds and lookaheads
# randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"

# # attempt 1, this succeeded actually because I got the string wrong
# # regex = re.compile(r"(?<=<h1>)\w.*?(?=</h1>)")

# # attempt 2
# regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")

# matches = re.findall(regex, randStr)
# print(matches)

# for i in matches:
#     print(i)




# # Negative Look Behind
# # Try 1, failed
# # (?!expression) : Negative Look Ahead
# # (?<!expression) : Negative Look Behind

# # we do this by loooking for text that doesn't match our pattern
# randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"

# # Say you simply want how many individual items are actually there
# # Failed Try 1
# # regex = re.compile(r"(?<![A-Za-z0-9])\w+?(?![A-Za-z0-9])", randStr)

# # Pro's Try, he actually just looks for the number and no $
# regex = re.compile(r"(?<!\$)\d+")

# # the output of a negative lookbehind comes out as a string
# # so use len(matches)
# matches = re.findall(regex, randStr)

# print(len(matches))

# # for i in matches:
# #     print(i)

# # uses a list comprehension to turn all the index strings in matches
# # into integers
# # This list comprehension is doing more than initially thought
# # It is actually modifying list(map) with a function to get all
# # indices into intger indices.

# # Import the module for reduce
# from functools import reduce

# matches = [int(i) for i in matches]

# # This list comprehension could be written as 
# list1 = []
# for i in matches:
#     list1.append(int(i))
# print(list1)
# print("Total Items: {}".format(reduce((lambda x, y: x + y), list1)))

# # Print matches
# print(matches)


# # once he gets all the integers, he reduces them in order to get lambda
# # instead of matches list, we usually use range(), but any iterable works
# # Reduce gets a single result from a list
# print("Total Items: {}".format(reduce((lambda x, y: x + y), matches)))



# Tutorial 4 of REGEX


import re

# if re.search("REGEX", yourString)
# print("Matches: ", len(re.findall("REGEX", yourString)))
# regex = re.compile("REGEX") # create a pattern method like regex.sub
# yourString = regex.sub("substitution", yourString)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# [ ]  : Match what is in the brackets
# [^ ] : Match anything not in the brackets
# ( )  : Return surrounded submatch
# .    : Match any 1 character or space
# +    : Match 1 or more of what proceeds
# ?    : Match 0 or 1
# *    : Match 0 or More
# *?   : Lazy match the smallest match
# \b   : Word boundary
# ^    : Beginning of String
# $    : End of String
# \n   : Newline
# \d   : Any 1 number
# \D   : Anything but a number
# \w   : Same as [a-zA-Z0-9_]
# \W   : Same as [^a-zA-Z0-9_]
# \s   : Same as [\f\n\r\t\v]
# \S   : Same as [^\f\n\r\t\v]
# {5}  : Match 5 of what proceeds the curly brackets
# {5,7}: Match values that are between 5 and 7 in length
# ($m) : Allow ^ on multiline string

# Use a backreference to substitute what is between the
# bold tags and eliminate the bold tags
# re.sub(r"<n>(.*?)</b>", r"\1", ranfStr)

# Use a lookahead to find all characters of 1 or more
# with a word boundary, but don't return the word
# boundary.
# re.findall(r"\w+(?=\b)", randStr)

# Use lookbehind to find words starting with a number,
# period, and space, but only return the word that follows
# re.findall(r"(?<=\d.\s)\w+", randStr)

# Use a negative lookbehind to only reutrn numbers without
# a $ in front of them
# re.findall(r"(?<!\$)\d+", randStr)



# # using the (or) differentiator, which is a pipe |
# randStr = "1. Dog 2. Cat 3. Turtle"

# # just grab the dog and cat
# # wrong regex... though very close... use the parens instead
# # of the square brackets
# # regex = re.compile(r"\d+?\.\s(Cat|Dog)")

# # Pro's regex
# regex = re.compile(r"\d\.\s(Cat|Dog)")

# matches = re.findall(regex, randStr)

# for x in matches:
#     print(x)





# Problem
# Create a regex that matches for 5 digit zip codes,
# or those for dash and thenn four digits

# zipCodes = "12356 12345-1244 1234 12346-633"

# Try 1, failed recompile, regex
# close but forgot the space!
# the space determines if the regex will continue
# regex = re.compile(r"[\d]{5}\s|[\d]{5}-[\d]{4}")

# # Correct regex
# # regex = re.compile(r"\d{5}-\d{4}|\d{5}\s")

# matches = re.findall(regex, zipCodes)

# for x in matches:
#     print(x)

# print(matches)




# Group can be used to get parts of certain matches
# bd = input("Enter BD(mm-dd-yyyy)(use 01 if first day or month): ")
# bd = "55-55-3335"
# bdRegex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)

# print("You were born on ", bdRegex.group())
# print("Birth Month: ", bdRegex.group(1))
# print("Birth Day: ", bdRegex.group(2))
# print("Birth Year: ", bdRegex.group(3))

# if bdRegex:
#     print("True@ER!")




# Match Object Functions
# match = re.search(r"\d{2}", "The chicken weighed 13 lbs")

# print("Match: ", match.group())
# print("Span: ", match.span())
# print("Start: ", match.start())
# print("End: ", match.end())



# # Named Groups
# randStr = "December 21 1974"

# regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"

# matches = re.search(regex, randStr)

# # remember only re.findall() gives backa list
# # re.search() only gives one value... in this case we hide that
# # value in the Named Groups.
# # for x in matches:
# #     print(x)

# # This would be great for use input
# print("Month: ", matches.group('month'))
# print("Day: ", matches.group('day'))
# print("Year: ", matches.group('year'))





# Problem 1
# randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"

# regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-ZA-Z0-9-]+\.[a-zA-Z0-9-.]+")

# matches = re.findall(regex, randStr)

# for x in matches:
#     print(x)





# Problem 2, Try 1, VICTORY!
randStr = "14125551212 4125551212 (412)5551212 412 555 1212 "\
    "412-55-1212 1-412-555-1212"

# Try 1 answer
# regex = re.compile(r"1?\d{10}|\d{3}\s\d{3}\s\d{4}|[(]\d{3}[)]\d{7}|\d{3}-\d{3}-\d{4}|1-\d{3}-\d{3}-\d{4}")

# Pro's answer, this is actually really involved and I want to try this.
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\))?(\d{3})(-| )?(\d{4}|\d{4}))")

matches = re.findall(regex, randStr)

# for x in matches:
#     print(x)

for x in matches:
    print(x[0].lstrip())






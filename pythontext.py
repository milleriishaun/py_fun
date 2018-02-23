import random
import sys
import os
import timeit

# open first file, and write values to it
with open("test_file1.txt", 'w+', encoding = 'utf-8') as f1:
    f1.write("one\n")
    f1.write("two\n")
    f1.write("three\n")
    f1.write("four\n")
    f1.write("five")
# read each line in the file, and put into list

with open("test_file1.txt", 'r', encoding = 'utf-8') as f1:
    list1 = f1.read().splitlines()

# print new list
print(list1)
print('\n')

with open("test_file2.txt", 'w+', encoding = 'utf-8') as f2:
    f2.write("three\n")
    f2.write("four\n")
    f2.write("five\n")
    f2.write("six\n")
    f2.write("seven")
    # read each line in the file, and put into list
with open("test_file2.txt", 'r', encoding = 'utf-8') as f2:
    list2 = f2.read().splitlines()

# print new list
print(list2)
print('\n')

# add the two lists, then dedup the resultant list
#store the new list
list3 = list(dict.fromkeys(list1 + list2))

# print the new list
print(list3)
print('\n')

# write the new list to a new file
with open("final_file.txt", 'w+', encoding = 'utf-8') as f3:
    # write the new list with new line for each index
    f3.write('\n'.join(list3))

# print the list to check to see the order is the same
print(list3)

# change the reading the file now
with open("final_file.txt", 'r', encoding = 'utf-8') as f3:
# check that the list can be read on different lines
    list4 = f3.read().splitlines()

# don't need to create a new pointer... but I want to
listcheck = list4
# see if the print can work
print(listcheck)

# print the end
print("2 files created: text_file1.txt, text_file2.txt\nduplicates removed\nresultant is stored in final_file.txt")

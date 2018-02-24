'''
# Tree Attempt from Noob(Success 1)
tree = input("How tall is the tree?: ")

tree = int(tree)
hashes = '#'
indents = ' '

print('\n')

x = 0
while x <= tree:
    print(indents * (tree - x), end = "")
    print((hashes * ((1 + (x * 2)))) + '\n', end = "")
    if x == tree:
        print((indents*tree) + hashes)
    x += 1
print('\n' + "Christmas came early!")
'''

'''
# Tree like a Noob(Success 2)-->

# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces : 9 hashes

# Need to do
# 1. Decrement spaces by 1 each time through loop
# 2. Increment the hashes by 2 each time through loop
# 3. Save spaces to the stump by calcing tree height
# 4. Decrement from the tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

tree = input("How tall is the tree?: ")

tree_original = int(tree)
tree_height = int(tree)
spaces = tree_height
hashes = 1

while tree_height >= 0:
    print((' ' * spaces) + ('#' * hashes))
    spaces -= 1
    hashes += 2
    tree_height -= 1
    if tree_height < 0:
        print((' ' * tree_original) + '#')

print('Merry Christmas!')
'''


# Tree like a Professional-->

# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces : 9 hashes

# Need to do
# 1. Decrement spaces by 1 each time through loop
# 2. Increment the hashes by 2 each time through loop
# 3. Save spaces to the stump by calcing tree height
# 4. Decrement from the tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("How tall is the tree: ")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces til later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while tree_height != 0:

# print the spaces
# end=""
    for i in range(spaces):
        print(' ', end = "")

# Print the hashes
    for i in range(hashes):
        print('#', end = "")

# Newline after each row is printed
    print()

# That spacecs is decremented by 1 each time
    spaces -= 1

# That that hashes is incrementered by 2 each time
    hashes += 2

# Decrement tree height each time to jump out of loop
    tree_height -= 1

# Print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end = "")

print('#')
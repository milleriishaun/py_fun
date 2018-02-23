# Problem: Recieve miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

usermiles = input('Enter number of miles: ')
miles = int(usermiles)
kilometers = miles * 1.60934
print("{} miles equals {:{prec}} kilometers".format(miles, kilometers, prec = '.3'))

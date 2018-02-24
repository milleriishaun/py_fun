'''
# FIRST method of calculating present_value
# Have the user enter their investment amount
# and expected interest
invested = input("Enter how much you have invested: ")
# Each year their investment will increase by their
# investment + their investment * interest
time = 10
interest = -0.07
present_value = ((int(invested)) / (2.71828**(interest * time)))
# Print out the earnings ager a 10 year period
print("Earnings after 10 years: {}".format(present_value))
'''

#SECOND method of calcing present_value
# User enters investment amount and interest rate
# Each year, investment will increase by inv+(inv*rate)
# Print of the earnings after a 10 year period

# Ask for the $ invested + interest rate
inv, rate = input("Enter investment amount and rate(ex.1000 3): ").split()

# convert the value to a float
inv = float(inv)
rate = float(rate)
rate = rate*(-0.01)
# Convert value to a float and round the % rate by 2 digits
# Cycle through 10 years using the for loop and range 0 to 9
for x in range(1,11):
    present_value = inv / (2.71828**(x * rate))
    # Output the results
    print("End of Year {}, Earnings= {:.2f}".format(x-1, present_value))

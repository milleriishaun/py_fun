

# Customer list, my rendition, Try 1
customers = []

# Need a while loop to continue the quesses
while True:
    # use try except model for interacting iwth the user and not quitting
    try:
        # Get user input in correct format
        trial = input("Enter Customer (Yes, No): ").lower().strip()
        # if yes, ask their name, format should be firstName lastName
        if trial[0] == "y":
            # Assign variables the split names
            fName, lName = input("Enter customer first name and last name: ").split()
            # Append the dicitonary values into the list
            # Customers is a list of key, value pairs
            customers.append({'fName': fName, 'lName': lName})
            # Ask again to see if there is another name to input
            continue
        elif trial[0] == "n":
            # if they are not entering a customer name, they probably want tosee the list
            # REMEMBER that this could have been:
            for k in customers:
                print(k['fName'], k['lName'])
            # Rather than:
            # for k in range(0, len(customers)):
            #     print(customers[k].get("fName"), customers[k].get("lName"))
                # Show the list, first seeing which position in list, then using dictionary commands
            # Allow asking again
            continue
        else:
            # if not in right format, re-ask 
            print("Input a correct value")
            continue
    except ValueError:
        print("Value error occured")
        break

# Print these just to make sure
print("reached the end")
print(customers)




'''
# Pro's rendition

# Create an list
customers = []

# Create a loop
while True:

    # Get input and make it work for y or n
    createEntry = input("Enter Customer (Yes/No): ")
    createEntry = createEntry[0].lower()

    # Check to leave loop
    if createEntry == 'n':
        break

    # Get customer data
    else:
        fName, lName = input("Enter Customer Name: ".split())
    
    # Add customer data to list
    customers.append({'fName': fName, 'lName': lName})

# Print customer data
for cust in customers:
    print(cust['fName'], cust['lName'])
'''

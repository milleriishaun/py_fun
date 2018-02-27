shaunDict = {"fName": "Shaun", "lName": "Miller",
             "address": "123 Main St."}

print("May Name: ", shaunDict["fName"])


shaunDict["address"] = "222 North St."

# dictionaries are nonsequential but it looks like they come out at the same time
print(shaunDict)
print(shaunDict)
print(shaunDict)
print(shaunDict)


shaunDict['city'] = 'Sunnyvale'

print("Is there a city: ", "city" in shaunDict)

print(shaunDict.values())
print(shaunDict.keys())

for k, v in shaunDict.items():
    print(k, v)

# Middlename pritns Not Here, but lName prints right value
print(shaunDict.get("mName", "Not Here"))

del shaunDict["fName"]

# loop through dictionary
for i in shaunDict:
    print(i)
    
shaunDict.clear()

employees = []

fName, lName = input("Enter Employee Name: ").split()

employees.append({'fName': fName, 'lName': lName})

print(employees)


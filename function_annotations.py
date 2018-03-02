# Function Annotations
# Can define the datatypes of attributes and the return values
# Mainly used for documentation, doesn't change anything

def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Shaun", 41, 165.5))

print(random_func(89, "Shaun", "Turtle"))

print(random_func.__annotations__)

# Use magic methods to define hwo operators work
# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : Less Than
# __gt__ : Greater Than
# __le__ : Less Than or Equal
# __ge__ : Greater Than or Equal
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __div__ : Division
# __mod__ : Modulus

#__init__ : Initialization
#__str__ : String
'''
# Make a custom class called Time
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour,
                                        self.minute, self.second)
    
    # Demonstrate the __add__ MAGIC METHOD
    def __add__(self, other_time):
        new_time = Time()
        
        # Add the seconds and correct if sum >= 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second

        # Add the minutes and correct if sum is >= 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute - other_time.minute

        # Add the hours and orrect if sum is > 24
        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour - other_time.hour
        
        return new_time


def main():
    time1 = Time(1, 20,30)

    print(time1)

    time2 = Time(24, 41, 30)

    print(time1 + time2)


main()
'''

# My attempt at doing all of this myself, Try 1, try again later
# trying this again later wil help me get a lot more dones
class Time:

    def __init__(self, second=0, minute=0, hour=0):
        self.second = second
        self.minute = minute
        self.hour = hour
    
    def __str__(self):
        return "{:02d}:{:02d}:{:02d} is the time".format(self.second,
                                                        self.minute,
                                                        self.hour)

    def __add__(self, other_time):
        new_time = Time()

        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second
        
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        if (self.hour + other_time.hour) >= 24:
            self.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour
        
        return new_time

def main():

    time1 = Time(1, 20, 30)

    time2 = Time(24, 41, 30)

    print(time1)

    print(time2)

    print(time1 + time2)


main()
'''
import random
# Sam attacks Paul and deals 9 damage
# Paul is down to 10 halth
# Paul attacks Sam and deals 7 damage
# Sam is down to 7 health
# Sam attacks Paul and deals 19 damage
# Paul is down to -9 health
# Paul has Died and Sam is Victorious
# Game Over


# Long attempt at battle, Try 1, Success!
class warrior:
    def __init__(self, name="", health="20", resiliance="0"):
        self.name = name
        self.health = health
        self.resiliance = resiliance
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.isalpha():
            self.__name = value
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value.isdigit():
            self.__health = value

    @property
    def resiliance(self):
        return self.__resiliance
    
    @resiliance.setter
    def resiliance(self, value):
        if value.isdigit():
            self.__resiliance = value

    def attacked(self, value, new_res):
        return int(self.__health) - value + new_res


def main():
    # Create the two warriors
    warrior1 = warrior()
    warrior2 = warrior()
    
    # Loop for the battle sequence
    while True:
        # Try/Except blocks for user inputs
        try:
            aname1 = input("Name the first warrior(A-Z): ")
        except ValueError:
            print("use a different name")
        try:
            ahealth1 = input("Health of the warrior(#): ")
        except ValueError:
            print("use an appropriate amount of health")
        try:
            aresiliance1 = input("How resiliant is the warrior(0-10): ")
            if (int(aresiliance1) < 0) or (int(aresiliance1) > 10):
                aresiliance1 = 'valueerror'
        except ValueError:
            print("use an appropriate amount of resiliance")
        
        try:
            aname2 = input("Name the second warrior(A-Z): ")
        except ValueError:
            print("use a different name")
        try:
            ahealth2 = input("Health of the warrior(#): ")
        except ValueError:
            print("use an appropriate amount of health")
        try:
            aresiliance2 = input("How resiliant is the warrior(0-10): ")
            if (int(aresiliance2) < 0) or (int(aresiliance2) > 10):
                aresiliance2 = 'valueerror'
        except ValueError:
            print("use an appropriate amount of resiliance")
        break

    
    # Assign the user inputs to the warrior objects
    warrior1.name = aname1
    warrior1.health = ahealth1
    warrior1.resiliance = str(random.randrange(1, int(aresiliance1)+1))

    warrior2.name = aname2
    warrior2.health = ahealth2
    warrior2.resiliance = str(random.randrange(1, int(aresiliance2)+1))

    # New loop for the battle sequence
    while True:

        # Enter damage amounts
        damage1 = random.randrange(1,11)
        damage2 = random.randrange(1,11)

        # Keep resiliance less than damage
        if (int(warrior1.resiliance) > damage2):
            warrior1.resiliance = str(damage2)
        if (int(warrior2.resiliance) > damage1):
            warrior2.resiliance = str(damage1)

        # Call attacked() to affect health
        if (int(warrior1.health) - damage2) < 0:
            warrior1.health = str(0)
            if (int(warrior2.health) - damage1) < 0:
                warrior2.health = str(0)
            # Bug saying that you can't convert a negative number into a string
        else:
            warrior1.health = str(warrior1.attacked(damage2, int(warrior1.resiliance)))
            warrior2.health = str(warrior2.attacked(damage1, int(warrior2.resiliance)))
        
        # Battle sequence
        if int(warrior1.health) > 0:
            print("{}({}) attacks {} and deals {} damage".format(warrior1.name, warrior1.resiliance, warrior2.name, damage1))
            print("{}({}) is down to {} health".format(warrior2.name, warrior2.resiliance, warrior2.health))
        elif int(warrior1.health) <= 0:
            print("{}({}) attacks {} and deals {} damage".format(warrior2.name, warrior2.resiliance, warrior1.name, damage2))
            print("{}({}) has Died and {} is Victorious".format(warrior1.name, warrior1.resiliance, warrior2.name))
            print("Game Over")
            break
        else:
            print("Something went wrong")

        if int(warrior2.health) > 0:
            print("{}({}) attacks {} and deals {} damage".format(warrior2.name, warrior2.resiliance, warrior1.name, damage2))
            print("{}({}) is down to {} health".format(warrior1.name, warrior1.resiliance, warrior1.health))
        elif int(warrior2.health) <= 0:
            print("{}({}) attacks {} and deals {} damage".format(warrior1.name, warrior1.resiliance, warrior2.name, damage1))
            print("{}({}) has Died and {} is Victorious".format(warrior2.name, warrior2.resiliance, warrior1.name))
            print("Game Over")
            break
        else:
            print("Something went wrong")

        # Reset the resiliance to random value from 1 to user input
        warrior1.resiliance = str(random.randrange(1, int(aresiliance1)+1))
        warrior2.resiliance = str(random.randrange(1, int(aresiliance1)+1))

# Start the main loop
main()
'''

# Sam attacks Paul and deals 9 damage
# Paul is down to 10 halth
# Paul attacks Sam and deals 7 damage
# Sam is down to 7 health
# Sam attacks Paul and deals 19 damage
# Paul is down to -9 health
# Paul has Died and Sam is Victorious
# Game Over

'''
# Try 2, failed
# Warrior & Battle Class

class Warrior:
    def __init__(self, name="", health="", attack="", block=""):
        self.name = name
        self.health = health
        self.attack = attack
        self.block = block

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.isalpha():
            self.__name = value
        else:
            print("Enter a name using English")

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        self.__health = value
    
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self, value):
        if value.isdigit():
            self.__attack = value
        else:
            print("Use digits for the Attack")
    
    @property
    def block(self):
        return self.__block
    
    @block.setter
    def block(self, value):
        if value.isdigit():
            self._block = value
        else:
            print("Use digits for the Attack")

    def Attack(self):
        self.__attack = random() * 10
        return self.__attack
    
    def Block(self):
        self.__block = random() * 10
        return self.__block

class Battle:
    def __init__(self, warrior_offense="", warrior_defense=""):
        self.warrior_offense = warrior_offense
        self.warrior_defense = warrior_defense    

    def conflict(self):
        
    
    def game_over(self):
        if 

# Warriors will have names, health, and attack and block maximums
# They will have the capabitlities to attack and block random amounts

# Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random() as well

# Battle Class capability of keep looping until 1 warrior dies
# Warriors will each get a turn to attack each other

# Function gets 2 warriors
# 1 warrior attacks the other
# Attacks and Blocks be integers
'''


# Pro's method

# Sam attacks Paul and deals 9 damage
# Paul is down to 10 halth
# Paul attacks Sam and deals 7 damage
# Sam is down to 7 health
# Sam attacks Paul and deals 19 damage
# Paul is down to -9 health
# Paul has Died and Sam is Victorious
# Game Over

import random
import math

# Warrior & Battle Class

class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

# this class can loop and can allow battles
class Battle:

    # Utility class
    # capability to loop and warriors fight against each other
    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResults(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
        
            if self.getAttackResults(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    
    # Class Method, doesn't need to use self
    # method if the class, since class doesn't need a self(not tied to an object)
    # capability of the class
    @staticmethod
    def getAttackResults(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                warriorB.name, damage2WarriorB))
        
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorA.name,
                    warriorB.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():

    maximus = Warrior("Maximus", 50, 20, 10)

    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

main()

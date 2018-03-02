attack = {'quick': (lambda: print("Quick Attack")),
        'power': (lambda: print("Power Attack")),
        'miss': (lambda: print("Missed Attack"))}

attack['power']()

import random

list1 = list(attack.keys())
pick1 = random.choice(list1)
attack[pick1]()

# Consolidate code
attack[random.choice(list(attack.keys()))]()

# This looks best
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

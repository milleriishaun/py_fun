# Need to practice this at least 5 times.
# Use this for different applications.

# Real World Threading
# Model a bank account
# Use threads to block out other transactions
# Don't want someone to draw out more $ than is there
# Lock out the other users until the first person is done transacting

import threading
import time
import random

class BankAccount(threading.Thread):

    acctBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawl ${} at {}".format(customer.name,
                                                customer.moneyRequest,
                                                time.strftime("%H:%M:%S", time.gmtime())))
        
        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance: ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in account")
            print("Current balance: ${}".format(BankAccount.acctBalance))
        
        # three seconds
        time.sleep(3)

# allow locking of threads for executing
threadLock = threading.Lock()

# create our customers
doug = BankAccount("Doug: ", 1)
paul = BankAccount("Paul: ", 100)
sally = BankAccount("Sally: ", 50)


doug.start()
paul.start()
sally.start()

# wait for the previous threads to end
doug.join()
paul.join()
sally.join()

print("Execution Ends")



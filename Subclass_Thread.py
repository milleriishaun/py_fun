# Subclass a thread object
# change what it does afterwards by using the 'run' method
import threading
import time
import random

class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    # this method executes upon calling thread object
    def run(self):
        # execute code in an outside function
        getTime(self.name)
    
        print("Thread", self.name, "Execution Ends")


def getTime(name):
    print("Thread {} sleeps at {}".format(name,
                                    time.strftime("%H:%M:%S", time.gmtime())))
    
    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

# Name them 1 and 2
thread1 = CustThread("1")
thread2 = CustThread("2")

# Execute the threads
thread1.start()
thread2.start()

# check that it is alive
print("Thread 1 Alive: ", thread1.is_alive())
print("Thread 2 Alive: ", thread2.is_alive())

# Let's get the thread name
# could also setName() but we'll use getName now
print("Thread 1 Name: ", thread1.getName())
print("Thread 2 Name: ", thread2.getName())

# Use join in order to wait for threads to exit(joins the threads)
thread1.join()
thread2.join()

print("Execution Ends")
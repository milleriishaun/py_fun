# Threading
# Like running multiple programs at once
# Actually only one thread working at a time, and they take turns
# One is executing at one time
# Other one sleeps until it's turn...
# A thread is simply a block of code that executes

import threading
import time
import random

# First thread of Main
def executeThread(i):
    print("Thread {} sleeps at {}".format(i,
                                        time.strftime("%H:%M:%S",
                                        time.gmtime())))

    # looong time in computer world but just seconds
    randSleepTime = random.randint(1, 5)

    # Make a thread(group of code) pause while the others execute
    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at {})".format(i,
                                        time.strftime("%H:%M:%S",
                                        time.gmtime())))

# Second Thread of Main
# Create the thread and run them
for i in range(10):
    # use a comma at the end of args
    # because it expects a sequence to be passed through
    # but instead, we are using only a single argument/thread
    thread = threading.Thread(target=executeThread, args=(i,))

    # start the execution of the thread
    thread.start()

    # print all the active threads that are executing
    print("Active Threads: ", threading.activeCount())

    # return a list of all the active thread objects out there
    print("Thread Objects: ", threading.enumerate())

    # lines up a bunch of threads and execute the same exact code...
    # doesnt have to be the same code
    # But they work until all the codes are executed.

# These are all the time functions that I am aware of

import time
from tkinter import *
from tkinter import ttk

global time1
global timeHour1
global timeMin1
global timeSec1

global time2
global timeHour2
global timeMin2
global timeSec2

#ticking function to show time
def tick():
    time1 = ""
    timeHour1 = ""
    timeMin1 = ""
    timeSec1 = ""

    time2 = ""
    timeHour2 = ""
    timeMin2 = ""
    timeSec2 = ""


    # Current local time
    time2 = time.strftime('%H:%M:%S')
    # timeHour2 = time.strftime('%H')
    # timeMin2 = time.strftime('%M')
    # timeSec2 = time.strftime('%S')
    # update time1 if old
    if time2 != time1:
        time1 = time2
        # timeHour1 = timeHour2
        # timeMin1 = timeMin2
        # timeSec1 = timeSec2
    
        clock_output.config(text=time2)
        # calls self every 200 milliseconds, recursive
        clock_output.after(200, tick)

root = Tk()

root.geometry("200x200+300+300")

# basic time manipulation
# get the current time...which is ticks
ticks = time.time()

# convert the time to readable time Tuple
time2 = time.localtime(ticks)

# set up a clock variable type stringVar
clock = StringVar()
# set the clock
# clock.set("{}:{}:{}".format(time2[3], time2[4], time2[5]))
clock_var = clock.get()

# superfluous print out of the clock just to make sure
print(clock_var)

clock_name = ttk.Label(root, text="Clock")
clock_name.grid(row=0, column=0, padx=5, pady=5)

# Make a text box for the clock time reads
clock_output = ttk.Label(root)
clock_output.grid(row=1, column=0, padx=5, pady=5)


# for the function
tick()

root.mainloop()
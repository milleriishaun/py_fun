# Make this GUI for SOMETHING!
# need GUI for TimeWatch app!

# Make the clock system


# Modules go here
import math
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Functions go here

def tick():
    global time1
    global timeHour1
    global timeMin1
    global timeSec1


    # Current local time
    time2 = time.strftime('%H:%M:%S')
    timeHour2 = time.strftime('%H')
    timeMin2 = time.strftime('%M')
    timeSec2 = time.strftime('%S')
    # update time1 if old
    if time2 != time1:
        time1 = time2
        timeHour1 = timeHour2
        timeMin1 = timeMin2
        timeSec1 = timeSec2
        clock_output.config(text=time2)
    # calls self every 200 milliseconds, recursive
    clock_output.after(200, tick)

def print_start(event=None):
    startBut.bind("<Button-1>")
    startTime['text'] = time1
    startHourInt = int(timeHour1)
    startMinInt = int(timeMin1)
    startSecInt = int(timeSec1)

def print_end(event=None):
    stopBut.bind("<Button-1>")
    stopTime['text'] = time1
    stopHourInt = int(timeHour1)
    stopMinInt = int(timeMin1)
    stopSecInt = int(timeSec1)

def time_diff(event=None):
    if (stopHourInt-startHourInt) < 1:
        startMinInt += 60
        if stopMinInt-startMinInt < 0:
            stopMinInt += 60
    elif (stopMinInt-startMinInt) < 1:
        startSecInt += 60
        if stopSecInt-startSecInt < 0:
            stopSecInt += 60
    else:
        diffHour = stopHourInt - startHourInt
        diffMin = stopMinInt - startMinInt
        diffSec = stopSecInt - startSecInt
        print(diffHour+':'+diffMin+':'+diffSec)
        diffTime['text'] = diffHour


# Create a GUI for button to click to start the time and end the time

# make the root
root = Tk()

time1 = ''

''' # basic time manipulation
# get the current time...which is ticks
ticks = time.time()

# convert the time to readable time Tuple
time2 = time.localtime(ticks)

# set up a clock variable type stringVar
clock = StringVar()
# set the clock
clock.set("{}:{}:{}".format(time2[3], time2[4], time2[5]))

clock_var = clock.get()


# superfluous print out of the clock just to make sure
print(clock_var)
'''



# Title the window
root.wm_title("TimeWatch")

# Set the geometry of the window
root.geometry("400x400+300+300")

# window cannot be resized
root.resizable(width=False, height=False)

# color the window
root.config(bg="orange")

# Create a frame for the clock
frameTop = Frame(root)
frameTop.grid(row=0, column=0, padx=5, pady=5)

# Create a frame for the two buttons
frameBottom = Frame(root)
frameBottom.grid(row=1, column=0, padx=5, pady=5)

# Style up the Buttons to make them look ultracool
style = ttk.Style()
style.configure("TButton",
                bg="white",
                fg="blue",
                font="Mistral 20 bold",
                padding=20)

# Make a label for the top frame
clock_name = Label(frameTop, text="Clock")
clock_name.grid(row=0, column=0, padx=5, pady=5)

# Make a text box for the clock time reads
# Text(frameTop, textvariable="{}:{}:{}".format(time2[3], time2[4], time2[5]))
clock_output = Label(frameTop)
clock_output.grid(row=1, column=0, padx=5, pady=5)

print(time1)

# Make first button
startBut = ttk.Button(frameBottom, text="start timer", command=print_start)
startBut.bind("<Button-1>")
# Position first button, will position better next time
startBut.grid(row=0, column=0, padx=5, pady=5)

# Make start label
startLab = Label(frameBottom, text="start time: ")
startLab.grid(row=0, column=1, padx=5, pady=5)

# Show the new time saved
startTime = Label(frameBottom)
startTime.grid(row=0, column=2, padx=5, pady=5)

# Make second button
stopBut = ttk.Button(frameBottom, text="stop timer", command=print_end)
stopBut.bind("<Button-1>")
# Position first button, will position better next time
stopBut.grid(row=1, column=0, padx=5, pady=5)

# Make stop label
stopLab = Label(frameBottom, text="stop time: ")
stopLab.grid(row=1, column=1, padx=5, pady=5)

# Show the new time saved
stopTime = Label(frameBottom)
stopTime.grid(row=1, column=2, padx=5, pady=5)


# Make third button
diffBut = ttk.Button(frameBottom, text="Calc Difference!", command=print_end)
diffBut.bind("<Button-1>")
# Position first button, will position better next time
diffBut.grid(row=2, column=0, padx=5, pady=5)

# Add new feature of Time difference
diffLab = ttk.Label(frameBottom, text="time difference: ")
diffLab.grid(row=2, column=1, padx=5, pady=5)



time_diff()
# if (startTime['text']) and (stopTime['text']):
#     time_diff()
#     print('works')

diffTime = Label(frameBottom)
diffTime.grid(row=2, column=2, padx=5, pady=5)



tick()

root.mainloop()


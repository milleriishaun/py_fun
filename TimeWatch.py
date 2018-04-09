'''
User Case Description

This is a StopWatch called TimeWatch

I. The current time is displayed on first row.
    N1. Split current time into different variables. (Class Field integers)
II. User clicks a start button and the time is printed to the right. (self, current time)
    N2. Store the start time into a variable.
III. User clicks a stop button and the time is printed to the right. (self, current time)
    N2. Store the stop time into a variable.
IV. User clicks a difference button and the difference is printed to the right. (self, )


Note 1: Need to split the parts of the time into different variables. (Class Field integers)
Note 2: Need to store the value of the current time.

'''

# Modules go here
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

class TimeWatch:

    # Store start time and stop time
    start_abstraction = ""
    stop_abstraction = ""

    # Current Time
    def tick(self):
        time1 = ""
        # Store current local time
        self.time2 = time.strftime('%H:%M:%S')
        
        # update time1 if old
        if self.time2 != time1:
            time1 = self.time2
        
            # calls self every 200 milliseconds, recursive... be careful not to use self.tick()
            self.clock_output.config(text=self.time2)
            self.clock_output.after(200, self.tick)


    def print_start(self, event=None):
        self.startBut.bind("<Button-1>")
        self.start_abstraction = self.time2
        self.startTime['text'] = self.start_abstraction

    def print_end(self, event=None):
        self.stopBut.bind("<Button-1>")
        self.stop_abstraction = self.time2
        self.stopTime['text'] = self.stop_abstraction

    def time_diff(self, event=None):

        self.diffBut.bind("<Button-1>")

        self.startHour = int(self.start_abstraction[0:2])
        self.startMin = int(self.start_abstraction[3:5])
        self.startSec = int(self.start_abstraction[6:8])

        self.stopHour = int(self.stop_abstraction[0:2])
        self.stopMin = int(self.stop_abstraction[3:5])
        self.stopSec = int(self.stop_abstraction[6:8])

        diffHour = self.stopHour - self.startHour
        diffMin = self.stopMin - self.startMin
        diffSec = self.stopSec - self.startSec

        # all cases for negative time differences
        if diffSec < 0:
            if diffMin < 0:
                if diffHour < 0:
                    messagebox.showwarning("Syntax Error", "The difference is negative in hours, minutes, and seconds!")
                    return
                else:
                    messagebox.showwarning("Syntax Error", "The difference is negative in minutes and seconds!")
                    return
            elif diffHour < 0:
                messagebox.showwarning("Syntax Error", "The difference is negative in hours and seconds!")
                return
            else:
                messagebox.showwarning("Syntax Error", "The difference is negative in seconds!")
                return
        elif diffMin < 0:
            messagebox.showwarning("Syntax Error", "The difference is negative in minutes!")
            return
        else:
            if diffMin < 0:
                if diffHour < 0:
                    messagebox.showwarning("Syntax Error", "The difference is negative in hours and minutes!")
                    return
                else:
                    messagebox.showwarning("Syntax Error", "The difference is negative in minutes!")
                    return
            elif diffHour < 0:
                messagebox.showwarning("Syntax Error", "The difference is negative in hours!")
                return
            else:
                # diff_solution = "{%02d}:{%02d}:{%02d}".format(diffHour, diffMin, diffSec)
                diff_solution = str(diffHour).zfill(2) + ':' + str(diffMin).zfill(2) + ':' + str(diffSec).zfill(2)
                self.diffTime['text'] = diff_solution

    def __init__(self, root):

        # Create a GUI for button to click to start the time and end the time
        root.wm_title("TimeWatch")
        root.geometry("560x340+400+200")
        root.resizable(width=False, height=False)
        root.config(background="dark slate gray")

        # Style up the Buttons to make them look ultracool
        style = ttk.Style()
        style.configure("TLabel",
                        background="gold",
                        foreground="midnight blue",
                        font="Mistral 20 bold",
                        padding=5)
        style.configure("TFrame",
                        background="light sky blue",
                        foreground="midnight blue",
                        font="Arial 20 bold",
                        padding=5)
        style.configure("TButton",
                        background="dark slate gray",
                        foreground="midnight blue",
                        font="Arial 20 bold",
                        padding=5)

        # This textvariable will control time
        self.time2 = StringVar()

        # Create a frame for the clock
        self.frameTop = ttk.Frame(root, relief=SUNKEN)
        self.frameTop.grid(row=0, column=0, padx=5, pady=5)

        # Create a frame for the three buttons
        self.frameBottom = ttk.Frame(root, relief=SUNKEN)
        self.frameBottom.grid(row=1, column=0, padx=5, pady=5)

        # root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Make a label for the top frame
        self.clock_name = ttk.Label(self.frameTop, text="Clock")
        self.clock_name.grid(row=0, columnspan=3, padx=5, pady=5)

        # Make a text box for the clock time reads
        self.clock_output = ttk.Label(self.frameTop)
        self.clock_output.grid(row=1, columnspan=3, padx=5, pady=5)

        # Start Button
        self.startBut = ttk.Button(self.frameBottom, text="Start", cursor="hand2", command=lambda: self.print_start())
        self.startBut.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.startLab = ttk.Label(self.frameBottom, text="start time: ")
        self.startLab.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.startTime = ttk.Label(self.frameBottom)
        self.startTime.grid(row=0, column=2, padx=5, pady=5)

        # Stop Button
        self.stopBut = ttk.Button(self.frameBottom, text="Stop", cursor="hand2", command=lambda: self.print_end())
        self.stopBut.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.stopLab = ttk.Label(self.frameBottom, text="stop time: ")
        self.stopLab.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        self.stopTime = ttk.Label(self.frameBottom)
        self.stopTime.grid(row=1, column=2, padx=5, pady=5)

        # Difference Button
        self.diffBut = ttk.Button(self.frameBottom, text="Difference", cursor="coffee_mug", command=lambda: self.time_diff())
        self.diffBut.grid(row=2, column=0, padx=5, pady=5)
        self.diffLab = ttk.Label(self.frameBottom, text="time difference: ")
        self.diffLab.grid(row=2, column=1, padx=5, pady=5)

        # Show the time difference
        self.diffTime = ttk.Label(self.frameBottom)
        self.diffTime.grid(row=2, column=2, padx=5, pady=5)

def main():

    root = Tk()
    stopTimer = TimeWatch(root)
    stopTimer.tick()
    root.mainloop()

main()
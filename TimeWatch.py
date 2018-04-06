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
import math
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
        pass


    def print_start(self, event=None):
        self.startBut.bind("<Button-1>")
        self.start_abstraction = str(self.time1.get())
        self.startTime['text'] = self.start_abstraction

    def print_end(self, event=None):
        self.stopBut.bind("<Button-1>")
        self.stop_abstraction = str(self.time1.get())
        self.stopTime['text'] = self.stop_abstraction

    def time_diff(self, event=None):

        self.diffBut.bind("<Button-1>")

        self.startHour = int(self.start_abstraction[0:2])
        self.startMin = int(self.start_abstraction[3:5])
        self.startSec = int(self.start_abstraction[6:8])

        self.stopHour = int(self.stop_abstraction[0:2])
        self.stopMin = int(self.stop_abstraction[3:5])
        self.stopSec = int(self.stop_abstraction[6:8])

        try:
            if (self.stopHour-self.startHour) < 1:
                self.startMin += 60
                if self.stopMin-self.startMin < 0:
                    self.stopMin += 60
            elif (self.stopMin-self.startMin) < 1:
                self.startSec += 60
                if self.stopSec-self.startSec < 0:
                    self.stopSec += 60
            else:
                diffHour = self.stopHour - self.startHour
                diffMin = self.stopMin - self.startMin
                diffSec = self.stopSec - self.startSec
                diff_solution = str(diffHour) + ':' + str(diffMin) + ':' + str(diffSec)
                print(diff_solution)
                self.diffTime['text'] = diff_solution

        except ValueError:
            print("something wrong in time_diff function")

    def __init__(self, root):

        # Create a GUI for button to click to start the time and end the time
        root.wm_title("TimeWatch")
        root.geometry("500x800+300+100")
        root.resizable(width=False, height=False)
        root.config(background="orange")

        # Style up the Buttons to make them look ultracool
        style = ttk.Style()
        style.configure("TLabel",
                        bg="white",
                        fg="blue",
                        font="Mistral 20 bold",
                        padding=20)
        style.configure("TLabel",
                        bg="white",
                        fg="blue",
                        font="Mistral 20 bold",
                        padding=20)
        style.configure("TButton",
                        bg="white",
                        fg="blue",
                        font="Mistral 20 bold",
                        padding=20)

        # This textvariable will control time
        self.time2 = StringVar()

        # Create a frame for the clock
        self.frameTop = ttk.Frame(root)
        self.frameTop.grid(row=0, column=0, padx=5, pady=5)

        # Create a frame for the two buttons
        self.frameBottom = ttk.Frame(root)
        self.frameBottom.grid(row=1, column=0, padx=5, pady=5)

        # Make a label for the top frame
        self.clock_name = ttk.Label(self.frameTop, text="Clock")
        self.clock_name.grid(row=0, column=0, padx=5, pady=5)

        # Make a text box for the clock time reads
        self.clock_output = ttk.Label(self.frameTop)
        self.clock_output.grid(row=1, column=0, padx=5, pady=5)

        # Start Button
        self.startBut = ttk.Button(self.frameBottom, text="start timer", command=lambda: self.print_start())
        self.startBut.grid(row=0, column=0, padx=5, pady=5)
        self.startLab = ttk.Label(self.frameBottom, text="start time: ")
        self.startLab.grid(row=0, column=1, padx=5, pady=5)
        self.startTime = ttk.Label(self.frameBottom)
        self.startTime.grid(row=0, column=2, padx=5, pady=5)

        # Stop Button
        self.stopBut = ttk.Button(self.frameBottom, text="stop timer", command=lambda: self.print_end())
        self.stopBut.grid(row=1, column=0, padx=5, pady=5)
        self.stopLab = ttk.Label(self.frameBottom, text="stop time: ")
        self.stopLab.grid(row=1, column=1, padx=5, pady=5)
        self.stopTime = ttk.Label(self.frameBottom)
        self.stopTime.grid(row=1, column=2, padx=5, pady=5)

        # Difference Button
        self.diffBut = ttk.Button(self.frameBottom, text="Calc Difference!", command=lambda: self.time_diff())
        self.diffBut.grid(row=2, column=0, padx=5, pady=5)
        self.diffLab = ttk.Label(self.frameBottom, text="time difference: ")
        self.diffLab.grid(row=2, column=1, padx=5, pady=5)

        # Show the time difference
        self.diffTime = ttk.Label(self.frameBottom)
        self.diffTime.grid(row=2, column=2, padx=5, pady=5)



    def __iter__(self):
        return self

    def __next__(self):
        time1 = ""
        # Store current local time
        self.time2 = time.strftime('%H:%M:%S')
        print(self.time2)
        
        # update time1 if old
        if self.time2 != time1:
            time1 = self.time2
        
            self.clock_output.config(text=self.time2)
            # calls self every 200 milliseconds, recursive
            self.clock_output.after(200)
            return 
        else:
            raise StopIteration

def main():

    root = Tk()
    stopTimer = TimeWatch(root)
    root.mainloop()

main()
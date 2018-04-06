
import time
from tkinter import *
from tkinter import ttk

'''
#ticking function to show time
def tick():
    time1 = ""
    time2 = time.strftime('%H:%M:%S')

    if time2 != time1:
        time1 = time2
        clock_output.config(text=time2)
        # calls self every 200 milliseconds, recursive
        clock_output.after(200, tick)

root = Tk()
root.geometry("200x200+300+300")

clock_name = ttk.Label(root, text="Clock")
clock_name.grid(row=0, column=0, padx=5, pady=5)

# Make a text box for the clock time reads
clock_output = ttk.Label(root)
clock_output.grid(row=1, column=0, padx=5, pady=5)

# for the function
tick()

root.mainloop()
'''

def tick():
    x=0
    y=1
    if x != y:
        print(x)
        print(y)
        clock_output.config(text=str(y))
        clock_output.after(200, tick())

# reminder, just took out main()
root = Tk()

clock_name = ttk.Label(root, text="Clock")
clock_name.grid(row=0, column=0, padx=5, pady=5)

clock_output = ttk.Label(root)
clock_output.grid(row=1, column=0, padx=5, pady=5)

tick()
root.mainloop()

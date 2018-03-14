# How to make GUI in Python
# This is for things like Buttons and Interfaces
# Using TKInter in Python
# Everything is WORKING!
# import tkinter
# tkinter._test()
'''
from tkinter import *
from tkinter import ttk

root = Tk()

root.title("First GUI")

# # Can do a bunch of things with components
# ttk.Button(root, text="Hello TKInter").grid()

# These are some of the components:
# Some of the different Widgets: Button, Label, Canvas, Menu, Text, Scale,
# OptionMenu, Frame, CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar, Bitmap, SpinBox, Image

frame = Frame(root)

labelText = StringVar()

# We'll be changing labelText later
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

# now changing the labelText
labelText.set("I am a label")

# This is a geometry manager
label.pack()
button.pack()
frame.pack()

root.mainloop()
'''



'''
# PAC is a very simplistic Geometry Manager
# defines the layout of the components
# PAC positions by location: Top Right Left Bottom
# X and Y direction

from tkinter import *
from tkinter import ttk
root = Tk()
frame = Frame(root)
Label(frame, text="A Bunch of Buttons").pack()
Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()

'''




'''
# grid geometry manager is more commonly used
# rows and columns in table structure
from tkinter import *
from tkinter import ttk
root = Tk()

# Each cell holds one individual widget for this example
# otherwise, it can be multiple widgets per cell actaually
# Define where boxes go
# sticky means where it will stretch... N, NE, W, NW, etc.
# padx = padding is 4 pixels
Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)

root.mainloop()
'''




'''
# Now let's try a more compicated design
# A label
# An entry on the right side, 50px width
# Button on right side
# Underneath, a label followed by radio buttons
# Underneath, label with checkbox buttons on right of it.

from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)

# value tells which button is being clicked on
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

# Now make another label
Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)

root.mainloop()
'''



'''
# How do events work with tkinter!?
# Function called whenever a button is clicked on
from tkinter import *
from tkinter import ttk

# change what is entered by defining the function
def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2

    sumEntry.delete(0, "end")

    sumEntry.insert(0, sum)

# create the Tk() object
root = Tk()

# to get access to the values/cells/positions, can't use grid
# just use the PAC functions
# we have to put the entry positions in later
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

# Put a label inside, position it on the left
Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

# Equals button
equalButton = Button(root, text="=")
# Leftmost mouse button
# the binding here makes the event matter
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
'''



'''
# Good try, but now do it on your own!
# Now is my attempt at a bunch of things that I don't really understand
from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum1 = num1 + num2
    # Delete the answer so can reuse
    sumEntry.delete(0, "end")
    sumEntry.insert(0, sum1)

# This creates the instance
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
# Position it after all the calcs are done
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)


root.mainloop()
'''




'''
# Self Try, great!
from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum1 = num1 + num2
    sumEntry.delete(0, "end")
    sumEntry.insert(0, sum1)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalSign = Button(root, text="=")
equalSign.bind("<Button-1>", get_sum)
equalSign.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
'''




'''
# START of TKinter Tutorial
# Menubars, Tk Variables, Message Boxes, Styling Widgets, etc.
from tkinter import *
from tkinter import messagebox

# Default of None isn't always needed, but why not have it there
def get_data(event=None):
    print("StringVar: ", strVar.get())
    print("IntVar: ", intVar.get())
    print("Double: ", dblVar.get())
    print("BooleanVar: ", boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

# Tk inter variables can be set and have options
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String:")
intVar.set("Enter Integer:")
dblVar.set("Enter Double:")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intVar = Entry(root, textvariable=intVar)
intVar.pack(side=LEFT)

dblVar = Entry(root, textvariable=dblVar)
dblVar.pack(side=LEFT)

theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
# set to left mouse button, which is button 1
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)


root.mainloop()
'''





'''
# Try 1, worked after discovered some issues. Needs practice.
from tkinter import *
from tkinter import messagebox

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)



def binderFunct(event=None):
    if boolVar.get():
        checkBox.unbind("<Button-1>")
    else:
        checkBox.bind("<Button-1>", getData)



def get_data(event=None):
    print("String: ", strVar.get())
    print("Integer: ", intVar.get())
    print("Double: ", dblVar.get())
    print("Boolean: ", boolVar.get())

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String: ")
intVar.set("Enter Integer: ")
dblVar.set("Enter Double: ")
boolVar.set(True)

strVar = Entry(root, textvariable=strVar)
strVar.pack(side=LEFT)

intVar = Entry(root, textvariable=intVar)
intVar.pack(side=LEFT)

dblVar = Entry(root, textvariable=dblVar)
dblVar.pack(side=LEFT)

theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data!")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)



root.mainloop()
'''





'''
# Try 2, next day, this one I had fun with even though I need a lot of review.
# The modules are not sticking well because there is so much information
# But if I make something that is actualy usful to me, I think i will increase in skill

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# made the mistake of binding and unbinding the checkmark button
# rather than the getData button, and that is why there was no progress.
# Never get into the probelm of that again. So then I must not understand
# what it means to bind and unbind just yet.
def binderFunct(event=None):
    if boolVar.get():
        dataBut.unbind("<Button-1>")
    else:
        dataBut.bind("<Button-1>", getData)



def getData(event=None):
    print("String: ", strVar.get())
    print("Integer: ", intVar.get())
    print("Float: ", dblVar.get())
    print("Boolean: ", boolVar.get())

def openMsg():
    messagebox.askquestion("Do you want to know what the Matrix really is?", "Red pill or the blue pill?")


# don't forget to get the root
root = Tk()

frame = Frame(root)

# Use variables to store the data types
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# set the variables with text
strVar.set("Enter String: ")
intVar.set("Enter Integer: ")
dblVar.set("Enter Float: ")
boolVar.set(True)

# make the entry space
strVar = Entry(root, textvariable=strVar)
strVar.pack(side=LEFT)

# make the entry space
intVar = Entry(root, textvariable=intVar)
intVar.pack(side=LEFT)

# make the entry space
dblVar = Entry(root, textvariable=dblVar)
dblVar.pack(side=LEFT)

# make the checkmark button
checkBox = Checkbutton(root, text="Switch", variable=boolVar)
checkBox.bind("<Button-1>", binderFunct)
checkBox.pack(side=LEFT)

# make the get data button
dataBut = Button(root, text="Get Data!")
dataBut.bind("<Button-1>", getData)
dataBut.pack(side=LEFT)

style = ttk.Style()
style.configure("TButton",
                bg="midnight blue",
                fg="green",
                padding=20,
                font="Arial 40 bold")

theButton = Button(frame, text="Yo yo yo", command=openMsg)
theButton.pack()

frame.pack()
root.mainloop()
'''










'''
# Some kind of useful functioning
# How about a questioning app. I should look online for more tutorials.
# Just make something you like? The problem is that I don't know how stuff works together.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
'''



'''
# One responsive thing from this program which is interesting is the colorLog.insert(0.0, "Red\n")
# every time the function is called. And you have to make sure to use 'takefocus'

from tkinter import *

root = Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(bg="dark slate blue")
root.geometry("600x600+300+300")

def redCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
    colorLog.insert(0.0, "Red\n")

def yelCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='yellow')
    colorLog.insert(0.0, "Yellow\n")

def grnCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green')
    colorLog.insert(0.0, "Green\n")

# listbox = Listbox(root)
# listbox.pack(fill=BOTH, expand=1)

# for i in range(20):
#     listbox.insert(END, str(i))

#Left Frame and its contents
leftFrame = Frame(root)
leftFrame.grid(row=0, column=0, padx=5, pady=2)

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)

Instruct = Label(leftFrame, text="1\n2\n3\n4\n5\n6\n7\n8\n9\n", font="Mistral 22 bold")
Instruct.grid(row=1, column=0, padx=10, pady=2)


# Great way to see all the key/value pairs involved
print(Instruct.keys())
for items in Instruct.keys():
    print(items, ': ', Instruct[items])


try:
    imageEx = PhotoImage(file = 'image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2)

redBtn = Button(btnFrame, text="Red", command=redCircle)
redBtn.grid(row=0, column=0, padx=10, pady=2)

yellowBtn = Button(btnFrame, text="Yellow", command=yelCircle)
yellowBtn.grid(row=0, column=1, padx=10, pady=2)

greenBtn = Button(btnFrame, text="Green", command=grnCircle)
greenBtn.grid(row=0, column=2, padx=10, pady=2)


root.mainloop() #start monitoring and updating the GUI
'''




# Make this GUI for SOMETHING!






'''
# Different ways to style the widgets
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# 'command' takes in a function
def open_msg_box():
    messagebox.showwarning(
        "Event Triggered",
        "Button Clicked"
    )

root = Tk()

# define the widget...define size on window
# widthxheight+xoffset+yoffset
root.geometry("400x400+300+300")

# cannot resize
root.resizable(width=False, height=False)

# Create a simple frame to house all the widgets
frame = Frame(root)

# when using ttk.Style you have to import ttk
style = ttk.Style()

# now that we imported the module, style it
# target button to change the styling, want midnight blue
# foreground is like the color of the words
style.configure("TButton",
                foreground="dark slate gray",
                font="Times 20 bold italic",
                padding=20)

# website for foregrounds: http://wiki.tcl.tk/37701
# ttk widget names which can be styled: TButton, TCheckbutton, TCombobox,
# TEntry, TFrame, TLabel, TLabelframe, TMenubutton,
# TNotebook, TProgressbar, TRadiobutton, Tscale,
# TScrollbar, TSpinbox, Treeview


# You can also change your THEME STYLE of your widget
print(ttk.Style().theme_names())

# different OS's have different style settings...use lookup.
# change the style for all the buttons
print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

# show the themes of buttons
# these are built-in themes

# ttk.Style().theme_use('vista')

# let's create the buttons
# note: tied to the frame instead of the root
theButton = ttk.Button(frame,
                        text="Important Button",
                        command=open_msg_box)

# disable and enable the button
# reference state to fix this
theButton['state'] = 'disabled'
theButton['state'] = 'normal'

# this shows us the results
theButton.pack()

# this shows us the results
frame.pack()

root.mainloop()
'''





'''
# Try 1, used a lot of help
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open_msg_box():
    messagebox.showwarning("Event Triggered", "Button Clicked")

root = Tk()

root.geometry("400x400+300+300")

root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                    foreground="midnight blue",
                    background="tomato",
                    font= "Times 20 bold italic",
                    padding=20)

someButton = ttk.Button(frame,
                        text="SuperButton",
                        command=open_msg_box)

someButton.pack()
frame.pack()
root.mainloop()
'''



'''
# Try 2, Next day, needed a lot of help
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open_msg_box():
    messagebox.showwarning("This alert!1", "This alert 2!")

root = Tk()

root.geometry("1000x700+300+300")

root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                text="This is craycray!",
                fg="orange",
                bg="midnight blue",
                font="Times 20 bold",
                padding=20)

thisButton = ttk.Button(frame, text="Do it!", command=open_msg_box)

thisButton.pack()

frame.pack()

root.mainloop()
'''







'''
# Try 3, need to get used to using these commands actually down. I got better with them. But I forgot the past tutorials.open
# I shoudl try to make a real project using what I know.
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open_msg_box():
    messagebox.showwarning("black?", "Panther!")

root = Tk()

root.geometry("500x500+200+200")

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                bg="midnight blue",
                fg="pink",
                padding=20,
                font="Times 40 bold")

theButton = ttk.Button(frame, text="This button", command=open_msg_box)

theButton.pack()
frame.pack()
root.mainloop()
'''







# Next Example, using Tkinter








# Better layout usage for the desktop app.


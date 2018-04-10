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






'''
# Misc Youtuber Example, using Tkinter
# This is a great example setup for Tkinter GUI projects
from tkinter import *

global count
count =0
class App():
    
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')
        
    def start(self):
        global count
        count=0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
        
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(930,self.start_timer)
            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.geometry("600x500")
        self.root.resizable(False,False)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Courier 12 bold"))
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Courier 12 bold"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=130,y=100)
        self.bt2.place(x=255,y=100)
        self.bt3.place(x=370,y=100)
        self.root.mainloop()
    


a = App()
'''








'''

# This tutorial from someone else
# http://www.tkdocs.com/tutorial/onepage.html
from tkinter import *
from tkinter import ttk

# This is a calculate function with as many arguments as desired
# it is within a try/except model
# It marks the variable feet as a float, and gets the value from the main program
# meters.set bu tthen we have to put in all the decimals to make it all float
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

# I suppose people use mainframe to designate the Frame
# They also use the more advanced ttk.Frame reference
mainframe = ttk.Frame(root, padding="3 3 12 12")
# The sticky is all around so that it can be stretched
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# This makes it so that upon extra info, there is a resize of the window
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Designate the type of the variable
feet = StringVar()
meters = StringVar()

# Make the entry box
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Add the label for the meters, using meters variable
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Add the button for the calculation
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# add extra labels to get info.
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# This is a loop using the child variable as storage
# This checks the mainframe.winfo_children() iterable.
# I don't really get why a iterable is returned but it is probably
# a list
# Either way, for each part of the list, the child needs to be configured with padding
# all of the widgets that are children of our content frame get padding; shortcut
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# This gets the pointer to get into the box when it pops up
feet_entry.focus()
# This makes it so that if I press enter, it automatically calculates
# It is interesting though because I can also click on the button for result
root.bind('<Return>', calculate)

# DOn't forget the main loop
root.mainloop()

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

# ^review this stuff using TimeWatch app







'''
# Another Tutorial, by sentdex:
# https://www.youtube.com/watch?v=Ccct5D2AyNM
from tkinter import *
from PIL import Image, ImageTk

# It gets a Widget term passed through it within tkinter
# there is a Frame class in tkinter which will be passed through
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        # this going to be the master widget
        self.master = master

        #this is not built into tkinter
        self.init_window()

    def init_window(self):

        # title of window
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0, y=0)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the file button
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # Create the dit button
        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImage)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def showImage(self):
        load = Image.open('pillow.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text='z..zz..zzz')
        text.pack()


# this is aroot window
root = Tk()
root.geometry("400x300")

# Window called of root
app = Window(root)

root.mainloop()
'''






'''
# Better layout usage for the desktop app.
# Edit this so it is rather for TimeWatch app
from tkinter import *

global count
count =0
class App():
    
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')
        
    def start(self):
        global count
        count=0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
        
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(930,self.start_timer)
            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.geometry("600x500")
        self.root.resizable(False,False)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Courier 12 bold"))
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Courier 12 bold"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=130,y=100)
        self.bt2.place(x=255,y=100)
        self.bt3.place(x=370,y=100)
        self.root.mainloop()
    


a = App()
'''



'''
# review of Tkinter(Derek Banas) Part 1
from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2

    sumEntry.delete(0, "end")

    sumEntry.insert(0, sum)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
'''

# review of Tkinter(Derek Banas) Part 2.1
# Menubars, Tk Variabes, Message Boxes, Styling Widgets


'''
from tkinter import *
from tkinter import messagebox

def get_data(event=None):
    print("String: ", strVar.get())
    print("Integer: ", intVar.get())
    print("Double: ", dblVar.get())
    print("Boolean: ", boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
'''

# review of Tkinter(Derek Banas) Part 2.2
# working on styling
'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open_msg_box():
    messagebox.showwarning(
        "Event Triggered",
        "Button Clicked"
    )

root = Tk()

root.geometry("400x400+300+300")

root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                fg="midnight blue",
                font="Times 20 bold italic",
                padding=20)

print(ttk.Style().theme_names())

print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "fg"))
print(style.lookup("TButton", "padding"))

ttk.Style().theme_use('clam')


theButton = ttk.Button(frame,
                        text="Important Button",
                        command=open_msg_box)


theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()

frame.pack()

root.mainloop()
'''


# review of Tkinter(Derek Banas) Part 2.3
# working on menubars
'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
                            "About",
                            "This awesome program was made in 2018"
    )


root = Tk()

the_menu = Menu(root)

# ------ File Menu -----
file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")

file_menu.add_command(label="Save")

file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)

# ------ Font Menu -----
text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font Picked: ", text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                        variable=text_font,
                        command=change_font)

font_menu.add_radiobutton(label="Courier",
                        variable=text_font,
                        command=change_font)

font_menu.add_radiobutton(label="Ariel",
                        variable=text_font,
                        command=change_font)

# ------ View Menu -----

view_menu = Menu(the_menu, tearoff=0)

# store this in a TK variable(show or not show line numbers)
line_numbers = IntVar()
# set by default to "checked"... er true = 1
line_numbers.set(1)

view_menu.add_checkbutton(label="Line Numbers",
                        variable=line_numbers)

# tie this to the font_menu... but need to make it first
view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(label="View", menu=view_menu)

# ------ Help Menu -----

help_menu = Menu(the_menu, tearoff=0)

help_menu.add_command(label="About",
                    accelerator="ctrl-A", # little notification of shortcut
                    command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

root.bind("<Control-A>", show_about)
root.bind("<Control-a>", show_about)

root.config(menu=the_menu) # this is to show the menu updates

root.mainloop()
'''

'''
# Calculator App in Python using TkInter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Number Key Functions
def sevenIn(event=None):
    greenScreen.insert("end", 7)

def eightIn(event=None):
    greenScreen.insert("end", 8)

def nineIn(event=None):
    greenScreen.insert("end", 9)

def fourIn(event=None):
    greenScreen.insert("end", 4)

def fiveIn(event=None):
    greenScreen.insert("end", 5)

def sixIn(event=None):
    greenScreen.insert("end", 6)

def oneIn(event=None):
    greenScreen.insert("end", 1)

def twoIn(event=None):
    greenScreen.insert("end", 2)

def threeIn(event=None):
    greenScreen.insert("end", 3)

def zeroIn(event=None):
    greenScreen.insert("end", 0)

# Operation Key Functions
def get_division(event=None):
    firstVal.set(int(greenScreen.get()))
    print('first: ', val1.get())
    store.set(int(val1.get()))
    print('val1storage: ', val1storage.get())
    print('screen: ', greenScreen.get())
    greenScreen.delete(0, "end")
    print('screen: ', greenScreen.get())
    op1.delete(0, "end")
    print('/: ', op1.get())
    op1.insert(0, 1)
    print('/: ', op1.get())
    print()

def get_multiplication(event=None):
    firstVal.set(int(greenScreen.get()))
    print('first: ', val1.get())
    store.set(int(val1.get()))
    print('val1storage: ', val1storage.get())
    print('screen: ', greenScreen.get())
    greenScreen.delete(0, "end")
    print('screen: ', greenScreen.get())
    op1.delete(0, "end")
    print('*: ', op1.get())
    op1.insert(0, 2)
    print('*: ', op1.get())
    print()

def get_addition(event=None):
    firstVal.set(int(greenScreen.get()))
    print('first: ', val1.get())
    store.set(int(val1.get()))
    print('val1storage: ', val1storage.get())
    print('screen: ', greenScreen.get())
    greenScreen.delete(0, "end")
    print('screen: ', greenScreen.get())
    op1.delete(0, "end")
    print('+: ', op1.get())
    op1.insert(0, 3)
    print('+: ', op1.get())
    print()

def get_subtraction(event=None):
    firstVal.set(int(greenScreen.get()))
    print('first: ', val1.get())
    store.set(int(val1.get()))
    print('val1storage: ', val1storage.get())
    print('screen: ', greenScreen.get())
    greenScreen.delete(0, "end")
    print('screen: ', greenScreen.get())
    op1.delete(0, "end")
    print('-: ', op1.get())
    op1.insert(0, 4)
    print('-: ', op1.get())
    print()

# Equivalence Button
def get_equivalence(event=None):
    if (greenScreen.get()).isdigit():
        num1 = int(val1.get())
        print('first: ', val1.get())
        oper1 = int(op1.get())
        print('+: ', op1.get())
        num2 = int(greenScreen.get())
        print('screen: ', greenScreen.get())
        print()

        if oper1 == 1:
            result = num1 / num2
            greenScreen.delete(0, "end")
            greenScreen.insert("end", result)
        elif oper1 == 2:
            result = num1 * num2
            greenScreen.delete(0, "end")
            greenScreen.insert("end", result)
        elif oper1 == 3:
            result = num1 + num2
            print("oper1: {}".format(result))
            greenScreen.delete(0, "end")           
            greenScreen.insert("end", result)
        elif oper1 == 4:
            result = num1 - num2
            greenScreen.delete(0, "end")
            greenScreen.insert("end", result)
        else:
            messagebox.showwarning("Syntax Error", "Choose operation first")
    else:
        messagebox.showwarning("Syntax Error", "Please enter value")

def get_ac(event=None):
    store.set(0)
    greenScreen.delete(0, "end")

root = Tk()
root.geometry("300x256+400+400")
root.wm_title("Calculator Desktop App")
root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                foreground="midnight blue",
                background="goldenrod3",
                font= "Arial 20 bold")

style.configure("TFrame",
                foreground="midnight blue",
                background="goldenrod1",
                font= "Arial 20 bold")

# this is responsive because I tested padding but otherwise doesn't work
# may be that the Entry box is not linked to the style somehow
style.configure("TEntry",
                foreground="black",
                background="orange",
                font= "Arial 20 bold")

# tkinter variables
firstVal = IntVar()
store = IntVar() # this might be an extra variable unless I can get the storage function to work
operator1 = IntVar()

# value on greenScreen
val1 = ttk.Entry(frame, textvariable=firstVal)
# storage variable which can be used to get and set, if I can get it to work
val1storage = ttk.Entry(frame, textvariable=store)

# value upon operation key
op1 = ttk.Entry(frame, textvariable=operator1)

# Green Screen
greenScreen = ttk.Entry(frame, width=28, justify=RIGHT)
greenScreen.grid(row=0, column=0, columnspan=4, padx=3, pady=4, ipadx=41, ipady=12)

# Number Keys
sevenB = ttk.Button(frame, text="7", width=3, command=sevenIn)
sevenB.grid(row=1, column=0, padx=3, pady=2, ipadx=0, ipady=0)
eightB = ttk.Button(frame, text="8", width=3, command=eightIn)
eightB.grid(row=1, column=1, padx=3, pady=2, ipadx=0, ipady=0)
nineB = ttk.Button(frame, text="9", width=3, command=nineIn)
nineB.grid(row=1, column=2, padx=3, pady=2, ipadx=0, ipady=0)

fourB = ttk.Button(frame, text="4", width=3, command=fourIn)
fourB.grid(row=2, column=0, padx=3, pady=2, ipadx=0, ipady=0)
fiveB = ttk.Button(frame, text="5", width=3, command=fiveIn)
fiveB.grid(row=2, column=1, padx=3, pady=2, ipadx=0, ipady=0)
sixB = ttk.Button(frame, text="6", width=3, command=sixIn)
sixB.grid(row=2, column=2, padx=3, pady=2, ipadx=0, ipady=0)

oneB = ttk.Button(frame, text="1", width=3, command=oneIn)
oneB.grid(row=3, column=0, padx=3, pady=2, ipadx=0, ipady=0)
twoB = ttk.Button(frame, text="2", width=3, command=twoIn)
twoB.grid(row=3, column=1, padx=3, pady=2, ipadx=0, ipady=0)
threeB = ttk.Button(frame, text="3", width=3, command=threeIn)
threeB.grid(row=3, column=2, padx=3, pady=2, ipadx=0, ipady=0)

zeroB = ttk.Button(frame, text="0", width=3, command=zeroIn)
zeroB.grid(row=4, column=1, padx=3, pady=2, ipadx=0, ipady=0)

# Operations Keys
divisionB = ttk.Button(frame, text="/", width=3, command=get_division)
divisionB.grid(row=1, column=3, padx=3, pady=2, ipadx=0, ipady=0)

multiplicationB = ttk.Button(frame, text="*", width=3, command=get_multiplication)
multiplicationB.grid(row=2, column=3, padx=3, pady=2, ipadx=0, ipady=0)

additionB = ttk.Button(frame, text="+", width=3)
additionB.bind("<Button-1>", get_addition)
additionB.grid(row=3, column=3, padx=3, pady=2, ipadx=0, ipady=0)

subtractionB = ttk.Button(frame, text="-", width=3, command=get_subtraction)
subtractionB.grid(row=4, column=3, padx=3, pady=2, ipadx=0, ipady=0)

# Equivalence Key
equivalenceB = ttk.Button(frame, text="=", width=3)
equivalenceB.bind("<Button-1>", get_equivalence)
equivalenceB.grid(row=4, column=2, padx=3, pady=2, ipadx=0, ipady=0)

# All Clear Key
allClearB = ttk.Button(frame, text="AC", width=3, command=get_ac)
allClearB.grid(row=4, column=0, padx=3, pady=2, ipadx=0, ipady=0)



frame.pack()

root.mainloop()
'''

'''
# review of Tkinter(Derek Banas) Part 1
from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2

    sumEntry.delete(0, "end")

    sumEntry.insert(0, sum)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
'''


'''
from tkinter import *
from tkinter import messagebox

def get_data(event=None):
    print("String: ", strVar.get())
    print("Integer: ", intVar.get())
    print("Double: ", dblVar.get())
    print("Boolean: ", boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
'''

'''
from tkinter import *
import tkinter.filedialog

class TextEditor:

    @staticmethod
    def quit_app(event=None):
        root.quit()
    
    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                    initialdir='C:/Users/Shaun/Anaconda3/envs/pyfun/pyfun')
    
        if txt_file:

            self.text_area.delete(1.0, END)

            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())

                # update the text widget
                root.update_idletasks()
    
    def save_file(self, even=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')

        if file != None:
            data = self.text_area.get('1.0', END + '-1c')

            file.write(data)
            file.close()
        
    def __init__(self, root):
        self.text_to_write = ""

        root.title("Text Editor")

        root.geometry("600x550")

        frame = Frame(root, width=600, height=550)

        scrollbar = Scrollbar(frame)

        self.text_area = Text(frame, width=600, height=550,
                            yscrollcommand=scrollbar.set,
                            padx=10, pady=10)
        
        scrollbar.config(command=self.text_area.yview)

        scrollbar.pack(side="right", fill="y")

        self.text_area.pack(side="left", fill="both", expand=True)

        frame.pack()

        the_menu = Menu(root)

        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        file_menu.add_separator()

        file_menu.add_command(label="Quit", command=self.quit_app)

        the_menu.add_cascade(label="File", menu=file_menu)

        root.config(menu=the_menu)


root = Tk()

text_editor = TextEditor(root)

root.mainloop()
'''

'''
from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def on_fav_food_select(self, event=None):
        lb_widget = event.widget # get widget that triggered event
        # set up everything with indexes
        index = int(lb_widget.curselection()[0]) # index of listbox

        lb_value = lb_widget.get(index)

        # just change the label depending on what the user selects
        self.fav_food_label['text'] = "I'll get you " + lb_value

    def __init__(self, root):
        root.title("Toolbar Example")
        menubar = Menu(root)

        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)

        # Create the toolbar
        toolbar = Frame(root, borderwidth=1, relief=RAISED)

        open_img = Image.open("open.png").resize((50, 50))
        save_img = Image.open("save.png").resize((50, 50))
        exit_img = Image.open("exit.png").resize((50, 50))

        # create the tkinter image for the buttons
        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        # create teh buttons for the toolbar
        open_button = Button(toolbar, image=open_icon)
        save_button = Button(toolbar, image=save_icon)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        # add the image onto the button, in the image position
        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        # show all this stuff
        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        # create toolbar
        toolbar.pack(side=TOP, fill=X)
        # connect menubar
        root.config(menu=menubar)

        # make a label frame
        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)

        self.fav_food_label = Label(lb_frame, text="What is your favorite food?")

        self.fav_food_label.pack()

        list_box = Listbox(lb_frame)

        # insert the listbox options
        list_box.insert(1, "Spaghetti")
        list_box.insert(2, "Pizza")
        list_box.insert(3, "Burgers")
        list_box.insert(4, "Hot Dogs")

        # tie an event to the function
        # this connects clicked selection to function call
        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)

        list_box.pack()

        lb_frame.pack()


        # create the spinbox frame
        sb_frame = Frame(root)

        quantity_label = Label(sb_frame, text="How may do you want?")
        quantity_label.pack()

        spin_box = Spinbox(sb_frame, from_=1, to=5)
        spin_box.pack()

        extras_label = Label(sb_frame, text="Add on Item")
        extras_label.pack()

        extras_spin_box = Spinbox(sb_frame, 
                                values=('French Fries',
                                'Onion Rings',
                                'Tater Tots'))
        extras_spin_box.pack()

        sb_frame.pack()

    
root = Tk()
root.geometry("600x550")
app = TkInterEx(root)
root.mainloop()
'''

'''
from tkinter import *
import tkinter.font

# -------- Define my class -------

class PaintApp:

# -------- Define class variables -------

    drawing_tool = "text"

    left_but = "up"

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

# -------- Catch Mouse Down -------

    def left_but_down(self, event=None):
        self.left_but = "down"

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

# -------- Catch Mouse Up -------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # reset the x and y positon because they are in the "up" now
        self.x_pos = None
        self.y_pos = None

        # track when button is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)


# -------- Catch Mouse Move -------

    # we care about mouse movement when drawing with pencil
    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)



# -------- Draw Pencil -------

    def pencil_draw(self, event=None):
        if self.left_but == "down":
            # have an x and y position... then draw
            if self.x_pos is not None and self.y_pos is not None:
                # we want a smooth line
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)

            # want to store the current x and y...
            # allows dragging x and y... to amke a smoothe line
            # function will be updating over and over as you drag
            self.x_pos = event.x
            self.y_pos = event.y

# -------- Draw Line -------

    # draw regular straight lines too
    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")

# -------- Draw Arc -------

    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=ARC)

# -------- Draw Oval -------

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill="midnight blue", outline="yellow", width=2)

# -------- Draw Rectangle -------

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill="red", outline="orange", width=2)


# -------- Draw Text -------

    def text_draw(self, event):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            text_font = tkinter.font.Font(family='Helvetica', size=20, weight='bold', slant='italic')
            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill="green", font=text_font, text="Wow")


# -------- Initialize -------

    def __init__(self, root):
        root.title("PaintApp")
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
print(tkinter.font.families())
paint_app = PaintApp(root)
root.mainloop()

'''



'''
from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:
    # Class fields
    db_conn = 0
    theCursor = 0
    curr_student = 0


    def setup_db(self):
        # create DB
        self.db_conn = sqlite3.connect('student.db')

        # create cursor so you can traverse recrds of DB
        self.theCursor = self.db_conn.cursor()

        # create the table to store info if it doesn't exist
        # this might cause an error so let's use a try blockk
        try:
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL);")
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Error: Table not created")

        print("Setup DB")

    def stud_submit(self):
        # insert the student into the DB
        self.db_conn.execute("INSERT INTO Students(FName, LName) " + "VALUES ('" + self.fn_entry_value.get() + "', '" + self.ln_entry_value.get() + "')")

        # whenever student is entered, clear the entry boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # update list box
        self.update_listbox()
        print("Submit Stud")

    def update_listbox(self):
        # delete the items that are already in the listbox
        self.list_box.delete(0, "end")

        # get the students from the DB
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students")
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]
                
                # Put students in the LB
                self.list_box.insert(stud_id, stud_fname + " " + stud_lname)
        
        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
        except:
            print("1: Couldn't retrieve data from the DB")

        print("Update LB")

    def load_student(self, event=None): # need event b/c get index from event
        # get index selected which is the sudent id
        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1) # lb is 0 indexed, while Student DB starts at index 1

        # store the current student index
        self.curr_student = index

        # retreive student list from DB
        # use try when accessing the DB
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID=" + index)
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                # set the names in the entries
                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
        except:
            print("2: Couldn't retrieve data from the DB")


        print("Load Stud")
    
    def update_student(self):
        # Update based on current student
        try:
            self.db_conn.execute("UPDATE Students SET FName='" + self.fn_entry_value.get() + "', LName='" + self.ln_entry_value.get() + "' WHERE ID=" + self.curr_student)
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Database couldn't be updated")

        # Clear entries
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # Update list box with the new student list
        self.update_listbox()
        print("Update Stud")
    
    def __init__(self, root):
        root.title("Student Database")
        root.geometry("300x350")

        # ------ 1st row ------
        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root, textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # ------ 2nd row ------
        ln_label = Label(root, text="Last Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root, textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # ------ 3rd row ------
        self.submit_button = ttk.Button(root, text="Submit", command=lambda: self.stud_submit())
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.update_button = ttk.Button(root, text="Update", command=lambda: self.update_student())
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # ------ 4th row ------
        scrollbar = Scrollbar(root)

        self.list_box = Listbox(root)

        self.list_box.bind('<<ListboxSelect>>', self.load_student)

        self.list_box.insert(1, "Students Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)

        self.setup_db()

        self.update_listbox()

root = Tk()
studDB = StudentDB(root)
root.mainloop()
'''



'''
# Use Case Description

# At least 3 functions needed

# I. User clicks a number button (self, number)
#     N3. With each number 'button press' add the new value to the end
#         of the first and then update the entry
# II. User clicks a math button (self, math_func)
#     N1. Make sure entry has a value
#     N2. Switch boolean values representing math buttons to False on entry
#     N3. Have button pass in the math function pressed
#     N4. Store the entry value on entry to this function (Class Field)
#         (this mean that the whole calculator will be a big class object)
#     N5. Clear the entry field
# III. User clicks another number button
# IV. User clicks equal button and the result shows
#     N1. Make sure a math function was clicked
#     N2. Check which math function was clicked and provide the correct solution


# Note 1: Make sure previous required button was clicked
# Note 2: Make a way to track which math button was clicked last
# Note 3: Think about a way to handle the user entering single/multiple numbers
# Note 4: Track(store) the first number in the entry box after a math
#         button is clicked
# Note 5: What about division problems caused by integer division
#     a. Convert to a float each time we retrieve or store values in the entry


from tkinter import *
from tkinter import ttk

class Calculator:
    
    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        if value == 'AC':
            self.number_entry.delete(0, "end")
        else:
            # get curent value in the entry, and store it in entry_value
            entry_val = self.number_entry.get()

            # if they press multiple number buttons, put new value to right of it
            entry_val += value

            # clear entry box
            self.number_entry.delete(0, "end")

            # insert the new value into that box
            self.number_entry.insert(0, entry_val)

    # upon realizing that we need to convert to a float, make new funct
    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        # catch the valueError so that you know it's not a float
        except ValueError:
            return False

    def math_button_press(self, value):

        # only wnat to do something if entry has a value first
        # if have a float value in there, want to turn everything to false
        if self.isfloat(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            self.calc_value= float(self.entry_value.get())

            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        print("self.number_entry: ", type(self.number_entry))
        if self.calc_value != 0:
            if self.div_trigger or self.mult_trigger or self.add_trigger or self.sub_trigger:

                if self.div_trigger:
                    solution = self.calc_value + float(self.entry_value.get())
                elif self.mult_trigger:
                    solution = self.calc_value + float(self.entry_value.get())
                elif self.add_trigger:
                    solution = self.calc_value + float(self.entry_value.get())
                else:
                    solution = self.calc_value + float(self.entry_value.get())

                print(self.calc_value, " ", float(self.entry_value.get()), " ", solution)

                self.div_trigger = False
                self.mult_trigger = False
                self.add_trigger = False
                self.sub_trigger = False

                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, solution)
        else:
            pass


    def __init__(self, root):

        # store the value
        self.entry_value = StringVar(root, value="")

        root.title("Calculator")
        root.geometry("640x280")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)
        
        # text entry box at the top of the screen, tie it to entry_value
        # this way that when entry_value changes, it changes number_entry
        self.number_entry = ttk.Entry(root,
                                    textvariable=self.entry_value,
                                    width=100)
        self.number_entry.grid(row=0, columnspan=4, padx=6)

        # ------ 1st row -------
        self.button7 = ttk.Button(root,
                                text="7",
                                command=lambda:: self.button_press('7')).grid(row=1, column=0, pady=6)
        self.button8 = ttk.Button(root,
                                text="8",
                                command=lambda:: self.button_press('8')).grid(row=1, column=1, pady=6)
        self.button9 = ttk.Button(root,
                                text="9",
                                command=lambda:: self.button_press('9')).grid(row=1, column=2, pady=6)

        self.button_div = ttk.Button(root,
                                text="/",
                                command=lambda:: self.math_button_press('/')).grid(row=1, column=3, pady=6)


        # ------ 2nd row -------
        self.button4 = ttk.Button(root,
                                text="4",
                                command=lambda:: self.button_press('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(root,
                                text="5",
                                command=lambda:: self.button_press('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(root,
                                text="6",
                                command=lambda:: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(root,
                                text="*",
                                command=lambda:: self.math_button_press('*')).grid(row=2, column=3)

        # ------ 3rd row -------
        self.button1 = ttk.Button(root,
                                text="1",
                                command=lambda:: self.button_press('1')).grid(row=3, column=0, pady=6)
        self.button2 = ttk.Button(root,
                                text="2",
                                command=lambda:: self.button_press('2')).grid(row=3, column=1, pady=6)
        self.button3 = ttk.Button(root,
                                text="3",
                                command=lambda:: self.button_press('3')).grid(row=3, column=2, pady=6)

        self.button_add = ttk.Button(root,
                                text="+",
                                command=lambda:: self.math_button_press('+')).grid(row=3, column=3, pady=6)

        # ------ 4th row -------
        self.button_clear = ttk.Button(root,
                                text='AC',
                                command=lambda:: self.button_press('AC')).grid(row=4, column=0)
        self.button0 = ttk.Button(root,
                                text="0",
                                command=lambda:: self.button_press('0')).grid(row=4, column=1)
        self.button_equal = ttk.Button(root,
                                text="=",
                                command=lambda:: self.equal_button_press()).grid(row=4, column=2)
        self.button_sub = ttk.Button(root,
                                text="-",
                                command=lambda:: self.math_button_press('-')).grid(row=4, column=3)

root = Tk()

# create the calculator object
calc = Calculator(root)

root.mainloop()

'''

# User Case Description

# The calculator will be a class, which has functions,
# then we'll call the main program to run the GUI and create an instance of the big class object
# run the loop afterwards

# I. User presses a number button (self, value)
#     N1. print to screen the number
#     N2. start with the math triggers set to False
#     N3. keep the value in storage
#     N4. allow multiple number buttons pressed, just add on to string
# II. User presses a math button (self, math_funct)
#     N1. Store the math button trigger(boolean trigger starting at False)
# III. User presses a number button
#     N2. clear the entered screen value
#     N1. print to screen the number
# IV. User presses the equal button (self)
#     clear the screen
#     perform equivalence depending on whick math button trigger
#     get solution and put it on screen
#     return the boolean triggers to False

# Note 1: Store the number button pressed
# Note 2: convert integers to floats
# Note 3: keep track of when you are changing the num1(stored) and num2(present value)
# Note 4: Allow multiple or single number inputs

from tkinter import *
from tkinter import ttk

class Calculator:

    first_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def number_button_pressed(self, value):
        if value == 'AC':
            self.greenScreen.delete(0, "end")
        else:
            # this is abstraction of the self.entry_number internal value
            entry_val = self.entry_number.get()
            entry_val += value
            # this is for one value at a time added
            self.greenScreen.delete(0, "end")
            # print to the screen
            self.greenScreen.insert(0, entry_val)

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            print("self.entry_number NOT CONVERABLE")
            return False

    def math_button_pressed(self, mult_func):

        # if it is True, that entry number is a float, continue
        if self.is_float(str(self.entry_number.get())):

            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            # store the value
            self.first_value = float(self.entry_number.get())

            if mult_func == "/":
                self.div_trigger = True
            elif mult_func == "*":
                self.mult_trigger = True
            elif mult_func == "+":
                self.add_trigger = True
            else:
                self.sub_trigger = True

        self.greenScreen.delete(0, "end")


    def equal_button_pressed(self):

        # This makes sure only one is pressed, because all are False after
        if self.div_trigger or self.mult_trigger or self.add_trigger or self.sub_trigger:

            if self.div_trigger == True:
                solution = self.first_value / float(self.entry_number.get())
            elif self.mult_trigger == True:
                solution = self.first_value * float(self.entry_number.get())
            elif self.add_trigger == True:
                solution = self.first_value + float(self.entry_number.get())
            elif self.sub_trigger == True:
                solution = self.first_value - float(self.entry_number.get())
            else:
                print("error at equal button pressed")

            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            self.greenScreen.delete(0, "end")
            self.greenScreen.insert(0, solution)


    def __init__(self, root):

        root.geometry("780x250+400+300")
        root.resizable(width=False, height=False)
        root.wm_title("Calculator")
        style = ttk.Style()
        style.configure("TButton",
                        foreground="midnight blue",
                        background="gold",
                        font="Arial 20 bold",
                        padding=5)
        style.configure("TEntry",
                        foreground="midnight blue",
                        background="gold",
                        font="Arial 20 bold",
                        padding=5)

        # This is the one textvariable which is tracked throughout program
        # this is connected to the screen, and can be get, set, inserted, and deleted
        # it starts as a string
        self.entry_number = StringVar()

        self.greenScreen = ttk.Entry(root,
                                textvariable=self.entry_number,
                                width=120)
        # since the linked textvariable updates all the time, only map the textvariable when finished actions
        self.greenScreen.grid(row=0, columnspan=4, ipadx=6, ipady=2)

        # row 1
        self.button7 = ttk.Button(root,
                            text='7',
                            command=lambda: self.number_button_pressed('7')).grid(row=1, column=0, padx=6, pady=4)
        self.button8 = ttk.Button(root,
                            text='8',
                            command=lambda: self.number_button_pressed('8')).grid(row=1, column=1, padx=6, pady=4)
        self.button9 = ttk.Button(root,
                            text='9',
                            command=lambda: self.number_button_pressed('9')).grid(row=1, column=2, padx=6, pady=4)
        self.button_div = ttk.Button(root,
                            text='/',
                            command=lambda: self.math_button_pressed('/')).grid(row=1, column=3, padx=6, pady=4)


        # row 2
        self.button4 = ttk.Button(root,
                            text='4',
                            command=lambda: self.number_button_pressed('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(root,
                            text='5',
                            command=lambda: self.number_button_pressed('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(root,
                            text='6',
                            command=lambda: self.number_button_pressed('6')).grid(row=2, column=2)
        self.button_mult = ttk.Button(root,
                            text='*',
                            command=lambda: self.math_button_pressed('*')).grid(row=2, column=3)


        # row 3
        self.button1 = ttk.Button(root,
                            text='1',
                            command=lambda: self.number_button_pressed('1')).grid(row=3, column=0, padx=6, pady=4)
        self.button2 = ttk.Button(root,
                            text='2',
                            command=lambda: self.number_button_pressed('2')).grid(row=3, column=1, padx=6, pady=4)
        self.button3 = ttk.Button(root,
                            text='3',
                            command=lambda: self.number_button_pressed('3')).grid(row=3, column=2, padx=6, pady=4)
        self.button_add = ttk.Button(root,
                            text='+',
                            command=lambda: self.math_button_pressed('+')).grid(row=3, column=3, padx=6, pady=4)

        # row 4
        self.button_clear = ttk.Button(root,
                            text='AC',
                            command=lambda: self.number_button_pressed('AC')).grid(row=4, column=0)
        self.button0 = ttk.Button(root,
                            text='0',
                            command=lambda: self.number_button_pressed('0')).grid(row=4, column=1)
        self.button_equal = ttk.Button(root,
                            text='=',
                            command=lambda: self.equal_button_pressed()).grid(row=4, column=2)
        self.button_sub = ttk.Button(root,
                            text='-',
                            command=lambda: self.math_button_pressed('-')).grid(row=4, column=3)


def main():

    root = Tk()

    calc = Calculator(root)

    root.mainloop()

main()
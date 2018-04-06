# Use Case Description

# At least 3 functions needed

# I. User clicks a number button (self, value)
#     N3. With each number 'button press' add the new value to the end
#         of the first and then update the entry
# II. User clicks a math button (self, math_func)
#     N1. Make sure entry has a value
#     N2. Switch boolean values representing math buttons to False on entry(Class Field booleans)
#     N3. Have button pass in the math function pressed
#     N4. Store the entry value on entry to this function (Class Field float)
#         (this mean that the whole calculator will be a big class object)
#     N5. Clear the entry field
# III. User clicks another number button
# IV. User clicks equal button and the result shows (self)
#     N1. Make sure a math function was clicked
#     N2. Check which math function was clicked and provide the correct solution

# Note 1: Make sure previous required button was clicked
    # Since every button requires that the previous button was clicked
    # we need to make sure the click occurred.
# Note 2: Make a way to track which math button was clicked last(boolean CLASS FIELDS)
    # Maybe we want to make a way to track which math button was clicked last
    # because ned to know which operation we will be using
# Note 3: Think about a way to handle the user entering single/multiple numbers
    # When they click on the number buttons, they might want to click
    # another number button in a row.
# Note 4: Track(store) the first number in the entry box after a math
#         button is clicked
    # want to track the first number inthe entry box after a math
    # button was clicked. This tells us it is a CLASS FIELD.
# Note 5: What about division problems caused by integer division
#     a. Convert to a float each time we retrieve or store values in the entry
    # Division problems might happen with integer division.
    # We will then convert to a float everytime we retrieve or store values in entry.

from tkinter import *
from tkinter import ttk
import random

class Calculator:
    # store the value eventually
    first_value = 0.0

    # track the different math buttonn that were pressed
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
            entry_val += value # add the next number to the right
            # this is for one value at a time added
            self.greenScreen.delete(0, "end")
            # print to the screen
            self.greenScreen.insert(0, entry_val)

    # I don't fuly understand why when I press math_button subsequently,
    # it brings up the error. What is passing through it that
    # cannot be converted? Oh, it's entry when it is blank.
    def is_float(self, string):
        try:
            float(string)
            return True
        # this just makes it so that we don't get nasty errors,
        # we are just using this to check, not for an action it the code.
        except ValueError:
            print("self.entry_number NOT CONVERTABLE", random.randint(0, 10))
            return False

    def math_button_pressed(self, mult_func):

        # if it is True, that entry number is a float, continue
        # go and do something only when we know that a number is
        # within the entry. We are also looking for a float...
        # at this point we must check if the value in the entry box
        # is actually a float.(have it return True or False)
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

        # make sure a button was pressed, not really helping too much
        # just makes it so that we are allowed to do whatever below
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

        root.geometry("790x250+400+300")
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
        # I am not sure but this StringVar doesn't take in root,value.
        # I guess it assumes that it's a string... and root anywya.
        # ACTUALLY, MAYBE THIS IS WHY ENTRY STYLE IS NOT AFFECTED.
        # Actually, this is not the way.
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
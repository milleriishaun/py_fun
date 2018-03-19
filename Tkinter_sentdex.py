# Intermediate sendex Tkinter tutorial series 29 vids(~10mins each)
# Going through this to learn proper class/function management
# also using matplotlib
# create a Tkinter BitCoin tracker

# FOUNDATION FOR THE APP BELOW
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

# base for adding a frame
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # when have a bunch of windows, can insert window here
        # then go down to StartPage class and create a for loop to choose one
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew") # alignment+stretch=sticky

        self.show_frame(StartPage)

    def show_frame(self, cont): # controller=cont

        frame = self.frames[cont] # tkRaise raises one of the hidden frame to front
        frame.tkraise()

def qf(param):
    print(param)

# Use lambda to create a quick function that can be thrown away


# Now we need to starta frame
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font="LARGE_FONT")
        label.pack(padx=10, pady=10)

        button2 = tk.Button(self, text="Visit Page 1", command=qf("yoyoyoy"))
        button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))

        button1.pack()

    # Add here if we want to insert a new page


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font="LARGE_FONT")
        label.pack(padx=10, pady=10)

        # button1 = tk.Button(self, text="Visit Page 1", command=qf("yoyoyoy"))
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.pack()

# FOUNDATION FOR THE APP ABOVE
# adding more button and code affects PageOne function
app = SeaofBTCapp()
app.mainloop()
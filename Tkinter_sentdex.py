# Intermediate sendex Tkinter tutorial series 29 vids(~10mins each)
# Going through this to learn proper class/function management
# also using matplotlib
# create a Tkinter BitCoin tracker

# So far, this program is a live tkinter app, with multiple pages, and live graph

# FOUNDATION FOR THE APP BELOW
import tkinter as tk
# like css for tkinter
from tkinter import ttk

# get matplotlib for our graphs
import matplotlib
# this is the backend of matplotlib... important so everything works
matplotlib.use("TkAgg")
# get canvas for graph to sit on and navbar for forward/back/zoom
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# make sure to draw figures
from matplotlib.figure import Figure

# import the animation from matplotlib
import matplotlib.animation as animation
from matplotlib import style


# now we have to use these modules to manage the datasets/limiting data
# tikc data has all the buys and sells,
# want to have open high/open low candlesticks to make sense
# we want to be able to modify the data... so impor these modules
import urllib
import json

# data manipulation
import pandas as pd
# number crunching
import numpy as np

from matplotlib import pyplot as plt


SMALL_FONT = ("Verdana", 8)
NORM_FONT = ("Verdana", 10)
LARGE_FONT = ("Verdana", 12)

# add a style for the graph
style.use("ggplot")

# display of the graph is hard to configure
f = Figure()
# add a subplot to this figure
a = f.add_subplot(111)
# add the plot point data (x[], y[])
# a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5]) # not using this again
# we want to clear the data, so it isn't just adding graphs up and taking RAM


# we need to add an indicator counter, indicator updates the part even while
# the graph only loads every 10 seconds
# force an update
exchange = "Bitfinex"
datCounter = 9000
programName = "bitfinex"



def changeExchange(toWhat, pn):
    global echange
    global datCounter
    global programName

    exchange = toWhat
    programName = pn
    datCounter = 9000


# popupmsg
def popupmsg(msg):
    # mini tkinter instance... notice mainloop
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# need an animation function using matplotlib
# this is our main animation function
# but the animation can update other things too,
# animate function works with matplotlib, but animate can also
# update the tkinter code... even though tkinter has its own update function
# The core of the updates are going to happen in this animation
def animate(i):
    # need a data link
    # use the BTC API... er the BITFINEX API
    # we'll get the last trades(gives us historical data)...
    # (as opposed to ticks which gives us info but not population of a graph right away) 
    # for last trades... can do up to 2000 of the last ones
    # with the info, check which are bids and which are asks
    # This is a generated data set, and the last info was a UNIX timestamp

    # All the below makes the program go too slow and is not live
    # even without this slow code, it is still slow to resize window
    # r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2016-03-19&end=2018-03-19', verify=False)
    # real data from few years
    # get the BitCoin Price Index
    # for k, v in r.json()['bpi'].items():
    #     print(k, v)
    # a.clear()
    # a.plot(r.json()['bpi'].keys(), r.json()['bpi'].values())
    
    dataLink = "https://api.bitfinex.com/v1/trades/BTCUSD?limit_trades=2000"
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode("utf-8")
    data = json.loads(data)
    # data = data["btc_usd"] is useless for us

    data = pd.DataFrame(data)

    # Buys
    buys = data[(data["type"]=="buy")]# changed to match the api response bid is now buy
    # datestamp
    buys["datestamp"]= np.array(buys["timestamp"]).astype("datetime64[s]")
    # throw it at matplotlib
    buyDates = (buys["datestamp"]).tolist()

    sells = data[(data["type"]=="sell")] # changed to match the api response ask is now sell
    sells["datestamp"]= np.array(sells["timestamp"]).astype("datetime64[s]")
    sellDates = (sells["datestamp"]).tolist()

    # update the graph
    a.clear()
    a.plot_date(buyDates, buys["price"], "#00A3E0", label="buys")
    a.plot_date(sellDates,sells["price"], "#183A54", label="sells")

    # fix the legend to not cover the data
    a.legend(bbox_to_anchor=(0, 1.02, 1, 1.02), loc=3,
            ncol=2, borderaxespad=0)

    title = "Bitfinex BTC/USD Prices\nLast Price: " + str(data["price"][99])
    a.set_title(title)
    
'''
#old animate using info from sampleData file
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    # now we want to clear all the data and redraw it
    a.clear()
    a.plot(xList, yList)
'''



# base for adding a frame
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # insert the icon int eh corner, rather than the feather
        tk.Tk.iconbitmap(self, default="favicon.ico")

        # change the title
        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # just some options in the menubar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        # now place the menubar
        menubar.add_cascade(label="File", menu=filemenu)

        # new menu option
        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="Bitfinex",
                                    command=lambda: changeExchange("Bitfinex", "bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                                    command=lambda: changeExchange("Bitstamp", "bitstamp"))
        exchangeChoice.add_command(label="Huobi",
                                    command=lambda: changeExchange("Huobi", "huobi"))


        tk.Tk.config(self, menu=menubar)

        # when have a bunch of windows, can insert window here
        # then go down to StartPage class and create a for loop to choose one
        # every new page has to go throguh self.frames... just like StartPage
        # so just add a for loop
        self.frames = {}
        
        # says later on, "hey I want to show this frame"
        # add any newe pages to the tuple
        for F in (StartPage, BTCe_Page):
            frame = F(container, self)
            self.frames[F] = frame
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
        label = tk.Label(self, text="""ALPHA Bitcoin Trading Application
        Use at your own risk. There is not promise
        of warranty.""", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # button2 = tk.Button(self, text="Visit Page 1", command=qf("yoyoyoy"))
        # make s a throwaway function, and the point is so that it runs immediately rather than when called.
        # Can't pass through variables usng lambda, have to first tell the computer that 
        # that it is using a different button.
        button = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(BTCe_Page))

        button.pack()

    # Add here if we want to insert a new page
        button2 = ttk.Button(self, text="Disagree", command=quit)

        button2.pack()

# PageOne is just a reference, it is not in main SeaofBTCapp
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # button1 = tk.Button(self, text="Visit Page 1", command=qf("yoyoyoy"))
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.pack()

'''
        button2 = ttk.Button(self, text="Page two", command=lambda: controller.show_frame(PageTwo))

        button2.pack()
'''





'''
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # button1 = tk.Button(self, text="Visit Page 1", command=qf("yoyoyoy"))
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.pack()

        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))

        button2.pack()
'''

# Page 3 for our graphs
class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.pack()



        # bring up the canvas
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # we also want the navigation bar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # we want the graph to be autoupdating(maybe daemon working through tcl)
        # but not sure how to do it in tkinter, but can in matplotlib
        # we want live updates
        # we will use animation function to update/redraw graph every 2 secs



        # plot first, add the canvas, show it, put stuff to the canvas, add the navbar


# FOUNDATION FOR THE APP ABOVE
# adding more button and code affects PageOne function
app = SeaofBTCapp()

# make size of app, more than enouh for graph
app.geometry("1280x720")

#get the animation in before the mainloop
# 100 milliseconds = 1 sec
# need to make the text document with the sample data
ani = animation.FuncAnimation(f, animate, interval=10000)

app.mainloop()

# maybe check out matplotlib tutorial series
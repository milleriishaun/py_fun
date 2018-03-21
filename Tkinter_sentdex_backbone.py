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



exchange = "Bitfinex"
# we need to add an indicator counter, indicator updates the part even while
# the graph only loads every 10 seconds
# force an update
datCounter = 9000
programName = "bitfinex"

# default graph data/candles
reSampleSize = "15Min"
dataPace = "1d"
candleWidth = 0.008

# indicator defaults
topIndicator = "none"
middleIndicator = "none"
bottomIndicator = "none"
# allow user to get an infinite amount of SMA/EMA
SMAs = []
EMAs = []

# use the constant for the chart Load, default is True
chartLoad = True


def tutorial():
    # def leavemini(what):
        # what.destroy()
    
    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3!")

            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done!", command=tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title("Part 2!")

        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command=page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(tut, text = "Overview of the application", command=page2)
    B1.pack()

    B2 = ttk.Button(tut, text = "How do I trade with this client?", command=lambda: popupmsg("Not yet completed"))
    B2.pack()

    # How do indicators work
    # How do I trade with that API
    # questions like how do I connect to that API on that Exchange
    B3 = ttk.Button(tut, text = "Indicator Questions/Help", command=lambda: popupmsg("Not yet complete"))
    B3.pack()

    tut.mainloop()

# note that chartLoad is animation... and algorithmic trading
# and eventually we will have to create a headless version, which doesn't have a GUI
# The reason is to not have to update graph every time for automated trading
# run on a cloud server like digital ocean, can't have a GUI
def loadChart(run):
    global chartLoad
    if run == "start":
        charLoad = True



# MIDDLE INDICATOR
def addMiddleIndicator(what):
    # this is so that there is no 30 sec waiting time til update
    # we need it to update immediately
    global middleIndicator
    global datCounter
    
    # if watching tick data, don't need to watch RSI, etc... so popup
    if dataPace == "tick":
        popupmsg("Indicators in Tick Data not available. Choose 1 minute tf if you want short term.")

    # this is for the sma
    if what != "none":
        # is the indicator currently none?
        if middleIndicator == "none":
            # if user wants to do a simple moving avg
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global datCounter

                    # this says any interval is good
                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    datCounter = 9000
                    print("middle indicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            # if user wants to do a simple moving avg
            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global datCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    datCounter = 9000
                    print("middle indicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()  


        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to consider.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global datCounter

                    # this says not any interval is good
                    # middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    datCounter = 9000
                    print("middle indicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            # if user wants to do a simple moving avg
            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global datCounter

                    # middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    datCounter = 9000
                    print("middle indicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop() 

    else:
        middleIndicator = "none"

# TOP INDICATOR
def addTopIndicator(what):
    # this is so that there is no 30 sec waiting time til update
    # we need it to update immediately
    global topIndicator
    global datCounter
    
    # if watching tick data, don't need to watch RSI, etc... so popup
    if dataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")
    
    # force the update to remove the indicator from the graph
    elif what == "none":
        topIndicator = what
        datCounter = 9000

    elif what == "rsi":
        # ask the user a period of time first before get RSI applied
        # (generally 14 day interval when applied, but we want to allow user to choose interval)
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        # just put in a default if someone doesn't know
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global datCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)

            topIndicator = group
            datCounter = 9000
            # print to the console
            print("Set top indicator to ", group)
            # close the window once entered+callback
            rsiQ.destroy()

        # button configging
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    # there's 3 main values for macd that people use, but he forgets
    elif what == "macd":
        # global topIndicator
        # global datCounter
        topIndicator = "macd"
        datCounter = 9000



# add the BOTTOM INDICATOR
def addBottomIndicator(what):
    # this is so that there is no 30 sec waiting time til update
    # we need it to update immediately
    global bottomIndicator
    global datCounter
    
    # if watching tick data, don't need to watch RSI, etc... so popup
    if dataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")
    
    # force the update to remove the indicator from the graph
    elif what == "none":
        bottomIndicator = what
        datCounter = 9000

    elif what == "rsi":
        # ask the user a period of time first before get RSI applied
        # (generally 14 day interval when applied, but we want to allow user to choose interval)
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        # just put in a default if someone doesn't know
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global datCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)

            bottomIndicator = group
            datCounter = 9000
            # print to the console
            print("Set bottom indicator to ", group)
            # close the window once entered+callback
            rsiQ.destroy()

        # button configging
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    # there's 3 main values for macd that people use, but he forgets
    elif what == "macd":
        # global bottomIndicator
        # global datCounter
        bottomIndicator = "macd"
        datCounter = 9000







def changeTimeFrame(tf):
    global dataPace
    global datCounter
    if tf == "7d" and reSampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC Interval")
    else:
        dataPace = tf
        datCounter = 9000

# size of the bar, and width of the candle
def changeSampleSize(size, width):
    global reSampleSize
    global datCounter
    global candleWidth
    if dataPace == "7d" and reSampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC Interval")
    elif dataPace == "tick":
        popupmsg("You're currently viewing tick data, not OHLC.")
    else:
        reSampleSize = size
        datCounter = 9000
        candleWidth = width


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
        # now place the exchange menubar
        menubar.add_cascade(label="Exchange", menu=exchangeChoice)


        # how much data are we going to be looking at
        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label = "Tick",
                            command=lambda: changeTimeFrame('tick'))
        dataTF.add_command(label = "1 Day",
                            command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label = "3 Day",
                            command=lambda: changeTimeFrame('3d'))
        dataTF.add_command(label = "1 Week",
                            command=lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label = "Data Time Frame", menu = dataTF)

        # Config the Open High, Low Close...(width of the candlestick)
        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label = "Tick",
                            command=lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label = "1 Minute",
                            command=lambda: changeSampleSize('1Min', 0.0005))
        OHLCI.add_command(label = "5 Minute",
                            command=lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label = "15 Minute",
                            command=lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label = "30 Minute",
                            command=lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label = "1 Hour",
                            command=lambda: changeSampleSize('1H', 0.032))
        OHLCI.add_command(label = "3 Hour",
                            command=lambda: changeSampleSize('3H', 0.096))
        menubar.add_cascade(label = "OHLC Interval", menu = OHLCI)

        # with the graph, we wnat a TOP Indicator(RSI(relative strength index), or macd)
        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label = "None",
                            command=lambda: addTopIndicator('none'))
        topIndi.add_command(label = "RSI",
                            command=lambda: addTopIndicator('rsi'))
        topIndi.add_command(label = "MACD",
                            command=lambda: addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)

        # we also want a MIDDLE Indicator(SMA(simple moving average), EMA(exponential moving average))
        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label = "None",
                            command=lambda: addMiddleIndicator('none'))
        mainI.add_command(label = "SMA",
                            command=lambda: addMiddleIndicator('sma'))
        mainI.add_command(label = "EMA",
                            command=lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label="Main/middle Indicator", menu=mainI)

        # and now we want a BOTTOM Indicator
        bottomI = tk.Menu(menubar, tearoff=1)
        bottomI.add_command(label = "None",
                            command=lambda: addBottomIndicator('none'))
        bottomI.add_command(label = "SMA",
                            command=lambda: addBottomIndicator('sma'))
        bottomI.add_command(label = "EMA",
                            command=lambda: addBottomIndicator('ema'))
        menubar.add_cascade(label="Bottom Indicator", menu=bottomI)




        # want people to be able to make trades.. buy/sell
        # we want to set up preset offers... anc bind it to keypresses
        tradeButton = tk.Menu(menubar, tearoff=1)
        # ppl trade with simple rules like SMA>10, trade, or< 10 trade
        tradeButton.add_command(label="Manual Trading",
                                command=lambda: popupmsg("This is not live yet!"))
        tradeButton.add_command(label="Automated Trading",
                                command=lambda: popupmsg("This is not live yet!"))

        # user can do quick buy and sell(fee for trading)
        # different amounts of buying and selling because of the fee.middleIndicator
        tradeButton.add_command(label="Quick Buy",
                                command=lambda: popupmsg("This is not live yet!"))
        tradeButton.add_command(label="Quick Sell",
                                command=lambda: popupmsg("This is not live yet!"))

        tradeButton.add_command(label="Set-up Quick Buy/Sell",
                                command=lambda: popupmsg("This is not live yet!"))

        menubar.add_cascade(label="Trading", menu=tradeButton)

        # want to start and stop so that when we zoom in, we want to freeze screen
        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume",
                                command=lambda: loadChart('start'))
        startStop.add_command(label="Pause",
                                command=lambda: loadChart('stop'))                      
        menubar.add_cascade(label="Resume/Pause client", menu=startStop)

        # add a help Menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpmenu)



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
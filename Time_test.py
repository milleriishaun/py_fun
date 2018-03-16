# These are all the time functions that I am aware of

#ticking function to show time
def tick():
    global time1
    global timeHour1
    global timeMin1
    global timeSec1


    # Current local time
    time2 = time.strftime('%H:%M:%S')
    timeHour2 = time.strftime('%H')
    timeMin2 = time.strftime('%M')
    timeSec2 = time.strftime('%S')
    # update time1 if old
    if time2 != time1:
        time1 = time2
        timeHour1 = timeHour2
        timeMin1 = timeMin2
        timeSec1 = timeSec2
        clock_output.config(text=time2)
    # calls self every 200 milliseconds, recursive
    clock_output.after(200, tick)


# basic time manipulation
# get the current time...which is ticks
ticks = time.time()

# convert the time to readable time Tuple
time2 = time.localtime(ticks)

# set up a clock variable type stringVar
clock = StringVar()
# set the clock
clock.set("{}:{}:{}".format(time2[3], time2[4], time2[5]))

clock_var = clock.get()


# superfluous print out of the clock just to make sure
print(clock_var)

# for the function
tick()

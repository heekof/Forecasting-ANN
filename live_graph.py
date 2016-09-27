import numpy as np
from util import *
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.animation as animation
import time
import datetime as dt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    pullData = open("Data/data_demo.csv","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    zar = []
    p = 0;
    for eachLine in dataArray:
        if len(eachLine)>1 and p==1:
            t,x,y = eachLine.split(';')
            xar.append(float(x))
            yar.append(float(t))
            zar.append(float(y))
        p = 1
    ax1.clear()
    ax1.set_title("Realtime metric CPU Plot")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Values in %")
    ax1.plot(yar,xar)
    ax1.plot(yar,zar)
        #time.sleep(1)



ani = animation.FuncAnimation(fig, animate,interval=1000)



plt.show()

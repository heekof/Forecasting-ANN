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
    pullData = open("load.csv","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(';')
            xar.append(float(x))
            yar.append(float(y))


    ax1.clear()
    ax1.set_title("Realtime metric M Plot")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Values")
    ax1.plot(xar,yar)




ani = animation.FuncAnimation(fig, animate,interval=1000)



plt.show()

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
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



import pandas as pd
import numpy as np


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")




fig = plt.figure(figsize=(15,10), dpi=150)
ax1 = fig.add_subplot(1,1,1)

def animate(i):


    data = DataFrame.from_csv("Data/data_df.csv",sep=';')
    buys = data.index
    buys
    temps = np.array(buys).astype("datetime64[s]")
    buyDates = temps.tolist()
    buyDates

    A = data['load.avg_1_min'];
    B = data['cpu.wait_perc'];

    ax1.clear()

    ax1.set_title("Realtime metric "+str(data.columns.values))
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Values")
    ax1.plot(buys,B)
    ax1.plot(buys,A)






ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()

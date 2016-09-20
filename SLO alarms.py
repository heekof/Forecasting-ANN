
# coding: utf-8

# In[26]:
from __future__ import division
import pandas
import datetime
import time
from time import gmtime, strftime
import os
# Import libraries use for visualization and analysis
import pandas as pd
import numpy as np
#get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt

import cufflinks as cf

from monascaclient import client
from monascaclient import ksclient


from pandas import Series,DataFrame

import math


# Import library to execute remote commands for monasca-agent demo
import spur
import matplotlib.pyplot as plt
import seaborn as sns

import time as t
import datetime as dt

from sklearn.metrics import mean_squared_error
from math import sqrt



# In[27]:

dframe = pandas.read_csv("Data/training_data.csv",index_col='Timestamp',engine='python',sep=";")
dataset = dframe.values
dataset = dataset.astype('float32')
dataset




# In[28]:


# In[31]:

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("Data/data_demo.csv","r")
    loglines = follow(logfile)
    i=0;
    for line in loglines:
        #print line,

        print '\n \n ======================  Step '+str(i)+'  ======================== \n \n'
        print 'The predicted value is :'
        index = float(line.split(';')[0]) + 60;
        pred = line.split(';')[2];
        print pred;
        print 'The Real value is :'
        real = line.split(';')[1];
        print real;
        print 'The Amplitude  Error is  :'
        print sqrt(((float)(pred)-(float)(real))**2)
        val = dataset[i+2];
        if dframe.ix[index]['cpu.wait_perc']:
            print ' \n SLO 1 breach probability :'+str(dframe.ix[index]['cpu.wait_perc']/30)+'\n'
            if (14 - (float)(dframe.ix[index]['cpu.wait_perc'])) <= 0:

                print '********* Alarm ****** SLO cpu will be breached *************** \n'
                #print val;
                print '********* Alarm ****** SLO cpu will be breached *************** \n'

##
##

        print '\n \n ============================================== \n \n'
        i += 1;


# In[ ]:

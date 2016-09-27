
# In[26]:
from __future__ import division
import pandas
from pandas import DataFrame
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

#import cufflinks as cf

from monascaclient import client
from monascaclient import ksclient


from pandas import Series,DataFrame

import math


# Import library to execute remote commands for monasca-agent demo
#import spur
import matplotlib.pyplot as plt
#import seaborn as sns

import time as t
import datetime as dt

from sklearn.metrics import mean_squared_error
from math import sqrt
import logging


logging.basicConfig(filename='log/example.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
#logging.disable(logging.debug)


# In[27]:

dframe = pandas.read_csv("Data/training_data.csv",index_col='Timestamp',engine='python',sep=";")
dataset = dframe.values
dataset = dataset.astype('float32')
dataset

df_x = DataFrame.from_csv("Data/data_with_predictions.csv",index_col='Timestamp',sep=";")


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

#df_slo = pd.DataFrame(columns=('id','name','SLO'))

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

        Condition = index in df_x.index;
        if Condition:
            print ' \n SLO 1 breach probability :'+str(dframe.ix[index]['cpu.wait_perc']/30)+'\n'
            if (14 - (float)(dframe.ix[index]['cpu.wait_perc'])) <= 0:
                logging.debug('CPU = %s' % dframe.ix[index]['cpu.wait_perc'] )
                print '********* Alarm ****** SLO cpu will be breached *************** \n'
                #print val;
                print '********* Alarm ****** SLO cpu will be breached *************** \n'
                id = i;
                Name = "SLO Alarm - SLO will be breached"
                SLO_id = "1"
                d = pd.DataFrame(index=[id], data={ 'Alarm name' : 'Warning SLO will be breached','SLO_id' : SLO_id })
                d.to_csv("Data/alarms.csv",header=True,index=True,sep=';',index_label='Alarm ID')

##
##

        print '\n \n ============================================== \n \n'
        i += 1;


# In[ ]:

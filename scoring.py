import pandas as pd
import numpy as np
import math
import time
import datetime
import logging 
logging.basicConfig(filename='demo.log',level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
#logging.disable(logging.debug)


dframe = pd.read_csv("Data/data_with_predictions.csv",index_col='Timestamp',engine='python',sep=";")
for i in xrange(len(dframe)):
    if i != 0:
        dframe.head(i).to_csv('Data/data_demo.csv',header=True,index=True,sep=';')
        time.sleep(2)
        print ("step ", i)



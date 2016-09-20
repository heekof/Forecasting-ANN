import datetime
import time

# Import libraries use for visualization and analysis
import pandas as pd
import numpy as np




import cufflinks as cf


OS_PROJECT_NAME='mini-mon'
password='password'
OS_AUTH_URL='http://157.159.232.218:35357/v3/'
username='mini-mon'
MONASCA_API_URL='http://157.159.232.217:8070/v2.0/'
monasca_url = 'http://157.159.232.217:8070/v2.0/'

keystone_url = 'http://157.159.232.218:35357/v3/'
api_version = '2_0'






def df_from_measurements(raw, group):
    i=0
    log=0;
    df = pd.DataFrame()
    for s in raw:
        if s[0]['measurements'] and s[0]['dimensions']['hostname'] == group:
            m = np.array(s[0]['measurements'])
            timestamps = m[:, s[0]['columns'].index('timestamp')]
            df = pd.DataFrame(index = timestamps)
            break;
    m=0;
    for measure in raw:
        if measure[0]['measurements'] and measure[0]['dimensions']['hostname'] == group:
            hostname=group
            m = np.array(measure[0]['measurements'])
            timestamps = m[:, measure[0]['columns'].index('timestamp')]
            #df = pd.DataFrame(index = timestamps)
            #getting name
            if(log==1):
                print 'metric : \n'
                print measure[0]['name']
            name = measure[0]['name'];
            #getting dimensions
            if(log==1):
                print '\n Machine name : \n'
                print measure[0]['dimensions']['hostname']
            # Getting measurement
            if(log==1):
                print '\n measurements \n'
                print m#measure[0]['measurements']

            # Measurement into Array

            m = np.array(measure[0]['measurements'])


            timestamps = m[:, measure[0]['columns'].index('timestamp')]
            if(log==1):
                print timestamps


            values=m[:, measure[0]['columns'].index('value')]
            if(log==1):
                print '\n values \n '
                print values

            #vars()["df_"+str(i)] =  dict( zip( timestamps, m));

            df[name] = m[:, measure[0]['columns'].index('value')];

            if(log == 1):
                    print 'This is the dataframe'+'is'+name

            #vars()["df_"+str(i)]['hostname'] = hostname;

            if(log==1):
                print ' \n \n ***********  --------------- *********** \n'
            i=i+1;
    return df;




def Timestamp(df):
    tsp = np.array(df.index)
    i=0;
    for ind in tsp:
        tsp[i] = time.mktime(datetime.datetime.strptime(repr(str(ind))[1:-1], '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())
        i += 1;
    return tsp


def stamped_df(dframe):
    
    dframe['Timestamp']=Timestamp(dframe)
    dframe.index.names = [None]
    dframe = dframe.reset_index(drop=True)
    dframe = dframe.set_index('Timestamp')
    
    
    return dframe



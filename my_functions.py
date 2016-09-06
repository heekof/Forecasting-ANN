## Function for basic DATAFRAMES

bb = 3;
def cal():
    return 3;








'''
def test_func(x):
    print x

# Connect to monasca server
def monasca_connect(k,c):
    ksclient = k
    client = c
    api_version = '2_0'
    monasca_url = 'http://157.159.232.217:8070/v2.0/'
    # Authenticate to Keystone
    keystone_url = 'http://157.159.232.218:35357/v3/'
    ks = ksclient.KSClient(auth_url=keystone_url, username='mini-mon', password='password')
    # construct the mon client
    monasca_client = client.Client(api_version, monasca_url, token=ks.token)




# compute the autocorrelation
def autocorr(x):
    result = np.correlate(x,x,mode='full')
    return result[result.size/2]
# write dataframe to a CSV file
def write_to_csv(filename,df):
    dframe = DataFrame(df,columns=['valeur'])
    dframe.to_csv(filename,sep=';',index=False,header=None)

# Normalize inputs
def normalize(X):
        return X/X.sum()


# Computing DataFrame rolling avreage
def rolling_avg(X,m):
    mean = np.asarray(pd.rolling_mean(df_slice['valeur'],m))
    return mean[~np.isnan(mean)]

# Compute a the percentage change of an array
def percentage_change(X):
    return [100.0 * a1/a2 - 100 for a1, a2 in zip(X[1:], X)]

def SLO_mapping(ids,feature1,feature2,feature3,feature4):
    if(ids == 1):
        return feature1*feature2
    elif(ids == 2):
        return feature3*feature2
    elif(ids == 3)
        return feature1*0.2/feature1
    else return 0

def SLO_breach(val,alpha)
    if(val >= alpha):
           return 1
    else return 0





def unnorm(y_arr2):
    y_arr3 = np.zeros(y_arr2.size)
    for i in range(y_arr2.size):
        y_arr3[i] = y_arr2[i] * normx+normy
    return y_arr3


# Ploting data
def plot(x,y,points):
    plt.subplots(figsize=(30, 10))
    tmps = np.arange(points)
    plt.plot(tmps,x[:points],'r--')
    plt.plot(tmps,y[:points],'b-')

def recadrer(h,window):
    h_out = np.zeros(len(h)+window)
    i=0;
    for i in range(h_out.size):
        if i >= window:
            h_out[i] = h[i-window]
        else:
            h_out[i] = 0
    return h_out
'''

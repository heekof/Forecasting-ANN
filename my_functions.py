# Import the Monasca and Keystone clients
#from monascaclient import client
#from monascaclient import ksclient


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


# getting the metrics information
def get_metrics(names=[None], dimensions={}, limit=10):
    metrics = []
    for name in names:
        # Invoke the Monasca client
        metrics = metrics + monasca_client.metrics.list(name=name, dimensions=dimensions, limit=limit)
    return metrics

# function get measurements
def get_measurements(metrics, start_time = None, end_time = None, limit=None):
    measurements = []

    if start_time == None:
        start_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=3600)
        start_time = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    if end_time == None:
        end_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=0)
        end_time = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    for metric in metrics:
        # Invoke the Monasca client
        measurements.append(monasca_client.metrics.list_measurements(
                name=metric['name'],
                dimensions=metric['dimensions'],
                start_time=start_time,
                end_time=end_time))

    return measurements


# Unfortunatelly this function is not working
def df_from_measurements(measurements, group_by=[]):
    '''Returns a DataFrame given measurements'''
    measurement = measurements[1]
    m = np.array(measurement[0]['measurements'])
    timestamps = m[:, measurement[0]['columns'].index('timestamp')]
    df = pd.DataFrame(index = timestamps)

    for measurement in measurements:
        if measurement:
            measure = measurement
            m = np.array(measure[0]['measurements'])
            name = measure[0]['name']
            dimensions = measure[0]['dimensions']

            for group in group_by:
                if group in dimensions:
                    name += '.' + dimensions[group]
            #df[name] = m[:measure[1][0]['columns'].index('value')]
    return df

# getting my DataFrame df
def get_df():
    i = 0;
    max = len(measurements);
    for measure in measurements:
        if measure:

            data = np.array(measure[0]['measurements'])
            metric_name = measure[0]['name']
            hostname = measure[0]['dimensions'].get('hostname')
            service = measure[0]['dimensions'].get('service')
            timestamp = ["" for x in range(len(data))]
            values = np.zeros(len(data))
            i = i + 1;
            i=0;
            if hostname == "mini-mon" and metric_name == "net.out_packets_sec":
                for d in data:
                    timestamp[i] = d[0]
                    values[i] = d[1]
                    i = i + 1
                df = pd.DataFrame(index = timestamp)
                df['name'] = metric_name
                df[service] = service
                df[hostname] = hostname
                df['valeur'] = values
                df['time'] = np.arange(len(timestamp))
    return df;

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


# Structuring data before the inputs
def structure_data(X,window,sel):
    if sel == 0:
        y = X[window:]
        y_l = [ [y[i]] for i in range(y.size) ]
        X_input =  np.resize(X,(X.size/window,window))
        X_l = X_input.tolist()
        return X_l,y_l,y
    else:
        y = X[step_size:]
        y_l = [ [y[i]] for i in range(y.size) ]
        X = X[:-step_size]
        X_l = [ [X[i]] for i in range(X.size) ]
        return X_l,y_l,y

# getting the prediction in the form of an array
def get_prediction(Xi,norm):
    if norm == 0:
        return [ nn.predict(X[i])[0]*normx+normy for i in range(len(X))]
    else:
        return [ Xi[i] + nn.predict([Xi[i]])[0]*Xi[i] for i in range(len(Xi))]


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

import pandas
import numpy
import math


#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
# We will use Keras library
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
# And Scikit-Learn
from sklearn.preprocessing import MinMaxScaler

#dataframe = pandas.read_csv('Data/international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3,sep=';')

#  Here we take only the raw values dataframe['Passengers'] ! = dataframe.values

dataframe = pandas.read_csv("Data/data_df.csv", usecols=["cpu.wait_perc"], engine='python',sep=";")

dataset = dataframe.values
dataset = dataset.astype('float32')


# split into train and test sets
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)

X, Y = create_dataset(dataset[1:10],1)

# reshape into X=t and Y=t+1

## The window

look_back = 1

trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)


# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_dim=look_back))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=500, batch_size=1, verbose=2)

# generate predictions for training
trainPredict = model.predict(trainX,verbose=0)
testPredict = model.predict(testX,verbose=0)

# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# plot baseline and predictions


plt.figure(figsize=(15, 10), dpi=100)
plt.title("Learning")
plt.xlabel("Time")
plt.ylabel("Values")
plt.plot(dataset)
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)




plt.show()

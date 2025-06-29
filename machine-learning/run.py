import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Input

now = datetime.now()
start = datetime(now.year - 10, now.month, now.day)

df = yf.download("AAPL", start, now)
print(df.describe())


#feature engineering

df['MA_100'] = df['Close'].rolling(window=100).mean()

# plt.figure(figsize=(14, 7))
# plt.plot(df['Close'], label='Close Price', color='blue')
# plt.plot(df['MA_100'], label='MA 100', color='red')
# plt.show()




data_train = df[0:int(0.7*len(df))]['Close'].values.reshape(-1, 1)
data_test = df[int(0.7*len(df)):int(len(df))]['Close'].values.reshape(-1, 1)

data_train = MinMaxScaler(feature_range=(0,1)).fit_transform(data_train)


x_train = []
y_train = []

for i in range(100, data_train.shape[0]):
    x_train.append(data_train[i-100: i])
    y_train.append(data_train[i, 0])
    #print(data_train[i-100: i])
    
x_train, y_train = np.array(x_train), np.array(y_train)


model = Sequential()
model.add(Input(shape=(100, 1)))
model.add(LSTM(units=128, activation='tanh', return_sequences=True))
model.add(LSTM(units=64))
model.add(Dense(25))
model.add(Dense(1))


model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=50)

model.save('model.keras')

# from tensorflow.keras.models import load_model

# # Load the model from the file path
# model_path = r"D:\Projects\stock-predictor\model.keras"
# model = load_model(model_path)

# # Print the model summary
# model.summary()
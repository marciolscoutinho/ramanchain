import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class LoadPredictor:
    def __init__(self):
        self.model = Sequential()
        self.model.add(LSTM(50, activation='relu', input_shape=(10, 1)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')

    def train_model(self, data, labels, epochs=50):
        data = np.array(data).reshape((len(data), 10, 1))
        labels = np.array(labels)
        self.model.fit(data, labels, epochs=epochs, verbose=0)

    def predict_load(self, recent_data):
        recent_data = np.array(recent_data).reshape((1, 10, 1))
        return self.model.predict(recent_data)[0][0]

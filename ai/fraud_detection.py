from sklearn.ensemble import IsolationForest
import numpy as np

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.transaction_data = []

    def train_model(self, transaction_data):
        self.transaction_data = transaction_data
        self.model.fit(np.array(transaction_data))

    def detect_fraud(self, transaction_features):
        prediction = self.model.predict(np.array([transaction_features]))
        return prediction[0] == -1

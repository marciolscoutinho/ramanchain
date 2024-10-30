from sklearn.linear_model import LinearRegression
import numpy as np

class EnergyOptimizer:
    def __init__(self):
        self.model = LinearRegression()
        self.energy_data = []
        self.complexity_data = []

    def train_model(self, energy_data, complexity_data):
        self.model.fit(np.array(energy_data).reshape(-1, 1), complexity_data)

    def predict_complexity(self, energy_consumption):
        return self.model.predict(np.array([[energy_consumption]]))[0]

    def adjust_complexity(self, current_energy, current_complexity):
        self.energy_data.append([current_energy])
        self.complexity_data.append(current_complexity)
        self.train_model(self.energy_data, self.complexity_data)

        predicted_complexity = self.predict_complexity(current_energy)
        if current_energy > 500:
            return max(1, current_complexity - 1)
        elif current_energy < 200:
            return current_complexity + 1
        return current_complexity

import numpy as np
from sklearn.ensemble import RandomForestRegressor

class PortfolioManager
    def __init__(self)
        self.model = RandomForestRegressor()

    def train_model(self, features, target)
        self.model.fit(features, target)

    def predict_allocation(self, market_conditions)
        return self.model.predict([market_conditions])[0]

    def adjust_portfolio(self, portfolio, market_conditions)
        allocation = self.predict_allocation(market_conditions)
        for asset, weight in allocation.items()
            portfolio[asset] = weight
        return portfolio

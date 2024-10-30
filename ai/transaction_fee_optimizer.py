import numpy as np
import random

class TransactionFeeOptimizer:
    def __init__(self):
        self.q_table = np.zeros((10, 3))
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 2)
        return np.argmax(self.q_table[state])

    def update_q_value(self, state, action, reward, next_state):
        current_q = self.q_table[state, action]
        max_future_q = np.max(self.q_table[next_state])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_future_q)
        self.q_table[state, action] = new_q

    def adjust_fee(self, current_load):
        state = min(int(current_load / 10), 9)
        action = self.choose_action(state)
        if action == 0:
            return -1
        elif action == 1:
            return 0
        else:
            return 1

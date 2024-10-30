import random
import time

class StakingSystem:
    def __init__(self):
        self.stakes = {}
        self.stake_times = {}
        self.ranj_reward_pool = 10000

    def stake_arc(self, user, amount, wallet):
        if wallet.get_balance(user) >= amount:
            self.stakes[user] = self.stakes.get(user, 0) + amount
            self.stake_times[user] = time.time()
            wallet.transfer(user, "staking_pool", amount)

    def select_validator(self):
        total_stake = sum(self.stakes.values())
        selection_chance = {user: stake / total_stake for user, stake in self.stakes.items()}
        selected_validator = random.choices(list(selection_chance.keys()), weights=selection_chance.values(), k=1)[0]
        return selected_validator

    def distribute_ranj_reward(self, validator):
        if self.ranj_reward_pool > 0:
            staking_duration = time.time() - self.stake_times[validator]
            reward_multiplier = min(1 + staking_duration / 3600, 5)
            reward = min(100 * reward_multiplier, self.ranj_reward_pool)
            self.ranj_reward_pool -= reward
            return reward
        return 0

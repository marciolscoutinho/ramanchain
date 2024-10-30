class Wallet:
    def __init__(self):
        self.balances = {}

    def create_wallet(self, user, initial_balance=0):
        self.balances[user] = initial_balance

    def get_balance(self, user):
        return self.balances.get(user, 0)

    def transfer(self, sender, receiver, amount):
        if self.balances[sender] >= amount:
            self.balances[sender] -= amount
            self.balances[receiver] = self.balances.get(receiver, 0) + amount
            return True
        return False

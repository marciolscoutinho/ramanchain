import rsa

class Transaction:
    def __init__(self, sender, receiver, amount, fee, wallet, public_key, private_key):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.wallet = wallet
        self.public_key = public_key
        self.private_key = private_key
        self.signature = self.sign_transaction()

    def sign_transaction(self):
        transaction_data = f"{self.sender} envia {self.amount} Arc para {self.receiver} com taxa {self.fee}"
        return rsa.sign(transaction_data.encode('utf-8'), self.private_key, 'SHA-256')

    def validate_signature(self):
        transaction_data = f"{self.sender} sends {self.amount} Arc to {self.receiver} with fee {self.fee}"
        try:
            rsa.verify(transaction_data.encode('utf-8'), self.signature, self.public_key)
            return True
        except rsa.VerificationError:
            return False

    def process_transaction(self, miner_address):
        if not self.validate_signature():
            return False
        
        total_deduction = self.amount + self.fee
        if self.wallet.get_balance(self.sender) >= total_deduction:
            self.wallet.transfer(self.sender, self.receiver, self.amount)
            self.wallet.transfer(self.sender, miner_address, self.fee)
            return True
        return False

import hashlib
import time
from blockchain.consensus import PoMIConsensus

class Block:
    def __init__(self, index, previous_hash, transactions, miner_address, consensus_system):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.miner_address = miner_address
        self.consensus_system = consensus_system
        self.equation = self.consensus_system.generate_ramanujan_equation()
        self.hash = None

    def mine_block(self):
        start_time = time.time()
        miner_solution = self.consensus_system.solve_equation(self.equation)
        if self.consensus_system.validate_block(self.equation, miner_solution):
            end_time = time.time()
            time_taken = end_time - start_time
            self.consensus_system.adjust_complexity(time_taken)
            self.hash = self.calculate_hash()
            return True
        return False

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.transactions}{self.miner_address}"
        return hashlib.sha256(block_string.encode()).hexdigest()

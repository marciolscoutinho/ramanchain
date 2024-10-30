from blockchain.wallet import Wallet
from blockchain.block import Block
from blockchain.transaction import Transaction
from blockchain.staking import StakingSystem
from blockchain.audit import AuditSystem
from blockchain.consensus import PoMIConsensus
from ai.fraud_detection import FraudDetector
from ai.portfolio_manager import PortfolioManager
from ai.stablecoin_manager import StablecoinManager
from blockchain.self_healing_contract import SelfHealingSmartContract
from monitoring.metrics import start_monitoring
import rsa

wallet = Wallet()
wallet.create_wallet("User1", 100)
wallet.create_wallet("User2", 50)
wallet.create_wallet("Miner1", 0)

audit_system = AuditSystem()
staking_system = StakingSystem()
consensus_system = PoMIConsensus()
fraud_detector = FraudDetector()
portfolio_manager = PortfolioManager()
stablecoin_manager = StablecoinManager()

start_monitoring()

def simulate_transaction():
    user1_public_key, user1_private_key = rsa.newkeys(512)
    transaction = Transaction("User1", "User2", 20, 2, wallet, user1_public_key, user1_private_key)

    user_behavior = [20, 2, 0.5]
    if fraud_detector.detect_fraud(user_behavior):
        audit_system.log_transaction(transaction, "Failure - Malicious activity detected")
        print("Transaction blocked due to suspicious behavior!")
    else:
        if transaction.process_transaction("Miner1"):
            audit_system.log_transaction(transaction, "Sucess")
            print("Transaction processed successfully!")
        else:
            audit_system.log_transaction(transaction, "Failure")
            print("Error processing transaction.")

def mine_block_example():
    block = Block(1, "0000abc123", [], "Miner1", consensus_system)
    if block.mine_block():
        print(f"Block mined successfully: {block.hash}")
    else:
        print("Error mining the block.")

simulate_transaction()
mine_block_example()

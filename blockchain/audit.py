import time

class AuditSystem:
    def __init__(self):
        self.audit_log = []

    def log_transaction(self, transaction, result):
        self.audit_log.append({
            'type': 'transaction',
            'transaction': transaction,
            'result': result,
            'timestamp': time.time()
        })

    def log_staking(self, validator, reward, result):
        self.audit_log.append({
            'type': 'staking',
            'validator': validator,
            'reward': reward,
            'result': result,
            'timestamp': time.time()
        })

    def detect_fraud(self):
        for entry in self.audit_log:
            if entry['result'] == "Failure":
                print(f"Fraud alert detected in transaction from {entry['transaction'].sender}")

    def show_audit_log(self):
        for entry in self.audit_log:
            print(f"Timestamp: {time.ctime(entry['timestamp'])}, Details: {entry}")

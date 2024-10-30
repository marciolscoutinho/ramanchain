import random

class SelfHealingSmartContract:
    def __init__(self, rules):
        self.rules = rules
        self.vulnerabilities = []

    def detect_vulnerability(self, condition):
        if random.uniform(0, 1) > 0.7:
            self.vulnerabilities.append(condition)
            return True
        return False

    def apply_patch(self):
        if self.vulnerabilities:
            patch = f"Patch applied for vulnerability: {self.vulnerabilities.pop(0)}"
            print(patch)
        else:
            print("No vulnerabilities detected.")

    def execute(self, parameters):
        if not self.detect_vulnerability(parameters):
            print("Contract executed successfully.")
        else:
            self.apply_patch()
            print("Self-healing contract in action.")

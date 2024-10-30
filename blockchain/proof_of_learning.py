import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class ProofOfLearning:
    def __init__(self):
        self.model = SimpleNN()
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01)
        self.criterion = nn.CrossEntropyLoss()
        self.global_model_state = self.model.state_dict()

    def local_train(self, local_data, local_labels, epochs=5):
        dataset = TensorDataset(torch.tensor(local_data).float(), torch.tensor(local_labels).long())
        loader = DataLoader(dataset, batch_size=32, shuffle=True)
        for epoch in range(epochs):
            for data, labels in loader:
                self.optimizer.zero_grad()
                output = self.model(data)
                loss = self.criterion(output, labels)
                loss.backward()
                self.optimizer.step()

    def update_global_model(self, local_model_state):
        for key in self.global_model_state.keys():
            self.global_model_state[key] += local_model_state[key]
        for key in self.global_model_state.keys():
            self.global_model_state[key] /= 2

    def validate_and_sync_model(self, node_model_state):
        self.update_global_model(node_model_state)
        self.model.load_state_dict(self.global_model_state)

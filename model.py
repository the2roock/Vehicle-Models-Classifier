import torch.nn as nn
import torch.nn.functional as F


class VehiclePriceIdentifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(in_features=12, out_features=16)
        self.fc2 = nn.Linear(in_features=16, out_features=8)
        self.fc3 = nn.Linear(in_features=8, out_features=1)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        out = self.fc3(x)
        return out
    
    @property
    def parameters_count(self) -> int:
        S = sum([p.numel() for p in self.parameters()])
        return S

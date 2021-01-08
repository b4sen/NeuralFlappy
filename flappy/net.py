import torch
import torch.nn as nn

class FlappyNet(nn.Module):

    def __init__(self, hidden=4):
        super(FlappyNet, self).__init__()
        self.input = nn.Linear(4, hidden)
        self.hidden = nn.Linear(hidden, hidden)
        self.out = nn.Linear(hidden, 1)

    def forward(self, x):
        x = self.input(x)
        x = self.hidden(x)
        x = self.out(x)
        return torch.sigmoid(x)

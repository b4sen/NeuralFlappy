import torch
import torch.nn as nn
import torch.nn.functional as F
import random

class FlappyNet(nn.Module):

    def __init__(self, hidden=8):
        super(FlappyNet, self).__init__()
        self.input = nn.Linear(5, hidden)
        self.hidden = nn.Linear(hidden, hidden)
        self.out = nn.Linear(hidden, 1)

    def forward(self, x):
        x = F.relu(self.input(x))
        x = F.relu(self.hidden(x))
        x = self.out(x)
        return torch.sigmoid(x)

    def mutate(self, rate):
        for param in self.parameters():
            for dat in param.data:
                if dat.ndim == 0:
                    if random.random() < rate:
                        dat += torch.randn_like(dat)
                else:
                    for num in dat:
                        if random.random() < rate:
                            num += torch.randn_like(num)

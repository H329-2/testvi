import time
from turtle import forward
import torch 
from torch import nn

class ShuffleNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(3,64)
    
    def forward(self, x):
        return 0
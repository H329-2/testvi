import time
import torch 
from torch import nn

class ShuffleNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.int = 1
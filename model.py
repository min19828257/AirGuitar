import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self,inp=42,out=2):
        super(Net,self).__init__()
        self.relu=nn.ReLU()
        
        self.layer=nn.Sequential(
            nn.Linear(inp,64,bias=True),
            self.relu,
            nn.Linear(64,64,bias=True),
            self.relu,
            nn.Linear(64,32,bias=True),
            self.relu,
            nn.Linear(32,out,bias=True),
            nn.Sigmoid()
        )
    def forward(self,inp):
        return self.layer(inp)

if __name__ == '__main__':
    t=Net()
    r=torch.rand(1,40)
    print(t.forward(r))
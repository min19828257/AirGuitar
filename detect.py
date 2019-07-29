from model import Net

import torch

def hand_detect(model,X):

    predict=model(X)
    ret=predict.argmax(1).item()

    return ret

if __name__ == '__main__':
    model=Net()
    model.load_state_dict(torch.load('model/Net.pth'))

    X=torch.randint(low=0,high=368,size=(1,42)).float()
    
    result=hand_detect(model,X)

    print(result)
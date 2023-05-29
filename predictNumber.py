from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from PIL import Image
import numpy as np
import base64
from io import BytesIO


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


def predict(image):
    # load model
    model = Net()
    model.load_state_dict(torch.load("demo/model/mnist_cnn.pt"))
    model.eval()
    # load test data
    img = Image.open(image).convert('L')
    img = img.resize((28, 28))  # 更改图片大小
    npimg1 = np.array(img)  # 转为numpy矩阵
    flatten_img = npimg1.reshape(1, 1, 28, 28)  # 转为mnist1, 1, 28, 28二维张量

    # 以下意思是把白色背景转为黑色背景，因为训练的都是黑色背景
    new_flatten_img = (255 - flatten_img) / 255.0
    new_flatten_img = new_flatten_img.reshape(1, 1, 28, 28)  # --------  该数据可直接被模型识别

    test_kwargs = {'batch_size': 1}
    test_loader = torch.utils.data.DataLoader(new_flatten_img, **test_kwargs)
    for data in test_loader:
        data = data.to(torch.float32)
        output = model(data)
        pred = output.argmax(dim=1, keepdim=True)
        print(pred)
        print(pred.item())
        return pred.item()

#原文链接：https: // blog.csdn.net / qq_39691492 / article / details / 122088475
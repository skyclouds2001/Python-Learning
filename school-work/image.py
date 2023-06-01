from multiprocessing import freeze_support

import torch
import torchvision
from torchvision import datasets, models, transforms
import os

freeze_support()

data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'validation': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

batch_size = 16
data_dir = './../CNN_synth_testset_divided/'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in
                  ['train', 'validation']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True, num_workers=8) for
               x in ['train', 'validation']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'validation']}

class_names = image_datasets['train'].classes
trainloader = dataloaders['train']
testloader = dataloaders['validation']

import matplotlib.pyplot as plt
import numpy as np


def my_imgs_plot(image, labels, preds=None):
    cnt = 0
    plt.figure(figsize=(16, 16))
    for j in range(len(image)):
        cnt += 1
        plt.subplot(1, len(image), cnt)
        plt.xticks([], [])
        plt.yticks([], [])
        if preds is not None:
            plt.title(f"pred: {class_names[preds[j]]}\n true: {class_names[labels[j]]}"
                      , color='green' if preds[j] == labels[j] else 'red')
        else:
            plt.title("{}".format(class_names[labels[j]]), fontsize=15, color='green')
        inp = image[j].numpy().transpose((1, 2, 0))
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        inp = std * inp + mean
        inp = np.clip(inp, 0, 1)
        plt.imshow(inp)
    plt.show()


for _ in range(1):
    freeze_support()
    dataiter = iter(trainloader)
    freeze_support()
    images, labels = dataiter.next()
    my_imgs_plot(images, labels)

import torch.nn as nn
import torch.nn.functional as F


## my
class myNet(nn.Module):
    def __init__(self, in_size=224, in_channels=3, num_classes=2):
        super(myNet, self).__init__()  # RGB 3*32*32
        self.conv1 = nn.Conv2d(in_channels, 15, 3)  # 输入3通道，输出15通道，卷积核为3*3
        self.conv2 = nn.Conv2d(15, 75, 4)  # 输入15通道，输出75通道，卷积核为4*4
        self.conv3 = nn.Conv2d(75, 150, 3)  # 输入75通道，输出150通道，卷积核为3*3
        self.conv4 = nn.Conv2d(150, 300, 3)  # 输入75通道，输出300通道，卷积核为3*3
        self.conv5 = nn.Conv2d(300, 300, 3)  # 输入300通道，输出300通道，卷积核为3*3
        self.fc1 = nn.Linear(7500, 400)  # 输入10800，输出400
        self.fc2 = nn.Linear(400, 120)  # 输入400，输出120
        self.fc3 = nn.Linear(120, num_classes)  # 输入120，输出2

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)  # 3*224*224  -> 150*222*222 -> 15*111*111
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # 15*111*111 -> 75*108*108  -> 75*54*54
        x = F.max_pool2d(F.relu(self.conv3(x)), 2)  # 75*54*54  -> 150*52*52  -> 150*26*26
        x = F.max_pool2d(F.relu(self.conv4(x)), 2)  # 150*26*26   -> 300*24*24  -> 300*12*12
        x = F.max_pool2d(F.relu(self.conv5(x)), 2)  # 300*12*12  -> 300*10*10  -> 300*5*5
        x = x.view(x.size()[0], -1)  # 将300*5*5的tensor打平成1维，7500
        x = F.relu(self.fc1(x))  # 全连接层 10800 -> 400
        x = F.relu(self.fc2(x))  # 全连接层 400 -> 120
        x = self.fc3(x)  # 全连接层 84  -> 10
        return x


# 自动选择 GPU 或 CPU
use_cuda = True
print("CUDA Available: ", torch.cuda.is_available())
device = torch.device("cuda" if (use_cuda and torch.cuda.is_available()) else "cpu")

net = VGG11(3, num_classes=2).to(device)
# net = VGGbase().to(device)
net = myNet().to(device)

import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

from tqdm import tqdm

loss_plot = []
net.train()

l = tqdm(range(192))
for epoch in l:  # 在数据集上循环多次
    # gc.collect()
    # torch.cuda.empty_cache()

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # 获取输入；数据是[输入、标签]的列表
        inputs, labels = data[0].to(device), data[1].to(device)

        # 将参数梯度归零
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # 打印统计数据
        running_loss += loss.item()
        if i % 100 == 99:  # print every 100 mini-batches
            loss_plot.append(running_loss / 100)
            running_loss = 0.0
    # print(f'epoch {epoch + 1} loss: {loss_plot[-1]}')
    l.set_description(f'current loss: {loss_plot[-1]}')
print('Finished Training')

plt.plot(loss_plot)

PATH = './fakeFace_{}.pth'.format(net.__class__.__name__)
torch.save(net.state_dict(), PATH)

dataiter = iter(testloader)
images, labels = dataiter.next()
my_imgs_plot(images, labels)

# net = VGG11(3,num_classes=2).to(device)
# net.load_state_dict(torch.load(PATH))
net.to('cpu')
outputs = net(images)

# 输出是2个类的 energy 。一个类的 energy 越高，网络就越多认为图像是特定类别的。
# 那么，让我们得到最高 energy 的指数：
_, predicted = torch.max(outputs, 1)

my_imgs_plot(images, labels,predicted)

# prepare to count predictions for each class
correct_pred = {classname: 0 for classname in class_names}
total_pred = {classname: 0 for classname in class_names}

# 同样，不需要梯度
with torch.no_grad():
    for data in tqdm(testloader):
        images, labels = data
        outputs = net(images)
        _, predictions = torch.max(outputs, 1)
        # collect the correct predictions for each class
        for label, prediction in zip(labels, predictions):
            if label == prediction:
                correct_pred[class_names[label]] += 1
            total_pred[class_names[label]] += 1


# 打印每一个类的准确性
for classname, correct_count in correct_pred.items():
    accuracy = 100 * float(correct_count) / total_pred[classname]
    print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')



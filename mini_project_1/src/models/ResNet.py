"""
Description: Pytorch implementation of a residual network (adapted from Practical 6)
"""

import torch.nn as nn
from torch.nn import functional as F


######################################################################

class ResNet(nn.Module):

    def __init__(self, d=0, only_image=False, nb_residual_blocks=5, nb_channels=20,
                 kernel_size=3, skip_connections=True, batch_normalization=True):
        super(ResNet, self).__init__()

        input_shape = 1 if only_image else 2
        output_shape = 10 if only_image else 2

        self.conv = nn.Conv2d(input_shape, nb_channels,
                              kernel_size=kernel_size,
                              padding=(kernel_size - 1) // 2)
        self.bn = nn.BatchNorm2d(nb_channels)

        self.resnet_blocks = nn.Sequential(
            *(ResNetBlock(nb_channels, kernel_size, d, skip_connections, batch_normalization)
              for _ in range(nb_residual_blocks))
        )

        self.fc = nn.Linear(nb_channels, output_shape)

    def forward(self, x):
        x = F.relu(self.bn(self.conv(x)))
        x = self.resnet_blocks(x)
        x = F.avg_pool2d(x, 8).view(x.size(0), -1)
        x = self.fc(x)
        return x


######################################################################

class ResNetBlock(nn.Module):
    def __init__(self, nb_channels, kernel_size, d,
                 skip_connections=True, batch_normalization=True):
        super(ResNetBlock, self).__init__()

        self.conv1 = nn.Conv2d(nb_channels, nb_channels,
                               kernel_size=kernel_size,
                               padding=(kernel_size - 1) // 2)

        self.bn1 = nn.BatchNorm2d(nb_channels)

        self.conv2 = nn.Conv2d(nb_channels, nb_channels,
                               kernel_size=kernel_size,
                               padding=(kernel_size - 1) // 2)

        self.bn2 = nn.BatchNorm2d(nb_channels)

        self.skip_connections = skip_connections
        self.batch_normalization = batch_normalization
        self.dropout = nn.Dropout(d)

    def forward(self, x):
        y = self.conv1(x)
        if self.batch_normalization:
            y = self.bn1(y)
        y = F.relu(y)
        y = self.conv2(y)
        if self.batch_normalization:
            y = self.bn2(y)
        if self.skip_connections:
            y = y + x
        y = F.relu(y)

        return y


def res_net(dropout=0, only_image=False):
    model = ResNet(d=dropout, only_image=only_image)
    return model





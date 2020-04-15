"""
File: mse.py
Description: MSE loss function implementation
"""
from .module import Module


class MSE(Module):

    def __init__(self):
        super(MSE, self).__init__()
        self.__loss_value = None

    def __loss(self, input, target):
        return (input - target).pow(2).sum()

    def __dloss(self, input, target):
        return 2 * (input - target)

    def backward(self, model):
        grad = self.__dloss(self.param().get('input'), self.param().get('target'))
        grads = model.backward(grad)
        model.add_parameter('grads', grads)
        model.add_parameter('layers', model.f.layers)
        return grad

    def forward(self, input, target):
        self.add_parameter('input', input)
        self.add_parameter('target', target)
        self.__loss_value = self.__loss(input, target)
        return self

    def item(self):
        return self.__loss_value.item()
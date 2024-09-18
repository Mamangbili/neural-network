
from abc import ABC
from numbers import Real
from typing import TypedDict, override

from numpy import array, exp, maximum, ndarray
import numpy as np


class Activation(ABC):
    @override
    def calculate(self):
        pass

class ReLU(Activation):
    def calculate(self, layer : ndarray):
        return maximum(0,layer)

class Sigmoid(Activation):
    def calculate(self, x : ndarray):
        return 1/1 + exp(x)

class Layer(TypedDict):
    layer : ndarray
    activation : Activation
    bias : ndarray

class NeuralNetwork:
    def __init__ (self):
        self.__activation_function : Activation = ReLU()
        self.__input : array = None
        self.__layer : list[Layer] = []
    
    def set_activation(self, activation_function : Activation) -> None :
        self.__activation_function = activation_function
    
    def input(self, input) :
        pass
    
    def train(self) :
        pass
    
    def forward_pass(self):
        pass
    
    def backward_pass(self):
        pass
    
    def add_layer(self, layer : ndarray) -> None :
        self.__layer.append(layer)
        
    
        
    

test = np.random.random_sample(10) - 0.5 
print( np.maximum(0,test) )
print( test )

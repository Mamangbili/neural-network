from typing import Tuple
import PIL.Image
import numpy as np

class Converter:
    def __init__(self,flatten_pixel : np.ndarray):
        self.__flatten_pixel = np.array( flatten_pixel )
    
    def convert(self, size : Tuple):
        gray_scale_array = self.__flatten_pixel.reshape(size)
        image = PIL.Image.fromarray(np.uint8(gray_scale_array),'L')
        return image
        


import os
import pathlib
from typing import List
import PIL
import PIL.Image
import numpy as np


class Loader:
    def __init__(self,dir_path : str): 
        self.__images_path  = dir_path
    
    def lazy_load(self) -> np.array:
        img_names : List[str] = os.listdir(self.__images_path)
        for i,name in enumerate(img_names,0):
            image = PIL.Image.open(self.__images_path / name)
            yield i,np.array(image, dtype="uint8")






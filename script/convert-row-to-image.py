import time
import PIL.Image
import numpy as np
import pandas as pd

from CSVLoader.Loader import Loader
import constant
from grayscale_converter.Converter import Converter

loader = Loader(constant.train_path)

start = time.time()
for i,row in loader.lazy_load():
    converter = Converter(row[1:])
    img = converter.convert((28,28))
    img.save(f"./img/angka-{i}.png")
    if i == 1000 : break
    
print(f'Elapsed :: {time.time() - start}')
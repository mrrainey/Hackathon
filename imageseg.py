import os
import pandas as pd
import numpy as np
from PIL import Image
from mrcnn import utils
from keras_preprocessing.image import img_to_array

class ImageLoader(utils.Dataset):

    def load_image(self, filename, dir='image'):
        """Load in an image of the given filename
        """
        if dir == 'train':
            img = Image.open(f"train/{dir}/{filename}")
        elif dir == 'test':
            img = Image.open(f"test/{dir}/{filename}")
        else:
            raise Exception('Image was not found')
        
        return img_to_array(img)

    def load_mask(self, filename):
        """Load masks of the given filename.
        """
        return self.load_image(filename, dir='mask')

img_loader = ImageLoader()
image = img_loader.load_image('1.png')

mask = img_loader.load_mask('1.png')
print(mask)
import os
import pandas as pd
import numpy as np
from PIL import Image
from mrcnn import utils


class ImageLoader(utils.Dataset):

    def load_image_init(self, data_url):
        self.add_class("lesion", 1, "lesion")

        for image in data_url['image']:
            self.add_image(
                "lesion",
                image_id=image,
                path=os.path.join(os.getcwd(), "image/{}.png".format(image)))

    # def load_image(self, filename):
    #     """Load in an image of the given filename
    #     """
    #     if dir == 'train':
    #         img = Image.open(f"train/{filename}")
    #     elif dir == 'test':
    #         img = Image.open(f"test/{filename}")
    #     else:
    #         raise Exception('Image was not found')
    #     return img
    #
    # def load_mask(self, filename):
    #     """Load masks of the given filename.
    #     """
    #     return self.load_image(filename)

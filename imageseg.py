import os
from mrcnn import utils


class ImageLoader(utils.Dataset):

    def load_image_init(self, data_url):
        self.add_class("lesion", 1, "lesion")

        for image in data_url['image']:
            self.add_image(
                "lesion",
                image_id=image,
                path=os.path.join(os.getcwd(), "image/{}.png".format(image)))


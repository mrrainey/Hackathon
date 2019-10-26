import os
import pandas
from imageseg import ImageLoader
from mrcnn.config import Config
import mrcnn.model as modellib

model_save = os.getcwd() + "/save"


class LesionsConfig(Config):
    NAME = "lesions"

    NUM_CLASSES = 2

    IMAGE_MIN_DIM = 64
    IMAGE_MAX_DIM = 64

    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)

    TRAIN_ROIS_PER_IMAGE = 32

    STEPS_PER_EPOCH = 100

    VALIDATION_STEPS = 5


config = LesionsConfig()

# set up training data

data = pandas.read_csv('train_data_64/index.csv')

data = data.sample(frac=1, random_state=42)
train_data = data.loc[data['subset'] == 'T']
test_data = data.loc[data['subset'] == 'V']

del data

# Create model in training mode
model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=model_save)


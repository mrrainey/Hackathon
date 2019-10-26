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

    LEARNING_RATE = 0.002


config = LesionsConfig()

# set up training data

data = pandas.read_csv('train/updated_csv.csv')

data = data.sample(frac=1, random_state=42)
train_data = data.loc[data['subset'] == 'T']
val_data = data.loc[data['subset'] == 'V']

del data
train_data.drop(columns="subset")
val_data.drop(columns="subset")

dataset_train = ImageLoader()
dataset_train.load_image_init(train_data)
dataset_train.prepare()

dataset_val = ImageLoader()
dataset_val.load_image_init(val_data)
dataset_val.prepare()

# Create model in training mode
model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=model_save)
model.load_weights(model.get_imagenet_weights(), by_name=True)

model.train(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE,
            epochs=1,
            layers='all')

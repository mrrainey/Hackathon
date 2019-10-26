import os
import pandas
import skimage.

model_save = os.getcwd() + "/save"

# set up training data

data = pandas.read_csv('train/updated_csv.csv')

data = data.sample(frac=1, random_state=42)
train_data = data.loc[data['subset'] == 'T']
val_data = data.loc[data['subset'] == 'V']

del data
train_data.drop(columns="subset")
val_data.drop(columns="subset")

def image_loader(image_id):


import tensorflow as tf
import skimage
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
                   if os.path.isdir(os.path.join(data_directory, d))]
    images = []
    labels = []

    for directory in directories:
        label_directory = os.path.join(data_directory, directory)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels


CURRENT_WORKING_DIRECTORY = "/Desktop/nxsyed/Code/Github/tensorflow-TrafficSigns/"
train_data_directory = os.path.join(CURRENT_WORKING_DIRECTORY, "TrafficSigns/Training")
test_data_directory = os.path.join(CURRENT_WORKING_DIRECTORY, "TrafficSigns/Testing")


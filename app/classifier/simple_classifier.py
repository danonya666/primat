from tensorflow import keras
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras.datasets import fashion_mnist

from app import settings

from app import settings

class SimpleClassifier:
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        try:
            self.model.load_weights('weight.h5')
        except OSError:
            raise FileNotFoundError("no weight.h5 file")

        self.model.compile(optimizer=keras.optimizers.Adam(lr=0.001, decay=1e-6),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def predict(self, img):
        prediction = self.model.predict(img)[0]
        class_names = settings.CLASS_NAMES
        result = {}
        # mapping predictions with classnames
        for i in range(len(prediction)):
            result[class_names[i]] = prediction[i]

        return result



simple_classifier = SimpleClassifier()
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

test_images = test_images / 255.0

img = (np.expand_dims(test_images[1], 0))

print(simple_classifier.predict(img))

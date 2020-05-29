from typing import Dict

import numpy as np
import tensorflow as tf
from tensorflow import keras

from app import settings


class SimpleClassifier:
    def __init__(self) -> None:
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        try:
            self.model.load_weights('weight.h5')
        except OSError:
            raise FileNotFoundError("no weight.h5 file")

        self.model.compile(
            optimizer=keras.optimizers.Adam(lr=0.001, decay=1e-6),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'],
        )

    def predict(self, image: np.ndarray) -> Dict[str, int]:
        prediction = self.model.predict(image)[0]
        class_names = settings.CLASS_NAMES
        return {class_names[i]: prediction[i] for i in range(len(prediction))}

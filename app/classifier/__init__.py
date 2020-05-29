from typing import Dict

import numpy as np

from .main import SimpleClassifier

simple_classifier = SimpleClassifier()


def predict_class(image: np.ndarray) -> Dict[str, float]:
    """
    Predicts class of an object on the image
    :param image: binary image file stored in the RAM
    :return: mappings of {settings.CLASS_NAME: probability}
    """
    return simple_classifier.predict(image)

<<<<<<< HEAD
from typing import Dict

from simple_classifier import SimpleClassifier
from ..settings.dist import CLASS_NAMES

simple_classifier = SimpleClassifier()


def predict(image: bytes) -> Dict[str, float]:
    """
    Predicts class of an object on the image
    :param image: binary image file stored in the RAM
    :return: mappings of {settings.CLASS_NAME: probability}
    """
    predictions = simple_classifier.predict()
    print(predictions)
    result = {}


=======
from .main import predict_class
>>>>>>> d90a4cdfd4694bcce80269865adf2e471ebf0021

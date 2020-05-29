from typing import Dict

from app.classifier.simple_classifier import SimpleClassifier

simple_classifier = SimpleClassifier()


def predict(image: bytes) -> Dict[str, float]:
    """
    Predicts class of an object on the image
    :param image: binary image file stored in the RAM
    :return: mappings of {settings.CLASS_NAME: probability}
    """
    return simple_classifier.predict()


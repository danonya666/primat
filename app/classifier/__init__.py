from typing import Dict

from app import settings


def predict(image: bytes) -> Dict[str, float]:
    """
    Predicts class of an object on the image
    :param image: binary image file stored in the RAM
    :return: mappings of {settings.CLASS_NAME: probability}
    """
    raise NotImplementedError

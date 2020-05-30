import numpy as np
from PIL import Image

from app import settings


def convert_image(picture_path: str = settings.DEFAULT_IMAGE_PATH) -> np.ndarray:
    img = Image.open(picture_path).resize((28, 28), Image.ANTIALIAS).convert('L')
    data = np.asarray(img, dtype="float")
    if settings.STAGE == 'dev':
        img.save('grey.png')
    img.close()
    data = (np.expand_dims(data, 0))
    for pixel in data:
        pixel /= 255.0
    return data

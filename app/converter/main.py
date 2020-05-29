import numpy as np
from PIL import Image

from app import settings


def convert_image(picture_url: str) -> np.ndarray:
    img = Image.open(picture_url).resize((28, 28), Image.ANTIALIAS).convert('L')
    data = np.asarray(img, dtype="float")
    if settings.STAGE == 'dev':
        img.save('grey.png')
    img.close()
    for pixel in data:
        pixel /= 255.0
    return data

import numpy as np

from app import settings


def save_picture(picture: bytes, filename: str = 'last_picture.png') -> None:
    with open(filename, 'wb') as file:
        file.write(picture)


def convert_image(picture_url: str) -> np.ndarray:
    raise NotImplementedError
    if settings.STAGE == 'dev':
        save_image(image)

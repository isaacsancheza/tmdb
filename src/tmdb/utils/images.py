from io import BytesIO
from typing import cast

from PIL import Image
from requests import get


class Images:
    def __init__(self, /, *, image_size: str = 'original') -> None:
        self._endpoint = f'https://image.tmdb.org/t/p/{image_size}'

    def get_image(self, url: str, /) -> tuple[str, bytes]:
        response = get(self._endpoint + url)
        if not response.ok:
            response.raise_for_status()

        data = response.content
        image: Image.Image = Image.open(BytesIO(data))
        
        image_format = cast(str, image.format).lower()
        image.close()
        
        return image_format, data   

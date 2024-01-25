from tmdb.utils.images import Images


class Utils:
    def __init__(self, /) -> None:
        self._images = None
    
    @property
    def images(self, /) -> Images:
        if self._images is None:
            self._images = Images()
        return self._images

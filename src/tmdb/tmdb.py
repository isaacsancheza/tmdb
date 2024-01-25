from tmdb.utils import Utils
from tmdb.movies import Movies
from tmdb.series import Series


class TMDB:
    def __init__(self, api_key: str, /, *, api_version: int = 3) -> None:
        self._utils = None
        self._movies = None
        self._series = None
        self._api_key = api_key
        self._api_version = api_version

    @property
    def utils(self) -> Utils:
        if self._utils is None:
            self._utils = Utils()
        return self._utils

    @property
    def movies(self) -> Movies:
        if self._movies is None:
            self._movies = Movies(self._api_key, self._api_version)
        return self._movies

    @property
    def series(self) -> Series:
        if self._series is None:
            self._series = Series(self._api_key, self._api_version)
        return self._series 

from typing import Any
from datetime import date

from tmdb.base import Base


class Movies(Base):    
    def get_videos(self, movie_id: int, /) -> list[dict[str, Any]]:
        params = {
            'language': 'es-MX',
        }
        response = self._request('movie', movie_id, 'videos', params=params)
        return response['results']

    def get_details(self, movie_id:  int, /) -> dict[str, Any]:
        params = {
            'language': 'es-MX',
        }
        response = self._request('movie', movie_id, params=params)
        return response

    def get_backdrops(self, movie_id: int, /) -> list[dict[str, Any]]:
        params = {
            'language': 'es-MX',
        }
        response = self._request('movie', movie_id, 'images', params=params)
        return response['backdrops']

    def get_release_dates(self, movie_id: int, /) -> list[dict[str, Any]]:
        params = {
            'language': 'es-MX',
        }
        response = self._request('movie', movie_id, 'release_dates', params=params)
        return response['results']

    def get_alternative_titles(self, movie_id: int, /) -> list[dict[str, Any]]:
        params = {
            'language': 'es-MX',
        }
        response = self._request('movie', movie_id, 'alternative_titles', params=params)
        return response['titles']

    def get_upcoming_movies(self, since_dt: date, until_dt: date, /) -> list[dict[str, Any]]:
        fmt = '%Y-%m-%d'
        since = since_dt.strftime(fmt)
        until = until_dt.strftime(fmt)
        return self._get_upcoming_movies(since, until)

    def _get_upcoming_movies(self, since: str, until: str, /, *, page: int = 1) -> list[dict[str, Any]]:                    
        params = {
            'page': page,
            'region': 'MX',
            'language': 'es',
            'include_video': False,
            'include_adult': False,
            'release_date.gte': since,
            'release_date.lte': until,
            'with_release_type': 3,  # theatrical release
        }
        response = self._request('discover', 'movie', params=params)
        
        results = response['results']
        total_pages = response['total_pages']

        if page < total_pages:
            results += self._get_upcoming_movies(since, until, page=page + 1)
        
        return results

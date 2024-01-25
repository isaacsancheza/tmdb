from typing import Any
from datetime import date

from tmdb.base import Base
from tmdb.series.seasons import Seasons


class Series(Base):    
    def __init__(self, api_key: str, api_version: int, /) -> None:
        super().__init__(api_key, api_version)
        self._seasons = None
    
    @property
    def seasons(self) -> Seasons:
        if self._seasons is None:
            self._seasons = Seasons(self._api_key, self._api_version)
        return self._seasons

    def get_videos(self, serie_id: int, /) -> list[dict[str, Any]]:
        """
        https://developer.themoviedb.org/reference/tv-series-videos
        """
        params = {
            'language': 'es-MX',
        }
        response = self._request('tv', serie_id, 'videos', params=params)
        return response['results']

    def get_details(self, serie_id:  int, /) -> dict[str, Any]:
        """
        https://developer.themoviedb.org/reference/tv-series-details
        """
        params = {
            'language': 'es-MX',
        }
        response = self._request('tv', serie_id, params=params)
        return response

    def get_backdrops(self, serie_id: int, /) -> list[dict[str, Any]]:
        """
        https://developer.themoviedb.org/reference/tv-series-images
        """
        params = {
            'language': 'es-MX',
        }
        response = self._request('tv', serie_id, 'images', params=params)
        return response['backdrops']

    def get_alternative_titles(self, serie_id: int, /) -> list[dict[str, Any]]:
        """
        https://developer.themoviedb.org/reference/tv-series-alternative-titles
        """
        response = self._request('tv', serie_id, 'alternative_titles')
        return response['results']

    def get_upcoming_series(self, since_dt: date, until_dt: date, /) -> list[dict[str, Any]]:
        fmt = '%Y-%m-%d'
        since = since_dt.strftime(fmt)
        until = until_dt.strftime(fmt)
        return self._get_upcoming_series(since, until)

    def _get_upcoming_series(self, since: str, until: str, /, *, page: int = 1) -> list[dict[str, Any]]: 
        """
        https://developer.themoviedb.org/reference/discover-tv
        """
        params = {
            'page': page,
            'language': 'es-MX',
            'watch_region': 'MX',
            'include_adult': False,
            'air_date.gte': since,
            'air_date.lte': until,
        }

        tv_providers = self._tv_providers()
        params['with_watch_providers'] = '|'.join([str(tv_p['provider_id']) for tv_p in tv_providers])

        response = self._request('discover', 'tv', params=params)
        
        results = response['results']
        total_pages = response['total_pages']

        if page < total_pages:
            results += self._get_upcoming_series(since, until, page=page + 1)
        
        return results

    def _tv_providers(self) -> list[dict[str, Any]]:
        """
        https://developer.themoviedb.org/reference/watch-provider-tv-list
        """
        response = self._request('watch', 'providers', 'tv', params={'language': 'es-MX', 'watch_region': 'MX'})
        return response['results']

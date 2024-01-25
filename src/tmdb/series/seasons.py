from typing import Any

from tmdb.base import Base


class Seasons(Base):    
    def get_details(self, serie_id:  int, season_number: int, /) -> dict[str, Any]:
        """
        https://developer.themoviedb.org/reference/tv-season-details
        """
        params = {
            'language': 'es-MX',
        }
        response = self._request('tv', serie_id, 'season', season_number, params=params)
        return response

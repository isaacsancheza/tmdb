from typing import Any

from requests import get


class Base:
    def __init__(self, api_key: str, api_version: int, /) -> None:
        self._api_key = api_key
        self._api_version = api_version
        self._endpoint = f'https://api.themoviedb.org/{api_version}'

    def _request(self, *args: str | int, params: dict[str, Any] = {}, headers: dict[str, str] = {}) -> dict[str, Any]:
        headers['Authorization'] = f'Bearer {self._api_key}'
        
        endpoint = '/'.join([self._endpoint] + [str(arg) for arg in args])
        response = get(endpoint, params=params, headers=headers)

        if not response.ok:
            response.raise_for_status()
        
        return response.json()

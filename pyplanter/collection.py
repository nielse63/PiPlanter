import requests
import urllib

from pyplanter.constants import DB_API_URL


class Collection:
    def __init__(self, name):
        self.name = name
        self.api = DB_API_URL + name

    def getById(self, id: str) -> dict:
        url = self.api + "/" + id
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def create(self, data: dict) -> dict:
        response = requests.post(self.api, data=data)
        response.raise_for_status()
        return response.json()

    def update(self, id: str, data: dict) -> dict:
        url = self.api + "/" + id
        response = requests.patch(url, data=data)
        response.raise_for_status()
        return response.json()

    def delete(self, id: str) -> None:
        url = self.api + "/" + id
        response = requests.delete(url)
        response.raise_for_status()

    def search(self, query: dict) -> list:
        query_string = urllib.parse.urlencode(query, doseq=False)
        url = self.api + "?" + query_string
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def list(self) -> list:
        response = requests.get(self.api)
        response.raise_for_status()
        return response.json()

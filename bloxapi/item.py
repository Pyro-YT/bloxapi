import json
import asyncio
import requests


class Item:

    def __init__(self, name: str, id: int):

        self.name = name
        self.id = id
        
    async def get_item(self):
        response = requests.get(url=f'https://catalog.roblox.com/v1/search/items/details?id={self.id}')
        json = response.json()["data"][0]
        return json["price"]     

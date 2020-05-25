import json
import asyncio
import requests


class Item:

    def __init__(self, name: str, id: int):

        self.name = name
        self.id = id

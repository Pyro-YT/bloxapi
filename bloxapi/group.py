import requests
import asyncio
from .utils.errors import *
import json


class Group:

    def __init__(self, name, Id, description):
        self.name = name
        self.Id = Id
        self.description = description


    async def get_group_roles(self):
        data = requests.get(url=f'https://groups.roblox.com/v1/groups/{self.Id}/roles').json()
        for i in data:

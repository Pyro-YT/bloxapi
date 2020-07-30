import requests
import asyncio
from .utils.errors import *
import json


class Group:

    def __init__(self, name, Id, description):
        self.name = name
        self.Id = Id
        self.description = description

import requests
import asyncio
from .utils.errors import *
import json


class User:

    def __init__(self, name, Id, status, about):
        self.name = name
        self.Id = Id
        self.status = status
        self.about = about

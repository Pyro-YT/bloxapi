import requests
import asyncio
from .utils.errors import *
import json


class Client:

    def __init__(self, Cookie=None):
        self.Cookie = Cookie
        self.cookies = {'.ROBLOSECURITY': f'{self.Cookie}'}
        self.AuthenticateCookie()

    def AuthenticateCookie(self):
        request = requests.get(url='https://www.roblox.com/my/profile', cookies=self.cookies)
        try:
            request.json()
        except json.decoder.JSONDecodeError:
            raise FailedAuthentication('Invalid cookie was given.')

    async def get_self(self):
        if not self.Cookie:
            raise NotAutenticated('You must be authenticated to execute this action.')
        
        data = requests.get(url='https://www.roblox.com/my/profile', cookies=self.cookies).json()
        print(data)



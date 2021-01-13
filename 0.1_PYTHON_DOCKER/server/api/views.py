# aiohttpdemo_polls/views.py
from aiohttp import web
import os
import requests


class Handler:

    async def index(self, request):
        home = os.environ['HOME']
        return web.Response(text="Hello, World Server! " + home)

    async def connect_gateway(self, request):
        try:
            res = requests.get('http://gateway:7000/message', timeout=3)
        except requests.exceptions.ConnectionError:
            res = "Can't connect to server."
        except requests.exceptions.Timeout:
            res = "Time for connection expired."
        finally:
            return web.json_response({
                'status': True,
                'message': 'Welcome to the Dockerized Flask Server!',
                'text': res.text
            })

    async def get_message(self, request):
        return web.json_response({
            'status': True,
            'message': 'Welcome to the Dockerized Flask Server!'
        })

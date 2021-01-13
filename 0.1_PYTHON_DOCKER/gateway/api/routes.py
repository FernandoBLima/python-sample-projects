from views import Handler
from aiohttp import web


def set_routes(app):
    """ Set routes, mechanism of mapping the URL directly to the code"""
    handler = Handler()

    app.router.add_route('GET', '/', handler.index)
    app.router.add_get('/message', handler.get_message)
    app.router.add_get('/connect', handler.connect_to_server)

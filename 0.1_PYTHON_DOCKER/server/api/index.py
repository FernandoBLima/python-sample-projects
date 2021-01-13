from aiohttp import web
from routes import set_routes
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    set_routes(app)
    web.run_app(app, port=8000, access_log_format=" :: %r %s %T %t")

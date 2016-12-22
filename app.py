# -*- coding: utf-8 -*-
import aiohttp_debugtoolbar
from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


if __name__ == '__main__':
    app = web.Application()
    aiohttp_debugtoolbar.setup(app)
    app.router.add_get('/', hello)
    web.run_app(app)

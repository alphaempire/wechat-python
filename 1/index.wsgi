# -*- coding: utf-8 -*-
import os

import sae
import web

urls = (
    '/', 'Hello',
)


class Hello:
    def GET(self):
        data = web.input()
        echostr = data.echostr
        return echostr

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)

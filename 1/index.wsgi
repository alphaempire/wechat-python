# -*- coding: utf-8 -*-
import os

import sae
import web
import hashlib

urls = (
    '/', 'Hello',
)


class Hello:
    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "das_crowd"
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1,update, list)
        hashcode = sha1.hexdigest()
        
        if hashcode = sha1.hexdigest()
            return echostr

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)

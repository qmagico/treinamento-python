#!/usr/bin/env python

from bottle import route, run


@route('/')
def index():
    return 'Hello world'

run(host='localhost', port=8080, debug=True)

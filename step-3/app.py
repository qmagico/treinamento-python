#!/usr/bin/env python

from bottle import route, run


@route('/')
@route('/<name>')
def index(name='Esquecidinho'):
    return 'Hello world, ' + name

run(host='localhost', port=8080, debug=True)

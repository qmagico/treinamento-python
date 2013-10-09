#!/usr/bin/env python

from time import strftime

from bottle import route, run


@route('/')
@route('/<name>')
def index(name='Esquecidinho'):
    return 'Hello world, ' + name + '. Sao ' + strftime('%H:%M:%S')

run(host='localhost', port=8080, debug=True)

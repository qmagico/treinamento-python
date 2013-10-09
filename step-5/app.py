#!/usr/bin/env python

from time import strftime

from bottle import route, run


def fat(number):
    if number in [0, 1]:
        return 1
    return number * fat(number - 1)


@route('/')
@route('/<name>')
def index(name='Esquecidinho'):
    return 'Hello world, ' + name + '. Sao ' + strftime('%H:%M:%S')


@route('/fatorial/<number>')
def fatorial(number):
    return 'Fatorial de ' + number + ' eh ' + str(fat(int(number)))

run(host='localhost', port=8080, debug=True)

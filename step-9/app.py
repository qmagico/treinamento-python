#!/usr/bin/env python
# coding: utf-8

from time import strftime

from bottle import route, run


def fat(number):
    if number in [0, 1]:
        return 1
    return number * fat(number - 1)


@route('/')
@route('/<name>')
def index(name='Esquecidinho'):
    return 'Hello world, %s. São %s.' % (name, strftime('%H:%M:%S'))


@route('/fatorial/<number>')
def fatorial(number):
    return 'Fatorial de %s é %s' % (number, str(fat(int(number))))


@route('/lista/<number>')
def lista(number):
    try:
        int(number)
    except:
        return 'Ops! Isso não é um número válido!'

    return ', '.join([str(i) for i in range(int(number))])


run(host='localhost', port=8080, debug=True)

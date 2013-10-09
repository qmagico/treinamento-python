#!/usr/bin/env python
# coding: utf-8

from time import strftime

from bottle import route, run


def fat(number):
    if number in [0, 1]:
        return 1
    return number * fat(number - 1)


class MyNumber(object):
    def __init__(self, number):
        self.number = number
        self.fatorial = fat(number)


@route('/')
@route('/<name>')
def index(name='Esquecidinho'):
    return 'Hello world, %s. São %s.' % (name, strftime('%H:%M:%S'))


@route('/fatorial/<number>')
def fatorial(number):
    try:
        int(number)
    except:
        return 'Ops! Isso não é um número válido!'

    my_number = MyNumber(int(number))

    return 'Fatorial de %d é %d' % (my_number.number, my_number.fatorial)


@route('/lista/<number>')
def lista(number):
    try:
        int(number)
    except:
        return 'Ops! Isso não é um número válido!'

    return ', '.join([str(i) for i in range(int(number))])


run(host='localhost', port=8080, debug=True)

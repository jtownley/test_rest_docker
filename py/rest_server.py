from bottle import route, run, template, abort, response
import os

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def root():
    return '<b>Welcome to the http test server</b>!'

@route('/200')
def twohundred():
    return 'you got a 200'

@route('/200/json')
def twohundred():
    return {'status': "OK"}

@route('/201')
def twohundred():
    response.status = 201
    return {'status': "CREATED" }

@route('/201/json')
def twohundred():
    response.status = 201
    return 'you created a 201'

@route('/404')
def fourOfour():
    abort(404, "Requested 404 found")

@route('/500')
def fivehundred():
    raise Exception("A server problem happened")

port = 8080
if 'PORT' in os.environ:
    port = os.environ['PORT']

run(host='0.0.0.0', port=port)
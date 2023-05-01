# Put your app in here.
from flask import Flask, request
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def add_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def sub_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def mult_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def div_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

math_dict = {
    'add' : add,
    'sub' : sub,
    'mult' : mult,
    'div' : div
}

@app.route('/math/<operation>')
def math_operation(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(math_dict[operation](a,b))

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/') # base route
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>') # route for printing a string
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>') # route for counting
def count(parameter):
    return '\n'.join([str(i) for i in range(int(parameter))] + [''])

@app.route('/math/<num1>/<operation>/<num2>') # route for math
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    if operation == '-':
        return str(int(num1) - int(num2))
    if operation == '*':
        return str(int(num1) * int(num2))
    if operation == 'div':
        return str(int(num1) / int(num2))
    if operation == '%':
        return str(int(num1) % int(num2))
    
print(app.url_map)
if __name__ == '__main__':
    app.run(port=5555, debug=True)

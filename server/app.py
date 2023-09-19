#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def user(username):
    print(username)
    return username

@app.route('/count/<string:count>')
def count(count):
    returny = ''
    for x in range(int(count)):
        returny += str(x) + '\n' 
    
    return returny 

@app.route('/math/<num1>/<operation>/<num2>')

def math(num1, operation, num2):

    if(operation == "+"):
        x = int(num1) + int(num2)
        return str(x)
    elif(operation == "-"):
        return str(int(num1) - int(num2))
    elif(operation == "*"):
        return str(int(num1) * int(num2))
    elif(operation == "div"):
        return str(int(num1) / int(num2))
    elif(operation == "%"):
        return str(int(num1) % int(num2))

    else:
        return 0 


if __name__ == '__main__':
    app.run(port=5555, debug=True)






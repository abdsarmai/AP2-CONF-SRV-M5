#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenue chez Abdallah et Maïssa !</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.50')

import requests
import numpy as np
import scipy
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

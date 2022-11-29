from flask import Flask, render_template
import numpy as np


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/about/')
def about():
    return 'This project is about ontologies in computing'

@app.route('/run/')
def run():
    return render_template('../html/run.html')

if __name__ == '__main__':
    app.run(port=5000)

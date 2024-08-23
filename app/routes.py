from flask import Flask, render_template
from app import init

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

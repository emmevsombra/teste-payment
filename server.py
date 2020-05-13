from flask import Flask, render_template
from apipaypal import Paypal

app = Flask(__name__)
paypal = Paypal()

@app.route('/')
def index():
    return render_template('index.html')

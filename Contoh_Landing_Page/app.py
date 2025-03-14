from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dashboard')
def dashboard():
    a = round(random.uniform(20,40), 2)
    b = round(random.uniform(960, 1050), 2)
    c = round(random.uniform(0, 100), 2)
    return render_template('dashboard.html', suhu=a, tekanan=b, kelembapan=c)


if __name__ == '__main__' :
    app.run(debug=True)
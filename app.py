from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Python.html')
def python():
    return render_template('python.html')

@app.route('/WebDesign.html')
def WebDesign():
    return render_template('WebDesign.html')

@app.route('/WebApp.html')
def WebApp():
    return render_template('WebApp.html')

@app.route('/Database.html')
def Database():
    return render_template('Database.html')

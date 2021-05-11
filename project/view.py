from project import app  # project是專案裡的資料夾名稱
from project import db
from flask import render_template

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/Python.html')
def python():
    return render_template('Python.html')


@app.route('/WebDesign.html')
def WebDesign():
    return render_template('WebDesign.html')


@app.route('/WebApp.html')
def WebApp():
    return render_template('WebApp.html')


@app.route('/Database.html')
def Database():
    return render_template('Database.html')

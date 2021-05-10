from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import db
app = Flask(__name__)
DB = db.DatabaseDriver()
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

# Create classData


@app.route("/CreateData/", methods=["POST"])
def CreateData():
    body = json.loads(request.data)
    Date = body["Date"]
    Teacher = body["Teacher"]
    Class1 = body["Class1"]
    Class2 = body["Class2"]
    Class3 = body["Class3"]
    Class4 = body["Class4"]
    Class5 = body["Class5"]
    Class6 = body["Class6"]
    Class7 = body["Class7"]

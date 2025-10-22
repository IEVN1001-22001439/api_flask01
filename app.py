from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route("/index")
def index():
    titulo="IEVN1001"
    listado=["Python", "Flask", "HTML", "CSS", "JavaScript"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route("/aporb")
def apor():
    return render_template('aporb.html')

@app.route("/resultado", methods=['POST'])
def resultado():
    n1=request.form.get("a")
    n2=request.form.get("b")
    return "La multiplicación de {} por {} es {}".format(n1, n2, int(n1)*int(n2))

@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    return render_template('distancia.html')

@app.route("/", methods=['GET', 'POST'])
def resultadoDist():
    x1=float(request.form.get("x1"))
    x2=float(request.form.get("x2"))
    y1=float(request.form.get("y1"))
    y2=float(request.form.get("y2"))
    return "La distancia entre {}, {} y {}, {} es {}".format(x1, y1, x2, y2, math.sqrt((x2-x1)**2 + (y2-y1)**2))
    

@app.route('/hola')
def func():
    return "<h1>¡Hola!</h1>"

@app.route('/user/<string:user>')
def user(user):
    return "<h1>¡Hello,{}!</h1>".format(user)

@app.route("/square/<int:num>")
def square(num):
    return "<h1>The square of {} is {}.</h1>".format(num, num**2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return "<h1>" + " ".join([text] * times) + "</h1>"

@app.route("/suma/<float:a>/<float:b>")
def suma(a,b):
    return "<h1>The sum of {} and {} is {}.</h1>".format(a,b, a+b)

if __name__ == '__main__':
    app.run(debug=True)
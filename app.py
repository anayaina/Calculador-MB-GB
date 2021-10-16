from flask import Flask, render_template, request, session
from werkzeug.utils import redirect

app = Flask(__name__)

#ANA PAULINA ANAYA ARIAS
#7 de mayo del 2020

#HOME
@app.route('/', methods=['GET','POST'])
def home():
    resultado=None
    if request.method == 'POST':
        tamaño = request.form['tamaño']
        velocidad = request.form['velocidad']
        duración = request.form['duración']
        valor = request.form['calcular']
        if(valor=="Calcular velocidad"):
            if (tamaño == '' or duración == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            velocidad = (int(tamaño)*8)/int(duración)
            total = str(velocidad)+' Mb/s'
        if (valor =="Calcular duración"):
            if (tamaño == '' or velocidad == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            duración = (int(tamaño)*8)/int(velocidad)
            total = str(duración)+' s'
        if (valor =="Calcular tamaño"):
            if (velocidad == '' or duración == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            tamaño = (int(velocidad)*int(duración))/8
            total = str(tamaño)+' MB'
        
        return render_template("home.html", resultado=total)
    else:
        return render_template("home.html")

@app.route('/gb', methods=['GET','POST'])
def gb():
    resultado=None
    if request.method == 'POST':
        tamaño = request.form['tamaño']
        velocidad = request.form['velocidad']
        duración = request.form['duración']
        valor = request.form['calcular']
        if(valor=="Calcular velocidad"):
            if (tamaño == '' or duración == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            velocidad = (int(tamaño)*8)/int(duración)
            total = str(velocidad)+' Gb/s'
        if (valor =="Calcular duración"):
            if (tamaño == '' or velocidad == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            duración = (int(tamaño)*8)/int(velocidad)
            total = str(duración)+' s'
        if (valor =="Calcular tamaño"):
            if (velocidad == '' or duración == ''):
                return render_template("index.html", resultado='Rellena los campos correctos.')
            tamaño = (int(velocidad)*int(duración))/8
            total = str(tamaño)+' GB'
        
        return render_template("gb.html", resultado=total)
    else:
        return render_template("gb.html")


if __name__ == "__main__":
    app.run(debug=True)
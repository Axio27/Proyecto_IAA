import os
from types import MethodDescriptorType
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, templating
from datetime import date, datetime

app = Flask (__name__)
app.config['REPOSITORIO'] = "./BBDD"

@app.route ('/')
def carga_archivo():
    return render_template('plantilla.html')

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['REPOSITORIO'], filename))
        now = datetime.now()
        return "Carga exitosa: " + str(now.date()) + ' ' + str(now.time())


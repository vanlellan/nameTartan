#!/usr/bin/python3
from flask import Flask, redirect, request, render_template, url_for
import os
import sys
import png
sys.path.insert(1, os.path.realpath(os.path.pardir))
from nameTartan import genNameTartan

#webapp to generate name tartans
#text field to input full name
#display image below (only one at a time)


app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return redirect(url_for('tartan', name='name-tartan-generator'))

@app.route('/<name>')
def tartan(name,page=None):
    fml, img = genNameTartan(name.split('-'), False)
    outFileName = f"{fml[0]}-{fml[1]}-{fml[2]}.png"
    with open('./static/'+outFileName, "wb") as outFile:
        w = png.Writer(len(img), len(img), greyscale=False)
        w.write(outFile, img)
    return render_template("tartan.html", genTartan = '/static/'+outFileName)

@app.route('/<name>', methods=['POST'])
def tartan_post(name,page=None):
    name = request.form['namebox']
    hyphensearch = '-'.join(name.split(' '))
    return redirect(url_for('tartan', name=hyphensearch))

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')

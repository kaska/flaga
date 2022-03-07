from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")


if __name__=="__main__":
    app.run()

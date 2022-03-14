from flask import Flask, render_template
import os
import random

from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem


app=Flask(__name__)

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/it-trends')
def xd():
    return render_template("it-trends.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    zmienna_python = 'abc'
    return render_template("ciekawe-postacie.html")#, zmienna_html=zmienna_python)

@app.route('/brudnopis')
def brudnopis():
    #hero = character( "Ija Kiwa")
    #return render_template("brudnopis.html", hero=hero)
    super_heroes = [ 'Bruce Lee', 'Kopernik', 'Kubuś Puchatek' ]
    chosen_hero = random.choice( super_heroes)
    super_hero = character( chosen_hero).encode('utf-8').decode()

    poem_lines = open_poem()

    return render_template("brudnopis.html", hero=super_hero, super_heroes=super_heroes, poem_lines=poem_lines)

if __name__=="__main__":
    app.run()

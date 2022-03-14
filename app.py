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
def it_trends():
    return render_template("it-trends.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
     characters_list = [
         "Małysz",
         "Kopernik",
         "Steve Wozniak",
         "Maria Skłodowska",
         "Kościuszko"
     ]

     characters_descriptions = []
     for i in range(3):
         hero=random.choice(characters_list)
         index = characters_list.index(hero)
         characters_list.pop(index)
         character_desc = character(hero)
         words_num=len(character_desc.split())
         info = [hero, character_desc, words_num]
         characters_descriptions.append(info)
    
     characters_descriptions.sort(key = lambda x: x[2], reverse=True)

     #ciekawa_postac=character(random.choice(lista_ciekawych_postaci))
     return render_template("ciekawe-postacie.html", characters_descriptions=characters_descriptions)

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

from flask import Flask, render_template, g, request, session, redirect, url_for
import sqlite3
app = Flask(__name__)
app.secret_key = '123456789'

MENUDB = 'mushrooms.db'

@app.route('/')
def index():
    db = sqlite3.connect(MENUDB)
    menu = get_all(db)
    db.close()
    return render_template(
    'index.html',
    disclaimer='may contain traces of nuts',
    mushroomsdata=menu['mushrooms']
    )

def get_all(db):
    mushrooms = []
    cur = db.execute('SELECT * FROM mushroomsdata')
    for row in cur:
        mushrooms.append(list(row))
    return {'mushrooms':mushrooms}


@app.route('/myshroom')
def myshroom():
    return render_template('myshroom.html')
    #db = sqlite3.connect(MENUDB)
    #menu = fetchmushroomsdata(db)
   # db.close()
  
from crypt import methods
from app import app
from flask import render_template, url_for, redirect
from app import pokeSearch
from app.form import pokeForm
from app.pokeSearch import *


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/finder', methods= ["GET", "POST"])
def finder():
    form = pokeForm()
    print(form)
    if form.validate():
        pokemon = catchemall(form.pokemon.data)
        if isinstance(pokemon, str):
            return 'Try again. That is not a valid Pokemon'
        else:
            return render_template('finder.html', pokemon = pokemon, form = form)
    return render_template('finder.html', title = 'catchemall', form = form)
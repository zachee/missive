import os
from missive.models import db
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app

# create our blueprint :)
bp = Blueprint('missive', __name__)

@bp.route('/')
def show_entries():
    pass
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    # return render_template('show_entries.html', entries=entries)

@bp.route('/add', methods=['POST'])
def add_entry():
    pass
    # if not session.get('logged_in'):
    #     abort(401)
    # db = get_db()
    # db.execute('insert into entries (title, text) values (?, ?)',
    #              [request.form['title'], request.form['text']])
    # db.commit()
    # flash('New entry was successfully posted')
    # return redirect(url_for('show_entries'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    pass
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != current_app.config['USERNAME']:
    #         error = 'Invalid username'
    #     elif request.form['password'] != current_app.config['PASSWORD']:
    #         error = 'Invalid password'
    #     else:
    #         session['logged_in'] = True
    #         flash('You were logged in')
    #         return redirect(url_for('show_entries'))
    # return render_template('login.html', error=error)

@bp.route('/logout')
def logout():
    pass
    # session.pop('logged_in', None)
    # flash('You were logged out')
    # return redirect(url_for('show_entries'))
import os
from missive.models import db, Entries
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app

# create our blueprint :)
bp = Blueprint('missive', __name__)

@bp.route('/')
def show_entries():
    entries = Entries.query.all()
    return render_template('show_entries.html', entries=entries)

@bp.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db.session.add(Entries(title=request.form['title'], text=request.form['text']))
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('missive.show_entries'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('missive.show_entries'))
    return render_template('login.html', error=error)

@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('missive.show_entries'))
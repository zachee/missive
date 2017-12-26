import os
from missive.models import db, Entries, User
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app

# create our blueprint :)
bp = Blueprint('missive', __name__)

@bp.route('/')
def show_entries():
    entries={}
    if session.get('logged_in'):
        cur_user = User.query.filter_by(id=session['user_id']).first()
        if not cur_user:
            abort(401)
        # TODO adjust relationship so can addign to user object
        entries = Entries.query.filter_by(user_id=cur_user.id).all()
    return render_template('show_entries.html', entries=entries)

@bp.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    cur_user = User.query.filter_by(id=session['user_id']).first()
    print(cur_user)
    if not cur_user:
        abort(401)
    entry = Entries(title=request.form['title'],
                           text=request.form['text'],
                           user_id=cur_user.id)  # TODO adjust relationship so can addign to user object
    print(entry)
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('missive.show_entries'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ex_user = User.query.filter_by(name=username).first()
        if ex_user == None:
            error = 'Invalid username'
        elif not ex_user.validate_password(password):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['user_id'] = ex_user.id
            flash('You were logged in')
            return redirect(url_for('missive.show_entries'))
    return render_template('login.html', error=error)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ex_user = User.query.filter_by(name=username).first()
        if password != request.form['conf_password']:
            error = 'Passwords don\'t match'
        elif username == '':
            error = 'Username Required'
        elif password == '':
            error = 'Password Required'
        elif ex_user != None:
            error = 'Username Already Taken'
        else:
            db.session.add(User(name=username, password=password))
            db.session.commit()
            flash('Username Registered')
            return redirect(url_for('missive.login'))
    return render_template('register.html', error=error)

@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('missive.show_entries'))
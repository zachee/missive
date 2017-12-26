# Missive Notepad

Note taking web app based on the Flask tutorial found [here](http://flask.pocoo.org/docs/0.12/tutorial/ "Flask Tutorial"). This is just a little app created to help familiarize myself with Flask and SQLalchemy. It is not really intended to be used in any way in its current state.

## Building the Database

You can inially build the missive database by running factory.py as the main module

`python missive/factory.py`

I suggest downloading sqlite3 to checkthe DB was built properly

## Running the app

This app uses a python setup file so it can be installed like any other program. From the top level directory:

`pip install --editable .`

This program uses the Flask app factory pattern so it can be run from the runner module:

```export FLASK_APP=missive.run
export FLASK_DEBUG=true  # if you want debugging enabled
flask run```

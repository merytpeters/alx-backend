#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


# Mock users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Local languages and timezone setting"""
    locale_param = request.args.get('locale')
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Retrieve User by ID"""
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id, None)


@app.before_request
def before_request():
    """Set the user for the current request"""
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """Returns and renders the html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)

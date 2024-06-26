#!/usr/bin/env python3
"""a Python script that sets up a basic Flask app"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Represents configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Gets user from users"""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Sets user as global"""
    user = get_user()
    g.user = user


@app.route('/')
def home():
    """The Home page"""
    return render_template("7-index.html")


@babel.localeselector
def get_locale():
    """Gets locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Gets timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.UnknownTimeZonError:
            pass
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                return pytz.timezone(timezone)
            except pytz.UnknownTimeZoneError:
                pass
    timezone = request.headers.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

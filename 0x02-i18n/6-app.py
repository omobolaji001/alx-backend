#!/usr/bin/env python3
"""a Python script that sets up a basic Flask app"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


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
    return render_template("5-index.html")


@babel.localeselector
def get_local():
    """Gets locale"""
    url_loc = request.args.get('locale', default='en')
    request_loc = request.headers.get('locale')

    if url_loc and url_loc in app.config['LANGUAGES']:
        return url_loc
    if g.user:
        if g.user.get('locale') in app.config['LANGUAGES']:
            return user_loc
    if request_loc and request_loc in app.config['LANGUAGES']:
        return request_loc
    return app.config['BABEL_DEFAULT_LOCALE']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

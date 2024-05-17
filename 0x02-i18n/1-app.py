#!/usr/bin/env python3
"""a Python script that sets up a basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Represents configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    """The Home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()

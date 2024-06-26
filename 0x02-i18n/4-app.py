#!/usr/bin/env python3
"""a Python script that sets up a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Represents configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """The Home page"""
    return render_template("4-index.html")


@babel.localeselector
def get_local():
    """Gets locale from request"""
    return request.args.get('locale', default='en')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

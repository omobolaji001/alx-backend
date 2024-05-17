#!/usr/bin/env python3
"""a Python script that sets up a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """The Home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()

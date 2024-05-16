# Flask Babel Internationalization (i18n) Project

Welcome to the Flask Babel Internationalization (i18n) Project! This is a standalone project that will guide you through the process of setting up a basic Flask app with internationalization support using Babel. In this project, we will create a simple web application that can display content in multiple languages.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3
- Flask
- Flask-Babel extension
- Babel

You can install Flask-Babel using the following command:

```bash
$ pip3 install flask_babel==2.0.0
```

## Project Structure

The project is organized into different tasks, each building upon the previous one. Below, you'll find a brief overview of each task and its associated files.

### Task 0: Basic Flask App

In this task, you will set up a basic Flask app in `0-app.py`. The app will have a single `/` route and an `index.html` template that displays "Welcome to Holberton" as the page title and "Hello world" as the header. You can find the files in the following locations:

- `0-app.py`
- `templates/0-index.html`

### Task 1: Basic Babel Setup

In Task 1, you will install the Babel Flask extension and configure it for your app. You will create a `Config` class that defines available languages as `["en", "fr"]`, sets the default locale to "en," and configures the timezone to "UTC." The relevant files are:

- `1-app.py`
- `templates/1-index.html`

### Task 2: Get Locale from Request

Task 2 involves creating a `get_locale` function with the `babel.localeselector` decorator. This function will determine the best-matching language based on the user's request using `request.accept_languages`. The associated files are:

- `2-app.py`
- `templates/2-index.html`

### Task 3: Parametrize Templates

In Task 3, you will parametrize your templates using the `_` or `gettext` function. Message IDs `home_title` and `home_header` will be used. You will also set up a `babel.cfg` file and initialize translations for English and French. The files include:

- `3-app.py`
- `babel.cfg`
- `templates/3-index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`
- `translations/en/LC_MESSAGES/messages.mo`
- `translations/fr/LC_MESSAGES/messages.mo`

### Task 4: Force Locale with URL Parameter

The final task, Task 4, allows you to force a specific locale by adding a `locale` parameter to your app's URLs. The `get_locale` function will detect this parameter and use it if valid. This task also includes the following file:

- `4-app.py`
- `templates/4-index.html`

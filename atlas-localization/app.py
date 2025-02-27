from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Configure available languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

def get_locale():
    # Use request headers or a user-specific preference to determine local
    return request.accept_languages.best_match(['en', 'fr'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    # This will display the string in the appropriate language
    return _("Hello, World!")

if __name__ == "__main__":
    app.run()

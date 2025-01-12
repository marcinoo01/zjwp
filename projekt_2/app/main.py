from flask import Flask
from projekt_2.app.route.pokemon_route import pokemon_blueprint

app = Flask(__name__)

app.register_blueprint(pokemon_blueprint, url_prefix='/pokemon')

if __name__ == '__main__':
    app.run(debug=True)

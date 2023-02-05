# Aula 05 - WEB Arquivos Estáticos

from flask import Flask

app = Flask(__name__, static_folder='public')

if __name__ == '__main__':
    app.run(debug=True)
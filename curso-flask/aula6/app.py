# Aula 06 - Métodos HTTP

from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='public')

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
         #return "OK %s" % request.form["name"]
         return dumps(request.form)
         
    return "OK GET"

if __name__ == '__main__':
    app.run(debug=True)
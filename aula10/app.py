# Enviando dados para o template
from flask import Flask, render_template_string

app = Flask(__name__, template_folder='templates')

@app.route('/')
def notas():
    return render_templates('notas.html')

if __name__ == '__main__':
    app.run(debug=True)
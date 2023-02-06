# Aula 14 - CRUD em Flask com SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Estudante(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    estado = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    email = db.Column(db.String(150))
    profissao = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, endereco, estado, cidade, email, profissao, idade):
        self.nome = nome
        self.endereco = endereco
        self.estado = estado
        self.cidade = cidade
        self.email = email
        self.profissao = profissao
        self.idade = idade

@app.route('/')
def index():
    estudantes = Estudante.query.all()
    return render_template('index.html', estudantes=estudantes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        estudante = Estudante(request.form['nome'], request.form['endereco'], request.form['estado'], request.form['cidade'], 
                              request.form['email'], request.form['profissao'], request.form['idade'])
        db.session.add(estudante)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.endereco = request.form['endereco']
        estudante.estado = request.form['estado']
        estudante.cidade = request.form['cidade']
        estudante.email = request.form['email']
        estudante.profissao = request.form['profissao']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=estudante)

@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)

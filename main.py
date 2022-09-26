from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo("Tetris", "x", "y")
jogo2 = Jogo("God of war", "x", "y")
listaJogos = [jogo1, jogo2]

app = Flask(__name__)
app.secret_key = 'blablabla'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/jogoteca'
db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), nullable=False, primary_key = True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    #tipo o toString do java
    def __repr__(self):
        return '<Name %r>' % self.name



@app.route('/')
def index():
    return render_template('lista.html', titulo ='JOGOS', jogos = listaJogos)

@app.route('/novo')
def novoJogo():
    if 'usuario_logado' not in session:
        return redirect('/login')
    return render_template('novo.html', titulo="Novo jogo")

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect('/')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=['POST'])
def autenticar():
    if 'teste1' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Usuario não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')




app.run(debug=True)
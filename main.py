from ctypes import resize
from flask import Flask, render_template, request, redirect, session, flash

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
from flask import Flask, render_template, request, redirect, url_for

class Pessoa():
    
    def __init__(self, nomepessoa, email, senha, caes):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.caes = caes

class CaesRB():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
        
class CaesDoar():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade

pessoas = {}        
caesexo = {}
caesdoar = {}

app = Flask(__name__, static_url_path='')

@app.route('/')
def fistpage():
    return render_template('1.html')
    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
    
    return render_template('login.html', dic = pessoas, erro = '')
    
@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        cidade = request.form['cidade']
    
    return render_template('cadastro.html', dic = caesexo, erro = '')
    
@app.route('/caddoar', methods=['POST','GET'])
def caddoar():
    if request.method == 'POST':
        
        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        cidade = request.form['cidade']
    
    return render_template('caddoar.html', dic = caesdoar, erro = '')
    
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')
    
@app.route('/opt')
def opt():
    return render_template('opt.html')
    
@app.route('/opt/user')
def user():
    return render_template('user.html')
    
@app.route('/doar')
def doar():
    return render_template('doar.html')
    
@app.route('/adotar')
def adotar():
    return render_template('adotar.html')
    
@app.route('/adotar/adote')
def adote():
    return render_template('adote.html')

    
    
    
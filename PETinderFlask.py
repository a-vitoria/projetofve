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

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/cadastro')
def cadastro():
    nome = request.args['nome']
    raca = request.args['raca']
    sexo = request.args['sexo']
    idade = request.args['idade']
    cor = request.args['cor']
    saude = request.args['saude']
    cidade = request.args['cidade']
    
    return render_template('cadastro.html', dic = caesexo, erro = '')
    
@app.route('/perfil')

    
        
@app.route('/login')
def conta():
    nomepessoa = request.args['nomepessoa']
    email = request.args['email']
    senha = request.args['senha']
    
    return render_template('login.html', dic = pessoas, erro = '')
    
    
    
    
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='')

@app.route('/')
def fistpage():
    email = request.args['email']
    senha = request.args['senha']
    
    return render_template('1.html')
    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        pessoa = Pessoa(nomepessoa, email, senha)
        pessoa.SalvarPessoa()
    
    return render_template('login.html', erro = '')
    
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
        primeiro = CaesBR(nome, raca, sexo, idade, cor, saude, cidade)
        primeiro.SalvarCaesBR()
    
    return render_template('cadastro.html', erro = '')
    
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
        segundo = CaesDoar(nome, raca, sexo, idade, cor, saude, cidade)
        segundo.SalvarCaesDoar()
    
    return render_template('caddoar.html', erro = '')
    
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

    
    
    
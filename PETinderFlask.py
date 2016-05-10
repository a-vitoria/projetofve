from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='')

@app.route('/')
def firstpage():
    email = request.args['email']
    senha = request.args['senha']
    if email in dicionario:
        if senha in dicionario:
            return render_template('1.html', dic = dicionario)
        else: 
            e = 'Senha incorreta'
            return render_template('1.html', dic = dicionario, erro = e) 
    else:
        e = 'Usuário inválido'
        return render_template('1.html', dic = dicionario, erro = e)
    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        pessoa = Pessoa(nomepessoa, email, senha)
        pessoa.Salvar_Pessoa()
    
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
        primeiro.Salvar_CaesBR()
    
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
        segundo.Salvar_CaesDoar()
    
    return render_template('caddoar.html', erro = '')
    
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/perfil')
def perfil():
    #página que mostrará os cães cadastrados pelo usuário
    return render_template('perfil.html')
    
@app.route('/opt')
def opt():
    #página que mostrará as opções de cães e tem as setinhas para passar
    return render_template('opt.html')
    
@app.route('/opt/user')
def user():
    #informações sobre o cão escolhido
    return render_template('user.html')
    
@app.route('/doar')
def doar():
    #página que mostrará os animais cadastrados pelo usuário para doação
    return render_template('doar.html')
    
@app.route('/adotar')
def adotar():
    #animais disponíveis para doação e setinhas para passar
    return render_template('adotar.html')
    
@app.route('/adotar/adote')
def adote():
    #informações sobre o cão escolhido
    return render_template('adote.html')

    
    
    
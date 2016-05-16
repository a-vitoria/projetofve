from flask import Flask, render_template, request

import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
dogBR=[]
dogDoar=[]
EMAIL=[]

class Pessoa():
    
    def __init__(self, nomepessoa, email, senha):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.dicionario={}
        self.caosex=[]
        self.caodoa=[]
        
    def Salvar_Pessoa(self):
        self.dicionario[self.email]=self.nomepessoa,self.email,self.senha,self.caosex,self.caodoa
        EMAIL.append(self.email)        
        return self.dicionario
        

class Caes():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade,objeto):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
        self.email=objeto.email
        self.dicionariocaosex={}
        self.dicionariocaodoa={}
        
        
class CaesBR(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade,objeto):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade,objeto)
    
    def Salvar_CaesBR(self,objeto):
        self.dicionariocaosex[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.email
        objeto.dicionario[objeto.email][3].append(self.email)
        dogBR.append(self.nome)
        return self.dicionariocaosex
#    def Listar_CaesBR(self):
        
        
class CaesDoar(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade,objeto):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade,objeto)

    def Salvar_CaesDoar(self,objeto):
        self.dicionariocaodoa[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.email
        (objeto.email).dicionario[objeto.email][4].append(self.email)
        dogDoar.append(self.nome)
        return self.dicionariocaodoa
#    def Listar_CaesDoar(self):

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        PETinder.get(point="/ListaEMAIL")
        if email in EMAIL:
            PETinder.get(point="/Pessoas")
            if request.form['email'].dicionario[request.form['email'].email][2] == senha:
                return render_template('main.html', dic = request.form['email'].dicionario)
            else: 
                e = 'Senha incorreta'
                
                return render_template('main.html',dic=request.form['email'].dicionario, erro = e) 

    return render_template('main.html', dic = request.form['email'].dicionario, erro = e)     

    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        PETinder.get(point="/ListaEMAIL")
        if email in EMAIL:
            e = 'Email já cadastrado'
            return render_template('login.html',dic=request.form['email'].dicionario, erro = e)

            
        else:
            request.form['email'] = Pessoa(nomepessoa, email, senha)
            request.form['email'].Salvar_Pessoa()
            PETinder.put(point="/Pessoas",data=Pessoa.dicionario)
            PETinder.put(point="/ListaEMAIL",data=EMAIL)
            return render_template('login.html', erro = '')

    
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
        request.form['nome'] = CaesBR(nome, raca, sexo, idade, cor, saude, cidade)
        request.form['nome'].Salvar_CaesBR()
        
    PETinder.put(point="/Pessoas",data=Pessoa.dicionario)
    PETinder.put(point="/Caes_BR",data=CaesBR.dicionariocaosex)
    PETinder.put(point="/Caes_Doar",data=CaesDoar.dicionariocaodoa)
    PETinder.put(point="/ListadogBR",data=dogBR)
    PETinder.put(point="/ListadogDoar",data=dogDoar)
    PETinder.put(point="/ListaEMAIL",data=EMAIL)
    
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
        request.form['nome'] = CaesDoar(nome, raca, sexo, idade, cor, saude, cidade)
        request.form['nome'].Salvar_CaesDoar()
        
    PETinder.put(point="/Pessoas",data=Pessoa.dicionario)
    PETinder.put(point="/Caes_BR",data=CaesBR.dicionariocaosex)
    PETinder.put(point="/Caes_Doar",data=CaesDoar.dicionariocaodoa)
    PETinder.put(point="/ListadogBR",data=dogBR)
    PETinder.put(point="/ListadogDoar",data=dogDoar)
    PETinder.put(point="/ListaEMAIL",data=EMAIL)
    
    return render_template('caddoar.html', erro = '')
        
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/perfil')
def perfil():
    PETinder.get(point="/Pessoas")
    caes = Pessoa.dicionario[Pessoa.email][3]
    #return x
    #Listar_CaesBRA
    #página que mostrará os cães cadastrados pelo usuário
    return render_template('perfil.html', x=caes)
    
@app.route('/doar')
def doar():
    PETinder.get(point="/Pessoas")
    caesdoar = Pessoa.dicionario[Pessoa.email][4]
    #return y
    #Listar_CaesDoar
    #página que mostrará os animais cadastrados pelo usuário para doação
    return render_template('doar.html', y=caesdoar)
    

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)

    
    
    
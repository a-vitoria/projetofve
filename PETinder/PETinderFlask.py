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
        self.dicionario["email"]=self.email
        self.dicionario["nomepessoa"]=self.nomepessoa
        self.dicionario["senha"]=self.senha
        self.dicionario["caesBR"]=self.caosex
        self.dicionario["caesDoar"]=self.caodoa
           
        PETinder.put_sync(point="/Pessoas/{0}".format(self.email),data=self.dicionario)
        
        
        

class Caes():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
        self.dicionariocaosex={}
        self.dicionariocaodoa={}
        
        
class CaesBR(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)
    
    def Salvar_CaesBR(self,objeto):
        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["cor"]=self.cor
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["email"]=eval(PETinder.get_sync(point="/Pessoas/{0}/dicionario/email".format(request.form['email'])))
        dogBR.append(self.nome)
        return self.dicionariocaosex
#    def Listar_CaesBR(self):
        
        
class CaesDoar(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)

    def Salvar_CaesDoar(self,objeto):
        self.dicionariocaodoa["nome"]=self.nome
        self.dicionariocaodoa["sexo"]=self.sexo
        self.dicionariocaodoa["raca"]=self.raca
        self.dicionariocaodoa["cor"]=self.cor
        self.dicionariocaodoa["idade"]=self.idade
        self.dicionariocaodoa["saude"]=self.saude
        self.dicionariocaodoa["cidade"]=self.cidade
        self.dicionariocaodoa["email"]=PETinder.get_sync(point="/Pessoas/{0}/dicionario/email".format(request.form['email']))
        dogDoar.append(self.nome)
        return self.dicionariocaodoa
#    def Listar_CaesDoar(self):

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        L = eval(PETinder.get_sync(point="/ListaEMAIL/{0}".format(email)))
        if email == L:
            listasenha=[]
            s= eval(PETinder.get_sync(point="/Pessoas/{0}/senha".format(email)))
            listasenha.append(s)
            if senha in listasenha:
                return render_template('home.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)))
            else: 
                e = 'Senha incorreta'
                return render_template('main.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e) 
        else:
            e = 'Usuário inválido'
            return render_template('main.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e)
            
    return render_template('main.html', pessoa = Pessoa('','',''))        

    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        ema= (PETinder.get_sync(point="/ListaEMAIL/{0}".format(email)))
        if email == ema:
            e = 'Email já cadastrado'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e)
        elif email == "":
            e = 'O campo Email está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e)
        else:
            EMAIL.append(email)
            EMAIL[-1] = Pessoa(nomepessoa, email, senha)
            EMAIL[-1].Salvar_Pessoa() 
            PETinder.put_sync(point="/ListaEMAIL/{0}".format(email),data=email)                
            return render_template('home.html', dic = EMAIL[-1].dicionario)
    
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
        
#    PETinder.put_sync(point="/Pessoas",data=Pessoa.dicionario)
#    PETinder.put_sync(point="/Caes_BR",data=request.form['nome'].dicionariocaosex)
#    PETinder.put_sync(point="/Caes_Doar",data=CaesDoar.dicionariocaodoa)
#    PETinder.put_sync(point="/ListadogBR",data=dogBR)
#    PETinder.put_sync(point="/ListadogDoar",data=dogDoar)
#    PETinder.put_sync(point="/ListaEMAIL",data=EMAIL)
#    
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
        
    PETinder.put_sync(point="/Pessoas",data=Pessoa.dicionario)
    PETinder.put_sync(point="/Caes_BR",data=CaesBR.dicionariocaosex)
    PETinder.put_sync(point="/Caes_Doar",data=request.form['nome'].dicionariocaodoa)
    PETinder.put_sync(point="/ListadogBR",data=dogBR)
    PETinder.put_sync(point="/ListadogDoar",data=dogDoar)
    PETinder.put_sync(point="/ListaEMAIL",data=EMAIL)
    
    return render_template('caddoar.html', erro = '')
        
@app.route('/home', methods=['POST', 'GET'])
def home():
    botao=request.form['button']
    if request.method == 'GET':
        if botao == "parceiro":
            return render_template('perfil.html')
        
        elif botao == "doar":
            return render_template('doar.html')
        
        elif botao == "adotar":
            return render_template('adotar.html')
            
    return render_template('home.html')
        
@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    a= PETinder.get_sync(point="/Pessoas/{0}/3/0".format(request.form['email']))
    caes = a
    #return x
    #Listar_CaesBRA
    #página que mostrará os cães cadastrados pelo usuário
    return render_template('perfil.html', x=caes)
    
@app.route('/doar', methods=['POST', 'GET'])
def doar():
    b= PETinder.get_sync(point="/Pessoas/{0}/4/0".format(request.form['email']))
    caesdoar = b
    #return y
    #Listar_CaesDoar
    #página que mostrará os animais cadastrados pelo usuário para doação
    return render_template('doar.html', y=caesdoar)
    

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)    
    
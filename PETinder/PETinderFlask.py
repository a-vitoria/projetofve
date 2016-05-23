from flask import Flask, render_template, request, url_for, redirect

import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
dogBR=[]
dogDoar=[]
EMAIL=[]
NOME=[]

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
    def __init__(self,nome,raca,sexo,cidade,idade,cor,saude):
        Caes.__init__(self,nome,raca,sexo,cidade,idade,cor,saude)
    
    def Salvar_CaesBR(self):

        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["cor"]=self.cor        
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaosex["email"]=eval(PETinder.get_sync(point="/Pessoas/a/email"))
        dogBR.append(self.nome)
        PETinder.put_sync(point="/Pessoas/a/Caes_BR/{0}".format(self.nome),data=self.dicionariocaosex)

    def Del_CaesBR(self):
        
        PETinder.delete_sync(point="Pessoas/{0}/caesBR".format("a"))        
        PETinder.delete_sync(point="Pessoas/{0}/Caes_BR".format("a"))

        
        
class CaesDoar(Caes):
    def __init__(self,nome,raca,sexo,cidade,idade,cor,saude):
        Caes.__init__(self,nome,raca,sexo,cidade,idade,cor,saude)

    def Salvar_CaesDoar(self):
        
        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["cor"]=self.cor        
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaodoa["email"]=PETinder.get_sync(point="/Pessoas/a/email")
        dogDoar.append(self.nome)
        PETinder.put_sync(point="/Pessoas/a/CaesDoar/{0}".format(self.nome),data=self.dicionariocaodoa)
        print("oba")
    def Del_CaesBR(self):
        
        PETinder.delete_sync(point="Pessoas/a/caesDoar")
        PETinder.delete_sync(point="Pessoas/a/Caes_Doar")

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        L = eval(PETinder.get_sync(point="/ListaEMAIL"))
        if email in L:
            listasenha=[]
            s= eval(PETinder.get_sync(point="/Pessoas/{0}/senha".format(email)))
            listasenha.append(s)
            if senha in listasenha:
                return render_template('home.html', email=email)
            else: 
                e = 'Senha incorreta'
                
                return render_template('main.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e) 
        else:
            e = 'Usuário inválido'
            return render_template('main.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(email)), erro = e)
#    el=request.args['email']
    return render_template('main.html', pessoa = Pessoa('','',''))        

    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        ema= eval(PETinder.get_sync(point="/ListaEMAIL"))
        if email in ema:
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
#    el=request.args['email']
    return render_template('login.html', erro = '')
    
@app.route('/cadastro', methods=['POST','GET'])
def cadastro():

    if request.method=='POST':


        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        cidade = request.form['cidade']
        NOME.append(nome)
        NOME[-1] = CaesBR(nome, raca, sexo, idade, cor, saude, cidade)
        NOME[-1].Salvar_CaesBR()
        return render_template('perfil.html')
    PETinder.put_sync(point="/ListadogBR",data=dogBR)
    return render_template('cadastro.html', erro = '')
    
    
    
@app.route('/caddoar', methods=['POST','GET'])
def caddoar():
    if request.method == 'POST':     
        print('2')
        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        cidade = request.form['cidade']
        NOME.append(nome)
        NOME[-1] = CaesDoar(nome, raca, sexo, idade, cor, saude, cidade)
        NOME[-1].Salvar_CaesDoar()
        return render_template('doar.html')
        
    PETinder.put_sync(point="/ListadogDoar",data=dogDoar)    
    return render_template('caddoar.html', erro = '')
        
@app.route('/home', methods=['POST', 'GET'])
def home():
  
    button=request.args['button']
    
    if request.method == 'GET':
        if button == "parceiro":
            
            return render_template('perfil.html', email = "a")
        
        elif button == "doar":
            return render_template('doar.html', email = "a" )
        
        elif button == "adotar":
            return render_template('adotar.html', email = "a" )
            
    return render_template('home.html')
        
@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
          
    if request.method == 'POST':
        a= eval(PETinder.get_sync(point="/Pessoas/a/Caes_BR/{0}/nome".format("nome")))
        caes = a

    #Listar_CaesBR
    #página que mostrará os cães cadastrados pelo usuário
    return redirect(url_for('perfil', x=caes))
    
@app.route('/doar', methods=['POST', 'GET'])
def doar():
    print('doar')
    if request.method == 'POST':
        b= eval(PETinder.get_sync(point="/Pessoas/a/Caes_Doar/{0}/nome".format("nome")))
        caesdoar = b

    #Listar_CaesDoar
    #página que mostrará os animais cadastrados pelo usuário para doação
    return redirect(url_for('doar', y=caesdoar))
    
@app.route('/opt', methods=['POST', 'GET'])
def opt():
    return render_template('opt.html')
    
@app.route('/opt/user', methods=['POST', 'GET'])
def user():
    return render_template('user.html')
    
@app.route('/adotar', methods=['POST', 'GET'])
def adotar():
    button = request.args['button']
    if request.methods == 'POST':
        print ("foi")
        if button == "adotar":
            return render_template('adote.html')
        
        
    return render_template('adotar.html')
    
@app.route('/adotar/adote', methods=['POST', 'GET'])
def adote():
    return render_template('adote.html')
    

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)   
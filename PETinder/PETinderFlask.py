from flask import Flask, render_template, request, url_for, redirect
import random
import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
dogBR=[]
dogDoar=[]
USER=[]
NOME=[]
ListadogBR=[]
ListadogDoar=[]


class Pessoa():
    
    def __init__(self, pessoa, nomepessoa, email, senha):
        self.pessoa=pessoa
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.dicionario={}
        self.caosex=[]
        self.caodoa=[]
        
    def Salvar_Pessoa(self):
        self.dicionario["pessoa"]=self.pessoa
        self.dicionario["email"]=self.email
        self.dicionario["nomepessoa"]=self.nomepessoa
        self.dicionario["senha"]=self.senha
        self.dicionario["caesBR"]=self.caosex
        self.dicionario["caesDoar"]=self.caodoa
           
        PETinder.put_sync(point="/Pessoas/{0}".format(self.nomepessoa),data=self.dicionario)
        
        

class Caes():
    
    def __init__(self, nome, raca, sexo, idade, cor, saude, cidade):
        self.nome = nome
        self.raca = raca
        self.sexo = sexo
        self.cidade = cidade    
        self.idade = idade
        self.cor = cor
        self.saude = saude
        self.dicionariocaosex={}
        self.dicionariocaodoa={}
        
        
class CaesBR(Caes):
    def __init__(self,nome,raca,sexo,cidade,idade,cor,saude):
        Caes.__init__(self,nome,raca,sexo,cidade,idade,cor,saude)
    
    def Salvar_CaesBR(self,user):
        
        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["cor"]=self.cor        
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaosex["nomepessoa"]=eval(PETinder.get_sync(point="/Pessoas/{0}/nomepessoa".format(user)))
        ListadogBR.append(self.dicionariocaosex)
        PETinder.put_sync(point="/Pessoas/{0}/Caes_BR/{1}".format(user,self.nome),data=self.dicionariocaosex)
        PETinder.put_sync(point="/ListadogBR/{0}".format(self.nome),data=ListadogBR[-1])
        
def Del_CaesBR(nome):
    print (nome)
    dono=eval(PETinder.get_sync("/ListadogBR/{0}/nomepessoa".format(nome)))
    PETinder.delete_sync(point="Pessoas/{0}/Caes_BR/{1}".format(dono,nome))
    PETinder.delete_sync(point="ListadogDoar/{0}".format(nome))

        
        
class CaesDoar(Caes):
    def __init__(self,nome,raca,sexo,cidade,idade,cor,saude):
        Caes.__init__(self,nome,raca,sexo,cidade,idade,cor,saude)

    def Salvar_CaesDoar(self,user):
        
        self.dicionariocaodoa["nome"]=self.nome
        self.dicionariocaodoa["raca"]=self.raca
        self.dicionariocaodoa["sexo"]=self.sexo
        self.dicionariocaodoa["cidade"]=self.cidade
        self.dicionariocaodoa["idade"]=self.idade
        self.dicionariocaodoa["cor"]=self.cor        
        self.dicionariocaodoa["saude"]=self.saude
        self.dicionariocaodoa["nomepessoa"]=eval(PETinder.get_sync(point="/Pessoas/{0}/nomepessoa".format(user)))
        ListadogDoar.append(self.dicionariocaodoa)
        PETinder.put_sync(point="/Pessoas/{0}/CaesDoar/{1}".format(user,self.nome),data=self.dicionariocaodoa)
        PETinder.put_sync(point="/ListadogDoar/{0}".format(self.nome),data=ListadogDoar[-1])
def Del_CaesDoar(nome):
    dono=eval(PETinder.get_sync("/ListadogDoar/{0}/nomepessoa".format(nome)))
    PETinder.delete_sync(point="Pessoas/{0}/CaesDoar/{1}".format(dono,nome))
    PETinder.delete_sync(point="ListadogDoar/{0}".format(nome))

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        senha = request.form['senha']
        L = eval(PETinder.get_sync(point="/ListaUSER"))
        if nomepessoa in L:
            listasenha=[]
            s= eval(PETinder.get_sync(point="/Pessoas/{0}/senha".format(nomepessoa)))
            listasenha.append(s)
            if senha in listasenha:
                return render_template('home.html', nomepessoa=nomepessoa)
            else: 
                e = 'Senha incorreta'
                
                return render_template('main.html', nomepessoa=nomepessoa, dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e) 
        else:
            e = 'Usuário inválido'
            return render_template('main.html', nomepessoa=nomepessoa, dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
#    el=request.args['email']
    return render_template('main.html', pessoa = Pessoa('','','',''))        

    
@app.route('/login', methods=['POST','GET'])
def conta():
    if request.method == 'POST':
        nome = request.form['pessoa']
        nomepessoa = request.form['nomepessoa']
        email = request.form['email']
        senha = request.form['senha']
        use= eval(PETinder.get_sync(point="/ListaUSER"))
        if nomepessoa in use:
            e = 'Usuário já cadastrado'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
        elif email == "":
            e = 'O campo Email está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
        elif senha == "":
            e = 'O campo Senha está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)        
        elif nomepessoa == "":
            e = 'O campo Usuário está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)        
        elif nome == "":
            e = 'O campo Nome está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
        else:
            USER.append(nomepessoa)
            USER[-1] = Pessoa(nome , nomepessoa, email, senha)
            USER[-1].Salvar_Pessoa() 
            PETinder.put_sync(point="/ListaUSER/{0}".format(nomepessoa),data=nomepessoa)                
            return render_template('home.html', dic = USER[-1].nomepessoa, nomepessoa = nomepessoa)

    return render_template('login.html', erro = '')
    
@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    user=request.args['user']
    if request.method=='POST':

        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        cidade = request.form['cidade']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        
        NOME.append(nome)
        NOME[-1] = CaesBR(nome, raca, sexo, idade, cor, saude, cidade)
        NOME[-1].Salvar_CaesBR(user)
        return redirect(url_for('perfil', user=user))

    return render_template('cadastro.html',nomepessoa = user, erro = '')
    
    
    
@app.route('/caddoar', methods=['POST','GET'])
def caddoar():
    user=request.args['user']
    if request.method == 'POST':     
        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        cidade = request.form['cidade']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        NOME.append(nome)
        NOME[-1] = CaesDoar(nome, raca, sexo, idade, cor, saude, cidade)
        NOME[-1].Salvar_CaesDoar(user)
        return redirect(url_for('doar', user=user))
        
   
    return render_template('caddoar.html', nomepessoa = user, erro = '')
        
@app.route('/home', methods=['POST', 'GET'])
def home():
  
    button=request.form['button']
    user=request.args['user']
    print (ListadogBR)
    
    if request.method == 'POST':
        
        if button == "parceiro":
            try:
                listausers= eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR".format(user)))
                for y in listausers:
                    return redirect(url_for('perfil', user=user))
            except:
                return render_template('perfil.html', nomepessoa=user)
        
        elif button == "doar":
            try:
                listauser=eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar".format(user)))
                for x in listauser:                
                    return redirect(url_for('doar', user = user ))
            except:
                return render_template('doar.html', nomepessoa = user)
        
        elif button == "adotar":
            return render_template('adotar.html', nomepessoa = user )
            
    return render_template('home.html', nomepessoa = user)
        
@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    user=request.args['user']
    caesb= eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR".format(user)))
    listacaes=[]
    for j in caesb:
        caes=eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR/{1}/nome".format(user, j)))
        listacaes.append(caes)
    #página que mostrará os animais cadastrados pelo usuário
    return render_template('perfil.html', nomepessoa=user, caesb=caesb)
    
@app.route('/doar', methods=['POST', 'GET'])
def doar():
    user=request.args['user']
    caesdoar= eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar".format(user)))
    listacaesd=[]
    for i in caesdoar:
        caesd=eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar/{1}/nome".format(user, i)))
        listacaesd.append(caesd)
    #Listar_CaesDoar
    #página que mostrará os animais cadastrados pelo usuário para doação
    return render_template('doar.html', nomepessoa=user, caesdoar=caesdoar)
    
@app.route('/opt', methods=['POST', 'GET'])
def opt():
    user=request.args['user']
    nome=request.args['nome']
    print("quase foi")
    cachorros=(eval(PETinder.get_sync(point = "/ListadogBR/{0}".format(random.choice), data=ListadogBR)))
    print (cachorros)
    h = cachorros
    if request.method == 'POST':
        print("foi")
        
        h=random.choice(eval(PETinder.get_sync(point = "/ListadogBR",data=ListadogBR)))
        
    return render_template('opt.html', cao = h, dic = (eval(PETinder.get_sync(point = "/ListadogBR/{0}".format(random.choice), data=ListadogBR), nomepessoa = user, nome = nome)))
                
    
    
@app.route('/user', methods=['POST', 'GET'])
def usuario():
    user=request.args['user']
    
    
    
@app.route('/adotar', methods=['POST', 'GET'])
def adotar():
    user=request.args['user']
    nome=request.args['nome']
    button = request.form['button']
    print (ListadogDoar)
    h=random.choice(eval(PETinder.get_sync(point = "/ListadogDoar", data=ListadogDoar)))
    if request.method == 'POST':
        print ("foi")
        if button == "adotar":
            return render_template('adote.html')
        
        
    return render_template('adotar.html', cao = h, user = user, nome = nome)
    
@app.route('/adote', methods=['POST', 'GET'])
def adote():
    user=request.args['user']
    adot=eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar".format(user)))
    listaadote=[]    
    for f in adot:
        caesad=eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar/{1}".format(user, f)))
        listaadote.append(caesad)
    return render_template('adote.html', caesad=caesad)

@app.route('/del', methods=['POST', 'GET']) 
def delete1():
    nome=request.args['nome']
    print(nome)
    Del_CaesBR(nome)
#    Del_CaesDoar(nome)
    
    #apos finalizar o tratamento, volta para a pagina principal
    return redirect(url_for('main'))   

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)   
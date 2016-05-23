from flask import Flask, render_template, request, url_for, redirect

import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
dogBR=[]
dogDoar=[]
USER=[]
NOME=[]

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
    
    def Salvar_CaesBR(self,user):
        
        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["cor"]=self.cor        
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaosex["email"]=eval(PETinder.get_sync(point="/Pessoas/{0}/email".format(user)))
        dogBR.append(self.nome)
        PETinder.put_sync(point="/Pessoas/{0}/Caes_BR/{1}".format(user,self.nome),data=self.dicionariocaosex)

    def Del_CaesBR(self,user):
        
        PETinder.delete_sync(point="Pessoas/{0}/caesBR".format(user))        
        PETinder.delete_sync(point="Pessoas/{0}/Caes_BR".format(user))

        
        
class CaesDoar(Caes):
    def __init__(self,nome,raca,sexo,cidade,idade,cor,saude):
        Caes.__init__(self,nome,raca,sexo,cidade,idade,cor,saude)

    def Salvar_CaesDoar(self,user):
        
        self.dicionariocaosex["nome"]=self.nome
        self.dicionariocaosex["raca"]=self.raca
        self.dicionariocaosex["sexo"]=self.sexo
        self.dicionariocaosex["cidade"]=self.cidade
        self.dicionariocaosex["idade"]=self.idade
        self.dicionariocaosex["cor"]=self.cor        
        self.dicionariocaosex["saude"]=self.saude
        self.dicionariocaodoa["email"]=PETinder.get_sync(point="/Pessoas/{0}/email".format(user))
        dogDoar.append(self.nome)
        PETinder.put_sync(point="/Pessoas/{0}/CaesDoar/{1}".format(user,self.nome),data=self.dicionariocaodoa)
        print("oba")
    def Del_CaesBR(self,user):
        
        PETinder.delete_sync(point="Pessoas/{0}/caesDoar".format(user))
        PETinder.delete_sync(point="Pessoas/{0}/Caes_Doar".format(user))

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    
    if request.method == 'POST':
        nomepessoa = request.form['nomepessoa']
        print(nomepessoa)
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
            e = 'User já cadastrado'

            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
        elif email == "":
            e = 'O campo Email está vazio'
            return render_template('login.html', dic = PETinder.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
        else:
            USER.append(nomepessoa)
            USER[-1] = Pessoa(nome , nomepessoa, email, senha)
            USER[-1].Salvar_Pessoa() 
            PETinder.put_sync(point="/ListaUSER/{0}".format(nomepessoa),data=nomepessoa)                
            return render_template('home.html', dic = USER[-1].nomepessoa)
#    el=request.args['email']
    return render_template('login.html', erro = '')
    
@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    user=request.args['user']
    print (user)
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
        NOME[-1].Salvar_CaesBR(user)
        return render_template('perfil.html',nomepessoa = user)
    PETinder.put_sync(point="/ListadogBR",data=dogBR)
    return render_template('cadastro.html',nomepessoa = user, erro = '')
    
    
    
@app.route('/caddoar', methods=['POST','GET'])
def caddoar():
    user=request.args['user']
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
        NOME[-1].Salvar_CaesDoar(user)
        return render_template('doar.html')
        
    PETinder.put_sync(point="/ListadogDoar",data=dogDoar)    
    return render_template('caddoar.html', erro = '')
        
@app.route('/home', methods=['POST', 'GET'])
def home():
  
    button=request.form['button']
    user=request.args['user']
    
    if request.method == 'POST':
        if button == "parceiro":
            
            return render_template('perfil.html', nomepessoa = user)
        
        elif button == "doar":
            return render_template('doar.html', nomepessoa = user )
        
        elif button == "adotar":
            return render_template('adotar.html', nomepessoa = user )
            
    return render_template('home.html', nomepessoa = user)
        
@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    user=request.args['user'] 
    if request.method == 'POST':
        a= eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR/{1}".format(user)))
        caes = a

    #Listar_CaesBR
    #página que mostrará os cães cadastrados pelo usuário
    return redirect(url_for('perfil', x=caes))
    
@app.route('/doar', methods=['POST', 'GET'])
def doar():
    user=request.args['user']
    print('doar')
    if request.method == 'POST':
        b= eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_Doar/{1}/nome".format(user,nome)))
        caesdoar = b

    #Listar_CaesDoar
    #página que mostrará os animais cadastrados pelo usuário para doação
    return redirect(url_for('doar', y=caesdoar))
    
@app.route('/opt', methods=['POST', 'GET'])
def opt():
    user=request.args['user']
    return render_template('opt.html')
    
@app.route('/opt/usuario', methods=['POST', 'GET'])
def usuario():
    user=request.args['user']
    return render_template('user.html')
    
@app.route('/adotar', methods=['POST', 'GET'])
def adotar():
    user=request.args['user']
    button = request.form['button']
    if request.methods == 'POST':
        print ("foi")
        if button == "adotar":
            return render_template('adote.html')
        
        
    return render_template('adotar.html')
    
@app.route('/adotar/adote', methods=['POST', 'GET'])
def adote():
    user=request.args['user']
    return render_template('adote.html')
    

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)   
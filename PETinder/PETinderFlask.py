from flask import Flask, render_template, request, url_for, redirect
import random
import firecall
"""
O FireBase é um database que utiliza dicionarios e listas para fazer armazanamentos,
para isso criamos o nosso, chamado PETinder, onde salva os dicionarios que queremos 
na url a seguir:https://petinder.firebaseio.com/ e usamos metodos do firecall
 que importamos para fazer esta conexao
"""
"""
O firecall faz essa ligacao entre o flask e FireBase, os metodos importados para uso sao
arquivos como put, para inserir o dado recebido para o firebase e get para que pegar um
dado no firebase e enviar para o flask, alem disso utilizamos o eval que funciona 
como um transformador, ele pega os dados do firebase em binario e transforma em string

"""
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
USER=[]
NOME=[]
ListadogBR=[]
ListadogDoar=[]
'''As listas acima foram criadas para armazenar todos os dados que necessitariamos
fazer verificacoes se ja existe um nome ou email, utilizado apenas para facilitar 
o uso geral. As funcoes abaixo sao usadas para pegar deletar os caes, nao sao 
partes do objeto porque alem o usuario poder apagar, ao ser adotado ou encontrado
um parceiro por parte de outra pessoa que pode aceitar o cao, assim, o cao nao deve esetar disponivel na lista do outro
'''
def Del_CaesBR(nome):
    dono=eval(PETinder.get_sync(point="/ListadogBR/{0}/nomepessoa".format(nome)))
    PETinder.delete_sync(point="Pessoas/{0}/Caes_BR/{1}".format(dono,nome))
    PETinder.delete_sync(point="ListadogBR/{0}".format(nome))

def Del_CaesDoar(nome):
    dono=eval(PETinder.get_sync(point="/ListadogDoar/{0}/nomepessoa".format(nome)))
    PETinder.delete_sync(point="Pessoas/{0}/CaesDoar/{1}".format(dono,nome))
    PETinder.delete_sync(point="ListadogDoar/{0}".format(nome))
    
'''
Objetos foram criados para facilitar na montagem dos atributos de cada pessoa, 
e cada cao, deixando o codigo mais organizado e facil de arrumar
'''
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
        self.dicionariocaosex["email"]=eval(PETinder.get_sync(point="/Pessoas/{0}/email".format(user)))        
        self.dicionariocaosex["nomepessoa"]=eval(PETinder.get_sync(point="/Pessoas/{0}/nomepessoa".format(user)))
        ListadogBR.append(self.dicionariocaosex)
        PETinder.put_sync(point="/Pessoas/{0}/Caes_BR/{1}".format(user,self.nome),data=self.dicionariocaosex)
        PETinder.put_sync(point="/ListadogBR/{0}".format(self.nome),data=ListadogBR[-1])
        

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
        self.dicionariocaodoa["email"]=eval(PETinder.get_sync(point="/Pessoas/{0}/email".format(user)))        
        self.dicionariocaodoa["nomepessoa"]=eval(PETinder.get_sync(point="/Pessoas/{0}/nomepessoa".format(user)))
        ListadogDoar.append(self.dicionariocaodoa)
        PETinder.put_sync(point="/Pessoas/{0}/CaesDoar/{1}".format(user,self.nome),data=self.dicionariocaodoa)
        PETinder.put_sync(point="/ListadogDoar/{0}".format(self.nome),data=ListadogDoar[-1])
"""
Aqui seria todos os metodos que utilizamos para controlar melhor o que colocamos no FireBase,
ao longo do codigo ha outros metodos para fazer pesquisas no FireBase, porem nao criamos funcoes
porque seria algo que teria uso pequeno, em condicoes especiais
"""

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['POST','GET'])
def firstpage():
    #LOGIN
    if request.method == 'POST': #Quando o método for POST
        nomepessoa = request.form['nomepessoa'] #Recebe nomepessoa do HTML
        senha = request.form['senha'] #Recebe senha do HTML
        L = eval(PETinder.get_sync(point="/ListaUSER")) #Chama ListaUSER do firebase
        #Validação do login:
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

    return render_template('main.html', pessoa = Pessoa('','','',''))        

    
@app.route('/login', methods=['POST','GET'])
def conta():
    #CADASTRO DO USUÁRIO
    if request.method == 'POST':
        nome = request.form['pessoa'] #Recebe pessoa do HTML como nome
        nomepessoa = request.form['nomepessoa'] #Recebe nomepessoa do HTML
        email = request.form['email'] #Recebe email do HTML
        senha = request.form['senha'] #Recebe senha do HTML
        use= eval(PETinder.get_sync(point="/ListaUSER")) #Chama ListaUSER do firebase
        #Condições de cadastro do usuário:
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
            #Cadastro o novo usuário e manda as informações para o firebase
            USER.append(nomepessoa)
            USER[-1] = Pessoa(nome , nomepessoa, email, senha)
            USER[-1].Salvar_Pessoa() 
            PETinder.put_sync(point="/ListaUSER/{0}".format(nomepessoa),data=nomepessoa)                
            return render_template('home.html', dic = USER[-1].nomepessoa, nomepessoa = nomepessoa)

    return render_template('login.html', erro = '')
    
@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    #CADASTRO DE CÃES PARA ENCONTRAR PARCEIRO
    user=request.args['user'] #Chama o usuário que está logado  
    if request.method=='POST':

        nome = request.form['nome'] #Recebe nome do HTML
        raca = request.form['raca'] #Recebe raca do HTML
        sexo = request.form['sexo'] #Recebe sexo do HTML
        cidade = request.form['cidade'] #Recebe cidade do HTML
        idade = request.form['idade'] #Recebe idade do HTML
        cor = request.form['cor'] #Recebe cor do HTML
        saude = request.form['saude'] #Recebe saude do HTML
        use=eval(PETinder.get_sync(point="/ListadogBR")) #Chama a ListadogBR do firebase
        #Condições de cadastro do cão:
        if nome in use:
            e = 'Cão já cadastrado'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)
        elif nome == "":
            e = 'O campo Nome está vazio'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)
        elif raca == "":
            e = 'O campo Raça está vazio'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)       
        elif sexo == 0:
            e = 'O campo Sexo deve ser selecionado'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)        
        elif cidade == "":
            e = 'O campo Cidade está vazio'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)
        elif idade == "":
            e = 'O campo Idade está vazio'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)
        elif cor == "":
            e = 'O campo Cor está vazio'
            return render_template('cadastro.html', dic = PETinder.get_sync(point="/ListadogBR/{0}".format(nome)),nomepessoa = user, erro = e)
        else:
            #Cadastra o novo cão do usuário logado e manda as informações para o firebase
            NOME.append(nome)
            NOME[-1] = CaesBR(nome, raca, sexo, idade, cor, saude, cidade)
            NOME[-1].Salvar_CaesBR(user)
            return redirect(url_for('perfil', user=user))

    return render_template('cadastro.html',nomepessoa = user, erro = '')
    
    
    
@app.route('/caddoar', methods=['POST','GET'])
def caddoar():
    #CADASTRO DE CÃES PARA DOAR
    user=request.args['user']
    if request.method == 'POST':     
        nome = request.form['nome']
        raca = request.form['raca']
        sexo = request.form['sexo']
        cidade = request.form['cidade']
        idade = request.form['idade']
        cor = request.form['cor']
        saude = request.form['saude']
        use=eval(PETinder.get_sync(point="/ListadogBR"))
        if nome in use:
            e = 'Usuário já cadastrado'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)
        elif nome == "":
            e = 'O campo Nome está vazio'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)
        elif raca == "":
            e = 'O campo raca está vazio'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)       
        elif sexo == 0:
            e = 'O campo sexo deve ser selecionado'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)        
        elif cidade == "":
            e = 'O campo cidade está vazio'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)
        elif idade == "":
            e = 'O campo idade está vazio'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)
        elif cor == "":
            e = 'O campo cor está vazio'
            return render_template('caddoar.html', dic = PETinder.get_sync(point="/Listadogoar/{0}".format(nome)),nomepessoa = user, erro = e)
        else:
            NOME.append(nome)
            NOME[-1] = CaesDoar(nome, raca, sexo, idade, cor, saude, cidade)
            NOME[-1].Salvar_CaesDoar(user)
            return redirect(url_for('doar', user=user))
        
   
    return render_template('caddoar.html', nomepessoa = user, erro = '')
        
@app.route('/home', methods=['POST', 'GET'])
def home():
  
    button=request.form['button']
    user=request.args['user']
    
    
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
            cachorros=eval(PETinder.get_sync(point="/ListadogDoar"))
            sorte=random.choice(list(cachorros.keys()))    
            while (eval(PETinder.get_sync(point="/ListadogDoar/{0}/nomepessoa".format(sorte)))) == user:
                sorte=random.choice(list(cachorros.keys()))                
            return redirect(url_for('adotar', user=user, cao=sorte ))
            
    return render_template('home.html', nomepessoa = user)
        
@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    user=request.args['user']
    try:
        caesb= eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR".format(user)))
        listacaes=[]
        for j in caesb:
            caes=eval(PETinder.get_sync(point="/Pessoas/{0}/Caes_BR/{1}/nome".format(user, j)))
            listacaes.append(caes)
    #página que mostrará os animais cadastrados pelo usuário
            return render_template('perfil.html', nomepessoa=user, caesb=caesb)
    
    except:
        return render_template('perfil.html', nomepessoa=user)
    
@app.route('/doar', methods=['POST', 'GET'])
def doar():
    user=request.args['user']
    try:
        caesdoar= eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar".format(user)))
        listacaesd=[]
        for i in caesdoar:
            caesd=eval(PETinder.get_sync(point="/Pessoas/{0}/CaesDoar/{1}/nome".format(user, i)))
            listacaesd.append(caesd)
            #Listar_CaesDoar
            #página que mostrará os animais cadastrados pelo usuário para doação
            return render_template('doar.html', nomepessoa=user, caesdoar=caesdoar)
    except:
        return render_template('doar.html', nomepessoa = user)
        
@app.route('/opt', methods=['POST', 'GET'])
def opt():
    user=request.args['user']
    cachorros=(eval(PETinder.get_sync(point = "/ListadogBR")))
    sorte=random.choice(list(cachorros.keys()))
    while (eval(PETinder.get_sync(point="/ListadogBR/{0}/nomepessoa".format(sorte)))) == user:
                sorte=random.choice(list(cachorros.keys()))            
    
    caninos=(eval(PETinder.get_sync(point = "/ListadogBR/{0}".format(sorte))))
        
    return render_template('opt.html', cao = sorte, caninos = caninos, nomepessoa = user)
                
    
    
@app.route('/user', methods=['POST', 'GET'])
def usuario():
    user=request.args['user']
    cao = request.args['cao']
    name=eval(PETinder.get_sync(point="/ListadogBR/{0}".format(cao)))
    return render_template('user.html', user=user, cao=cao, name=name)
    
    
@app.route('/adotar', methods=['POST', 'GET'])
def adotar():
    user=request.args['user']
    cachorros=eval(PETinder.get_sync(point="/ListadogDoar"))
    sorte=random.choice(list(cachorros.keys()))
    while (eval(PETinder.get_sync(point="/ListadogDoar/{0}/nomepessoa".format(sorte)))) == user:
                sorte=random.choice(list(cachorros.keys()))            
    caesdoar= eval(PETinder.get_sync(point="/ListadogDoar/{0}".format(sorte)))
 
    return render_template('adotar.html', cao=sorte, caesdoar=caesdoar, user=user)
    
@app.route('/adote', methods=['POST', 'GET'])
def adote():
    user=request.args['user']
    cao = request.args['cao']
    name=eval(PETinder.get_sync(point="/ListadogDoar/{0}".format(cao)))
    return render_template('adote.html', user=user, cao=cao, name=name)

@app.route('/del', methods=['POST', 'GET']) 
def delete1():
    user=request.args['user']
    nome=request.args['nome']
#    Del_CaesBR(nome)
    Del_CaesDoar(nome)
    
    #apos finalizar o tratamento, volta para a pagina principal
    return redirect(url_for('doar', user=user))   
    
@app.route('/deld', methods=['POST', 'GET']) 
def delete2():
    user=request.args['user']
    nome=request.args['nome']
#    Del_CaesBR(nome)
    Del_CaesBR(nome)
    
    #apos finalizar o tratamento, volta para a pagina principal
    return redirect(url_for('perfil', user=user))  

@app.route('/delfinal', methods=['POST', 'GET']) 
def delete3():
    user=request.args['user']
    nome=request.args['nome']
    print ('chegou')
    
    print ('ta quase')
#    Del_CaesBR(nome)
    Del_CaesDoar(nome)
    
    #apos finalizar o tratamento, volta para a pagina principal
    return render_template('home.html', user=user)
        
        
@app.route('/deldfinal', methods=['POST', 'GET']) 
def delete4():
    user=request.args['user']
    nome=request.args['nome']
#    Del_CaesBR(nome)
    Del_CaesBR(nome)
    
    #apos finalizar o tratamento, volta para a pagina principal
    return render_template('home.html', user=user)
    
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)   
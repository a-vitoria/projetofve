## -*- coding: utf-8 -*-
#"""
#Created on Mon May  2 12:41:14 2016
#
#@author: Pessoa Prawita
#"""
import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")

dicionario={}
dicionariocaosex={}
dicionariocaodoa={}
class Pessoa():
    
    def __init__(self, nomepessoa, email, senha):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.dicionario=dicionario
        self.caosex=[]
        self.caodoa=[]
        
    def Salvar_Pessoa(self):
        dicionario["{0}".format(self.nomepessoa)]=self.nomepessoa,self.email,self.senha,self.caosex,self.caodoa
        return dicionario
        

        

class Caes():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
        self.nomepessoa=Pessoa.nomepessoa
        
        
class CaesBR(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)
    
    def Salvar_CaesBR(self):
        dicionariocaosex["{0}".format(self.nome)]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.nomepessoa
        Pessoa.dicionario["{0}".format(Pessoa.nomepessoa)][3].append(self.nome)
        return dicionariocaosex
#    def Listar_CaesBR(self):
        
        
class CaesDoar(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)

    def Salvar_CaesDoar(self):
        dicionariocaodoa["{0}".format(self.nome)]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.nomepessoa
        Pessoa.dicionario["{0}".format(Pessoa.nomepessoa)][4].append(self.nome)
        return dicionariocaodoa
#    def Listar_CaesDoar(self):
        

#Pessoa=Pessoa("Pessoa","edu.tirta@gmail.com",0000)
#Pessoa.Salvar_Pessoa()

#Lucas=CaesBR("Lucas","Masculino","York","Preto","14","Castrado","Mogi")
#Lucas.Salvar_CaesBR()


PETinder.put(point="/Pessoas",data=dicionario)
PETinder.put(point="/Caes_BR",data=dicionariocaosex)
PETinder.put(point="/Caes_Doar",data=dicionariocaodoa)


#print(Pessoa)
## -*- coding: utf-8 -*-
#"""
#Created on Mon May  2 12:41:14 2016
#
#@author: Pessoa Prawita
#"""
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
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
        self.email=Pessoa.email
        self.dicionariocaosex={}
        self.dicionariocaodoa={}
        
        
class CaesBR(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)
    
    def Salvar_CaesBR(self):
        self.dicionariocaosex[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.email
        Pessoa.dicionario[Pessoa.email][3].append(self.email)
        dogBR.append(self.nome)        
        return self.dicionariocaosex
#    def Listar_CaesBR(self):
        
        
class CaesDoar(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)

    def Salvar_CaesDoar(self):
        self.dicionariocaodoa[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.email
        (Pessoa.email).dicionario[Pessoa.email][4].append(self.email)
        dogDoar.append(self.nome)
        return self.dicionariocaodoa
#    def Listar_CaesDoar(self):
        

#Pessoa=Pessoa("Pessoa","edu.tirta@gmail.com","0000")
#Pessoa.Salvar_Pessoa()

#Lucas=CaesBR("Lucas","Masculino","York","Preto","14","Castrado","Mogi")
#Lucas.Salvar_CaesBR()


PETinder.put(point="/Pessoas",data=Pessoa.dicionario)
PETinder.put(point="/Caes_BR",data=CaesBR.dicionariocaosex)
PETinder.put(point="/Caes_Doar",data=CaesDoar.dicionariocaodoa)
PETinder.put(point="/ListadogBR",data=dogBR)
PETinder.put(point="/ListadogDoar",data=dogDoar)
PETinder.put(point="/ListaEMAIL",data=EMAIL)


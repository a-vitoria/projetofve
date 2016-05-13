## -*- coding: utf-8 -*-
#"""
#Created on Mon May  2 12:41:14 2016
#
#@author: Pessoa Prawita
#"""
import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")
people=[]
dogBR=[]
dogDoar=[]

class Pessoa():
    
    def __init__(self, nomepessoa, email, senha):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.dicionario={}
        self.caosex=[]
        self.caodoa=[]
        
    def Salvar_Pessoa(self):
        self.dicionario[self.nomepessoa]=self.nomepessoa,self.email,self.senha,self.caosex,self.caodoa
        people.append(self.nomepessoa)        
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
        self.nomepessoa=Eduardo.nomepessoa
        self.dicionariocaosex={}
        self.dicionariocaodoa={}
        
        
class CaesBR(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)
    
    def Salvar_CaesBR(self):
        self.dicionariocaosex[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Eduardo.nomepessoa
        Eduardo.dicionario[Eduardo.nomepessoa][3].append(self.nome)
        dogBR.append(self.nome)        
        return self.dicionariocaosex
#    def Listar_CaesBR(self):
        
        
class CaesDoar(Caes):
    def __init__(self,nome,sexo,raca,cor,idade,saude,cidade):
        Caes.__init__(self,nome,sexo,raca,cor,idade,saude,cidade)

    def Salvar_CaesDoar(self):
        self.dicionariocaodoa[self.nome]=self.nome,self.sexo,self.raca,self.cor,self.idade,self.saude,self.cidade,Pessoa.nomepessoa
        (Pessoa.nomepessoa).dicionario[Pessoa.nomepessoa][4].append(self.nome)
        dogDoar.append(self.nome)
        return self.dicionariocaodoa
#    def Listar_CaesDoar(self):
        

Eduardo=Pessoa("Eduardo","edu.tirta@gmail.com","0000")
Eduardo.Salvar_Pessoa()

Lucas=CaesBR("Lucas","Masculino","York","Preto","14","Castrado","Mogi")
Lucas.Salvar_CaesBR()


PETinder.put(point="/Pessoas",data=Eduardo.dicionario)
PETinder.put(point="/Caes_BR",data=Lucas.dicionariocaosex)
#PETinder.put(point="/Caes_Doar",data=Lucas.dicionariocaodoa)


#print(Pessoa)
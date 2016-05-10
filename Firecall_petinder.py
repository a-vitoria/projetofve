## -*- coding: utf-8 -*-
#"""
#Created on Mon May  2 12:41:14 2016
#
#@author: Eduardo Prawita
#"""
import firecall
#
PETinder=firecall.Firebase("https://petinder.firebaseio.com/")

pessoas={}
caes={}

class Pessoa():
    
    def __init__(self, nomepessoa, email, senha):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
#    def Salvar_Pessoa(self):


class Caes():
    
    def __init__(self, nome, sexo, raca, cor, idade, saude, cidade):
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.saude = saude
        self.cidade = cidade
    #    def Salvar_Caes(self):

Pessoa.nomepessoa=input('Nome?')
Pessoa.email=input('Email?')
Pessoa.senha=input('Senha?')

Caes.nome = input('nome?')
Caes.sexo = input('sexo?')
Caes.raca = input('raca?')
Caes.cor = input('cor?')
Caes.idade =input('idade?')
Caes.saude =input('saude?')
Caes.cidade =input('cidade?')
dicionario = {"Nome" : Pessoa.nomepessoa, "Nome de usuario" : Pessoa.nomepessoa, "Email" : Pessoa.email, "Senha" : Pessoa.senha,"Cães":Caes}
#Lucas=Caes("Lucas","masculino","york","preto","14","castrado","mogi")
dicionariocao={'nome':Caes.nome,'sexo':Caes.sexo,'raca':Caes.raca,'cor':Caes.cor,'idade':Caes.idade,'saude':Caes.saude,'cidade':Caes.cidade}

PETinder.put(point="/Pessoas",data=dicionario)


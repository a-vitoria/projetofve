## -*- coding: utf-8 -*-
#"""
#Created on Mon May  2 12:41:14 2016
#
#@author: Eduardo Prawita
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
    def Salvar_Pessoa(self):
        dicionario["Nome"]=self.nomepessoa
        dicionario["Email"]=self.email
        dicionario["Senha"]=self.senha
        dicionario["CaesBR"]=dicionariocaosex
        dicionario["CaesDoar"]=dicionariocaodoa
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

class CaesBR(Caes):
    def Salvar_Caes(self):
        def Salvar_Caes(self):
            dicionariocaosex["Nome"]=self.nome
            dicionariocaosex["Sexo"]=self.sexo
            dicionariocaosex["Raca"]=self.raca
            dicionariocaosex["Cor"]=self.cor
            dicionariocaosex["Idade"]=self.idade
            dicionariocaosex["Saude"]=self.saude
            dicionariocaosex["Cidade"]=self.cidade
            return dicionariocaosex
class CaesDoar(Caes):
    def Salvar_Caes(self):
        def Salvar_Caes(self):
            dicionariocaodoa["Nome"]=self.nome
            dicionariocaodoa["Sexo"]=self.sexo
            dicionariocaodoa["Raca"]=self.raca
            dicionariocaodoa["Cor"]=self.cor
            dicionariocaodoa["Idade"]=self.idade
            dicionariocaodoa["Saude"]=self.saude
            dicionariocaodoa["Cidade"]=self.cidade
            return dicionariocaodoa
PETinder.put(point="/Pessoas",data=dicionario)


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
    
    def __init__(self, nomepessoa, email, senha, Caes):
        self.nomepessoa = nomepessoa
        self.email = email
        self.senha = senha
        self.caes = Caes
        self.dic={}
    def dicionario(self):
        dic={self.nomepessoa:[self.nomepessoa,self.email,self.senha,self.Caes]}
        return dic
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

Eduardo_Tirta=Pessoa('Eduardo Tirta Prawita','edu.tirta@gmail.com','0000','Lucas')       

#Lucas=Caes("Lucas","masculino","york","preto","14","castrado","mogi")


PETinder.put(point="/Cadastro das pessoas",data=Pessoa)



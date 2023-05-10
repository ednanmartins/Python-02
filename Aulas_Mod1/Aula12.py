# Aula 12 - Classes Abstratas

from abc import ABC, abstractclassmethod


class letras:
    @abstractclassmethod
    def mostrarTipo(self):
        print("Eu sou uma classe abstrata!")


class A(letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print("Aqui é um metodo diferente!")


letraa = A("Letra A")
letraa.mostrarTipo()
letraa.imprimir()
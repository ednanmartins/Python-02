"""EXERCÍCIO PRÁTICO

Crie uma classe animal com atributos e métodos, posteriormente, crie uma 
classe que herde seus atributos, e possuía os seus atributos próprios. 

Crie dois objetos da classe filha."""


class Animal:
    def __init__(self, nome, patas, rabo):
        self.nome = nome
        self.patas = patas
        self.rabo = rabo

    def aumenta_patas(self):
        self.patas += 1

    def diminui_patas(self):
        self.patas -= 1


class Ave(Animal):
    def __init__(self, nome, patas, rabo, asas):
        super().__init__(nome, patas, rabo)
        self.asas = asas


animal1 = Animal("Dog", 4, 1)
print(vars(animal1))

animal1.aumenta_patas
print(vars(animal1))

animal1.diminui_patas
print(vars(animal1))

animal2 = Ave("Papagaio", 2, 1, 2)
print(vars(animal2))

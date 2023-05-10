# Aula 08 - Correção do Exercicio


class Animal:
    def __init__(self, nome, porte):
        self.nome = nome
        self.porte = porte


class Gato(Animal):
    def __init__(self, nome, porte, som):
        super().__init__(nome, porte)
        self.som = som


lex = Gato("Lex", "Médio", "Mia")
lala = Gato("Lala", "Pequeno", "Mia")

print(vars(lex))
print(vars(lala))

# Aula 05 Atributos e métodos:


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_salario(self):
        print("Meu salário é: ", self._salario)

    def get_bonificacao(self):
        return self._salario * 0.15


f = Funcionario("José", "45678998788", 5000.59)
f.get_salario()
print(f.get_bonificacao())

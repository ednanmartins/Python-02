# Aula 03 -  Objetos:


class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Aviao:
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano


v = Veiculo("carro", "9BGRD08X04G117974", "Ferrari", "F112", "2017")
a = Aviao("Carga", "Quadrimotor", "SoulCode Airlines", "Airbus A380", "2010")

print(vars(v))
print(vars(a))

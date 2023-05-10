# Aula 07 - Herança:


class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada


v = Veiculo("carro", "9BGRD08X04G117974", "Ferrari", "F112", "2017")
m = Motocicleta("motocicleta", "5AZKG01Z12A339037", "Honda", "CG", "2015", 150)
print(vars(v))
print(vars(m))

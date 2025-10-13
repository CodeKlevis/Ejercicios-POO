import math

class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcular_promedio(self):
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += self.listaNotas[i]
        return suma / len(self.listaNotas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += (self.listaNotas[i] - prom) ** 2
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        menor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] < menor:
                menor = self.listaNotas[i]
        return menor

    def calcular_mayor(self):
        mayor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] > mayor:
                mayor = self.listaNotas[i]
        return mayor

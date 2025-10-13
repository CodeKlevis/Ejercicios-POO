import math
from FiguraGeometrica import FiguraGeometrica

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4.0 * math.pi * (self.radio ** 2)

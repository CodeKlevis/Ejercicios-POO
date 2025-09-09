"""Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo. """

def Cuadrado_y_cubo(Numero):
    Cuadrado = Numero ** 2
    Cubo = Numero ** 3
    return Cuadrado, Cubo

Numero = int(input("Introduce un número:"))
Cuadrado, Cubo = Cuadrado_y_cubo(Numero)
print ("El Cuadrado de", Numero, "es:", Cuadrado)
print ("El Cubo de", Numero, "es:", Cubo)
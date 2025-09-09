"""Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud
de la circunferencia."""

def Area_y_Longitud(Radio):
    Area = 3.1416 * Radio ** 2
    Longitud = 2 * 3.1416 * Radio
    return Area, Longitud
Radio = float(input("Introduce el radio del círculo:"))
Area, Longitud = Area_y_Longitud(Radio)
print ("El Área del círculo es:", Area)
print ("La Longitud de la circunferencia es:", Longitud)

import tkinter as tk
from VentanaCilindro import VentanaCilindro
from VentanaEsfera import VentanaEsfera
from VentanaPiramide import VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)

        boton_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        boton_cilindro.place(x=20, y=50, width=80)

        boton_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        boton_esfera.place(x=125, y=50, width=80)

        boton_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        boton_piramide.place(x=225, y=50, width=100)

    def abrir_cilindro(self):
        VentanaCilindro().grab_set()

    def abrir_esfera(self):
        VentanaEsfera().grab_set()

    def abrir_piramide(self):
        VentanaPiramide().grab_set()

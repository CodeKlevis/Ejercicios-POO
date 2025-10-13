import tkinter as tk
from tkinter import messagebox
from Esfera import Esfera

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20)

        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=100, y=50)

        self.volumen = tk.Label(self, text="Volumen (cm³):")
        self.volumen.place(x=20, y=90)

        self.superficie = tk.Label(self, text="Superficie (cm²):")
        self.superficie.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.volumen.config(text=f"Volumen (cm³): {esfera.calcular_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm²): {esfera.calcular_superficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

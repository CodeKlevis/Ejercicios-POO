import tkinter as tk
from tkinter import messagebox
from Piramide import Piramide

class VentanaPiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80)

        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=120, y=110)

        self.volumen = tk.Label(self, text="Volumen (cm³):")
        self.volumen.place(x=20, y=140)

        self.superficie = tk.Label(self, text="Superficie (cm²):")
        self.superficie.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.volumen.config(text=f"Volumen (cm³): {piramide.calcular_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm²): {piramide.calcular_superficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

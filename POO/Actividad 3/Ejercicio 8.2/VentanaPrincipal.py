import tkinter as tk
from Notas import Notas

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Notas")
        self.ventana.geometry("280x380")
        self.ventana.resizable(False, False)
        self.ventana.eval('tk::PlaceWindow . center')

        self.nota_labels = []
        self.campos_notas = []
        for i in range(5):
            lbl = tk.Label(self.ventana, text=f"Nota {i+1}:")
            lbl.place(x=20, y=20 + i*30)
            self.nota_labels.append(lbl)

            entry = tk.Entry(self.ventana)
            entry.place(x=105, y=20 + i*30, width=135)
            self.campos_notas.append(entry)

        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=20, y=170, width=100)

        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=125, y=170, width=80)

        self.lbl_promedio = tk.Label(self.ventana, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=210)

        self.lbl_desviacion = tk.Label(self.ventana, text="Desviación = ")
        self.lbl_desviacion.place(x=20, y=240)

        self.lbl_mayor = tk.Label(self.ventana, text="Nota mayor = ")
        self.lbl_mayor.place(x=20, y=270)

        self.lbl_menor = tk.Label(self.ventana, text="Nota menor = ")
        self.lbl_menor.place(x=20, y=300)

    def calcular(self):
        notas = Notas()
        for i in range(5):
            try:
                notas.listaNotas[i] = float(self.campos_notas[i].get())
            except ValueError:
                notas.listaNotas[i] = 0.0

        promedio = notas.calcular_promedio()
        desviacion = notas.calcular_desviacion()
        mayor = notas.calcular_mayor()
        menor = notas.calcular_menor()

        self.lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
        self.lbl_mayor.config(text=f"Nota mayor = {mayor:.2f}")
        self.lbl_menor.config(text=f"Nota menor = {menor:.2f}")

    def limpiar(self):
        for entry in self.campos_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")

    def iniciar(self):
        self.ventana.mainloop()

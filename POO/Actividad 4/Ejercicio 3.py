import math
import tkinter as tk
from tkinter import messagebox

class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)

def calcular():
    try:
        valor = float(entry_valor.get())
        log = CalculosNumericos.logaritmo_neperiano(valor)
        raiz = CalculosNumericos.raiz_cuadrada(valor)
        messagebox.showinfo(
            "Resultados",
            f"Resultados para {valor}:\n\n"
            f"Logaritmo neperiano: {log:.4f}\n"
            f"Raíz cuadrada: {raiz:.4f}"
        )
    except ValueError:
        messagebox.showerror("Error", "El valor ingresado no es un número válido.")
    except ArithmeticError as e:
        messagebox.showwarning("Error aritmético", f"{e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Se produjo un error: {e}")
    finally:
        entry_valor.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Cálculos Numéricos")
ventana.geometry("350x180")
ventana.resizable(False, False)

label = tk.Label(ventana, text="Ingrese un número positivo:", font=("Arial", 12))
label.pack(pady=10)

entry_valor = tk.Entry(ventana, font=("Arial", 12), justify="center")
entry_valor.pack(pady=5)

btn_calcular = tk.Button(ventana, text="Calcular", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", command=calcular)
btn_calcular.pack(pady=10)

label_pie = tk.Label(ventana, text="Ejercicio 6.6 - Manejo de Excepciones", font=("Arial", 9), fg="gray")
label_pie.pack(side="bottom", pady=5)

ventana.mainloop()

import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_equipo = 0

    def esta_lleno(self):
        return self.tamano_equipo == 3

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Maratón de Programación")

        self.equipo = None
        self.contador = 0

        self.frame_equipo = tk.Frame(root)
        self.frame_equipo.pack(padx=10, pady=10)

        tk.Label(self.frame_equipo, text="Nombre del equipo:").grid(row=0, column=0)
        self.nombre_equipo = tk.Entry(self.frame_equipo)
        self.nombre_equipo.grid(row=0, column=1)

        tk.Label(self.frame_equipo, text="Universidad:").grid(row=1, column=0)
        self.universidad = tk.Entry(self.frame_equipo)
        self.universidad.grid(row=1, column=1)

        tk.Label(self.frame_equipo, text="Lenguaje de programación:").grid(row=2, column=0)
        self.lenguaje = tk.Entry(self.frame_equipo)
        self.lenguaje.grid(row=2, column=1)

        tk.Button(self.frame_equipo, text="Crear equipo", command=self.crear_equipo).grid(row=3, column=0, columnspan=2, pady=5)

        self.frame_integrantes = tk.Frame(root)

    def crear_equipo(self):
        try:
            nombre = self.nombre_equipo.get().strip()
            universidad = self.universidad.get().strip()
            lenguaje = self.lenguaje.get().strip()

            if not nombre or not universidad or not lenguaje:
                raise Exception("Todos los campos son obligatorios.")

            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(universidad)
            EquipoMaratonProgramacion.validar_campo(lenguaje)

            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
            self.frame_equipo.pack_forget()
            self.mostrar_formulario_integrantes()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_formulario_integrantes(self):
        self.frame_integrantes.pack(padx=10, pady=10)

        tk.Label(self.frame_integrantes, text=f"Integrante {self.contador + 1}").grid(row=0, column=0, columnspan=2)

        tk.Label(self.frame_integrantes, text="Nombre:").grid(row=1, column=0)
        self.nombre_integrante = tk.Entry(self.frame_integrantes)
        self.nombre_integrante.grid(row=1, column=1)

        tk.Label(self.frame_integrantes, text="Apellidos:").grid(row=2, column=0)
        self.apellidos_integrante = tk.Entry(self.frame_integrantes)
        self.apellidos_integrante.grid(row=2, column=1)

        tk.Button(self.frame_integrantes, text="Agregar integrante", command=self.agregar_integrante).grid(row=3, column=0, columnspan=2, pady=5)

    def agregar_integrante(self):
        try:
            nombre = self.nombre_integrante.get().strip()
            apellidos = self.apellidos_integrante.get().strip()

            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)

            programador = Programador(nombre, apellidos)
            self.equipo.anadir(programador)
            self.contador += 1

            if self.contador < 3:
                self.nombre_integrante.delete(0, tk.END)
                self.apellidos_integrante.delete(0, tk.END)
                tk.Label(self.frame_integrantes, text=f"Integrante {self.contador + 1}").grid(row=0, column=0, columnspan=2)
            else:
                self.mostrar_resumen()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resumen(self):
        self.frame_integrantes.pack_forget()

        resumen = tk.Frame(self.root)
        resumen.pack(padx=10, pady=10)

        tk.Label(resumen, text="Equipo creado exitosamente", font=("Arial", 12, "bold")).pack()
        tk.Label(resumen, text=f"Nombre del equipo: {self.equipo.nombre_equipo}").pack()
        tk.Label(resumen, text=f"Universidad: {self.equipo.universidad}").pack()
        tk.Label(resumen, text=f"Lenguaje: {self.equipo.lenguaje_programacion}").pack()
        tk.Label(resumen, text="Integrantes:").pack()

        for p in self.equipo.programadores:
            tk.Label(resumen, text=f"- {p.nombre} {p.apellidos}").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

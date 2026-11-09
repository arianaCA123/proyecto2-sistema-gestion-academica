# Esta ventana llama a estos métodos del controlador:
#   registrar_estudiante, consultar_estudiante, modificar_estudiante y eliminar_estudiante
# Desde la ventana principal se abre con: self.controlador.abrir_estudiantes(self.raiz)

import tkinter as tk
from tkinter import ttk, messagebox     # ttk tiene el Combobox y el Treeview


class EstudianteVista:
    
    # Constructor: arma la ventana.
    # Recibe la ventana principal (ventana_padre) y el controlador.
    
    def __init__(self, ventana_padre, controlador):
        self.controlador = controlador

        # Toplevel = ventana secundaria
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Gestión de estudiantes")

        # Campos del formulario: un Label con el texto y un Entry para escribir
        tk.Label(self.ventana, text="Carné:").grid(row=0, column=0, padx=10, pady=5)
        self.txt_carnet = tk.Entry(self.ventana, width=30)
        self.txt_carnet.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        tk.Label(self.ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.txt_nombre = tk.Entry(self.ventana, width=30)
        self.txt_nombre.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

        tk.Label(self.ventana, text="Fecha nacimiento (dd/mm/aaaa):").grid(row=2, column=0, padx=10, pady=5)
        self.txt_edad = tk.Entry(self.ventana, width=30)
        self.txt_edad.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        # Combobox: lista desplegable para elegir la carrera
        tk.Label(self.ventana, text="Carrera:").grid(row=3, column=0, padx=10, pady=5)
        self.cmb_carrera = ttk.Combobox(self.ventana, width=27,
                                        values=["Informática Empresarial", "Administración de Empresas",
                                                "Contaduría Pública", "Turismo Ecológico", "Inglés"])
        self.cmb_carrera.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        tk.Label(self.ventana, text="Correo:").grid(row=4, column=0, padx=10, pady=5)
        self.txt_correo = tk.Entry(self.ventana, width=30)
        self.txt_correo.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

        # Botones: command es el método que se ejecuta al hacer clic (va sin paréntesis)
        tk.Button(self.ventana, text="Registrar", width=10, command=self.registrar).grid(row=5, column=0, pady=10)
        tk.Button(self.ventana, text="Consultar", width=10, command=self.consultar).grid(row=5, column=1, pady=10)
        tk.Button(self.ventana, text="Modificar", width=10, command=self.modificar).grid(row=5, column=2, pady=10)
        tk.Button(self.ventana, text="Eliminar", width=10, command=self.eliminar).grid(row=5, column=3, pady=10)
        tk.Button(self.ventana, text="Limpiar", width=10, command=self.limpiar).grid(row=5, column=4, pady=10)
        tk.Button(self.ventana, text="Cerrar", width=10, command=self.ventana.destroy).grid(row=5, column=5, pady=10)

        # Tabla (Treeview) para listar los estudiantes registrados
        self.tabla = ttk.Treeview(self.ventana, columns=("carnet", "nombre", "fecha", "carrera", "correo"),
                                  show="headings")
        self.tabla.heading("carnet", text="Carné")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("fecha", text="Fecha nac.")
        self.tabla.heading("carrera", text="Carrera")
        self.tabla.heading("correo", text="Correo")
        self.tabla.grid(row=6, column=0, columnspan=6, padx=10, pady=10)

    # ---------- Botones: leen los campos con .get() y llaman al controlador ----------

    def registrar(self):
        self.controlador.registrar_estudiante(self.txt_carnet.get(), self.txt_nombre.get(),
                                              self.txt_edad.get(), self.cmb_carrera.get(),
                                              self.txt_correo.get())

    # Para consultar solo hace falta el carné
    def consultar(self):
        self.controlador.consultar_estudiante(self.txt_carnet.get())

    # Primero se consulta (llena los campos), se cambian los datos y luego se modifica
    def modificar(self):
        self.controlador.modificar_estudiante(self.txt_carnet.get(), self.txt_nombre.get(),
                                              self.txt_edad.get(), self.cmb_carrera.get(),
                                              self.txt_correo.get())

    # Pide confirmación antes de eliminar (askyesno devuelve True si se presiona "Sí")
    def eliminar(self):
        if messagebox.askyesno("Confirmar", "¿Desea eliminar este estudiante?"):
            self.controlador.eliminar_estudiante(self.txt_carnet.get())

    # ---------- Métodos que usa el controlador para mostrar cosas ----------

    # Borra lo escrito en todos los campos
    def limpiar(self):
        self.txt_carnet.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_edad.delete(0, tk.END)
        self.cmb_carrera.set("")
        self.txt_correo.delete(0, tk.END)

    # Pone los datos del estudiante consultado en los campos
    def llenar_campos(self, estudiante):
        self.limpiar()
        self.txt_carnet.insert(0, estudiante.get_carnet())
        self.txt_nombre.insert(0, estudiante.get_nombre())
        self.txt_edad.insert(0, estudiante.get_edad())
        self.cmb_carrera.set(estudiante.get_carrera())
        self.txt_correo.insert(0, estudiante.get_correo())

    # Borra todas las filas de la tabla y la vuelve a llenar con la lista
    def mostrar_tabla(self, estudiantes):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for estudiante in estudiantes:
            self.tabla.insert("", tk.END, values=(estudiante.get_carnet(), estudiante.get_nombre(),
                                                  estudiante.get_edad(), estudiante.get_carrera(),
                                                  estudiante.get_correo()))

    # Muestra cualquier mensaje que le envíe el controlador (de éxito o de error)
    def mostrar_mensaje(self, texto):
        messagebox.showinfo("Información", texto)
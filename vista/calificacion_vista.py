import tkinter as tk
from tkinter import ttk, messagebox     # ttk tiene el Combobox y el Treeview


class CalificacionVista:
    def __init__(self, ventana_padre):
        self.__ventana = tk.Toplevel(ventana_padre)
        self.__ventana.title("Géstion de calificaciones")
        self.__ventana.resizable(False, False)

        tk.Label(self.__ventana, text="Registro de calificaciones", font=("Arial", 15, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(15, 10)
        )

        # Combobox de solo lectura (state="readonly"): el usuario elige de la lista y no puede escribir.
        # El controlador llena sus opciones con los estudiantes y cursos ya registrados.
        tk.Label(self.__ventana, text="Carné del estudiante:").grid(row=1, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__combo_carnet = ttk.Combobox(self.__ventana, width=32, state="readonly")
        self.__combo_carnet.grid(row=1, column=1, sticky="w")

        tk.Label(self.__ventana, text="Curso:").grid(row=2, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__combo_curso = ttk.Combobox(self.__ventana, width=32, state="readonly")
        self.__combo_curso.grid(row=2, column=1, sticky="w")

        tk.Label(self.__ventana, text="Nota:").grid(row=3, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__entrada_nota = tk.Entry(self.__ventana, width=35)
        self.__entrada_nota.grid(row=3, column=1, sticky="w")

        # El período se divide en ciclo (lista con opciones fijas) y año (se escribe)
        tk.Label(self.__ventana, text="Ciclo:").grid(row=4, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__combo_ciclo = ttk.Combobox(self.__ventana, width=32, state="readonly",
                                          values=["I", "II", "III"])
        self.__combo_ciclo.grid(row=4, column=1, sticky="w")

        tk.Label(self.__ventana, text="Año:").grid(row=5, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__entrada_annio = tk.Entry(self.__ventana, width=35)
        self.__entrada_annio.grid(row=5, column=1, sticky="w")

        marco_botones = tk.Frame(self.__ventana)
        marco_botones.grid(row=6, column=0, columnspan=2, pady=(15, 10))

        self.__boton_guardar = tk.Button(marco_botones, text="Guardar", width=9)
        self.__boton_guardar.grid(row=0, column=0, padx=3)
        self.__boton_consultar = tk.Button(marco_botones, text="Consultar", width=9)
        self.__boton_consultar.grid(row=0, column=1, padx=3)
        self.__boton_modificar = tk.Button(marco_botones, text="Modificar", width=9)
        self.__boton_modificar.grid(row=0, column=2, padx=3)
        self.__boton_eliminar = tk.Button(marco_botones, text="Eliminar", width=9)
        self.__boton_eliminar.grid(row=0, column=3, padx=3)
        self.__boton_limpiar = tk.Button(marco_botones, text="Limpiar", width=9)
        self.__boton_limpiar.grid(row=0, column=4, padx=3)
        self.__boton_salir = tk.Button(marco_botones, text="Salir", width=9)
        self.__boton_salir.grid(row=0, column=5, padx=3)

        self.__tabla = ttk.Treeview(self.__ventana, columns=("carnet", "nombre", "curso", "nota", "periodo"),
                                    show="headings", height=8)
        self.__tabla.heading("carnet", text="Carné")
        self.__tabla.heading("nombre", text="Nombre del estudiante")
        self.__tabla.heading("curso", text="Curso")
        self.__tabla.heading("nota", text="Nota")
        self.__tabla.heading("periodo", text="Período")
        self.__tabla.column("carnet", width=90)
        self.__tabla.column("nombre", width=180)
        self.__tabla.column("curso", width=170)
        self.__tabla.column("nota", width=60)
        self.__tabla.column("periodo", width=90)
        self.__tabla.grid(row=7, column=0, columnspan=2, padx=20, pady=(5, 15))

        self.__combo_carnet.focus()

    # El controlador le entrega los métodos que se ejecutan al presionar cada botón.
    # command=guardar va SIN paréntesis: se pasa el método, no se ejecuta todavía.
    def configurar_eventos(self, guardar, consultar, modificar, eliminar, limpiar, salir):
        self.__boton_guardar.config(command=guardar)
        self.__boton_consultar.config(command=consultar)
        self.__boton_modificar.config(command=modificar)
        self.__boton_eliminar.config(command=eliminar)
        self.__boton_limpiar.config(command=limpiar)
        self.__boton_salir.config(command=salir)
        self.__ventana.protocol("WM_DELETE_WINDOW", salir)      # al cerrar con la X

    def cargar_carnets(self, carnets):
        self.__combo_carnet.config(values=carnets)

    def cargar_cursos(self, codigos):
        self.__combo_curso.config(values=codigos)

    def obtener_carnet(self):
        return self.__combo_carnet.get().strip()

    def obtener_curso(self):
        return self.__combo_curso.get().strip()

    def obtener_nota(self):
        return self.__entrada_nota.get().strip()

    def obtener_ciclo(self):
        return self.__combo_ciclo.get().strip()

    def obtener_annio(self):
        return self.__entrada_annio.get().strip()

    # Pone los datos de la calificación consultada en los campos.
    # En los Combobox se usa set() y en los Entry se usa insert().
    def mostrar_calificacion(self, calificacion):
        self.limpiar_campos()
        self.__combo_carnet.set(calificacion.get_carnet_estudiante())
        self.__combo_curso.set(calificacion.get_codigo_curso())
        self.__entrada_nota.insert(0, calificacion.get_nota())
        self.__combo_ciclo.set(calificacion.get_ciclo())
        self.__entrada_annio.insert(0, calificacion.get_annio())

    # Recibe dos diccionarios ({carnet: nombre} y {codigo: nombre}) porque la calificación
    # solo guarda el carnet y el código, y la tabla muestra también los nombres.
    def mostrar_tabla(self, calificaciones, nombres_estudiantes, nombres_cursos):
        for fila in self.__tabla.get_children():
            self.__tabla.delete(fila)

        for calificacion in calificaciones:
            carnet = calificacion.get_carnet_estudiante()
            codigo = calificacion.get_codigo_curso()
            self.__tabla.insert("", tk.END, values=(carnet, nombres_estudiantes.get(carnet, ""),
                                                    nombres_cursos.get(codigo, codigo), calificacion.get_nota(),
                                                    str(calificacion.get_ciclo()) + "-" + str(calificacion.get_annio())))

    def limpiar_campos(self):
        self.__combo_carnet.set("")
        self.__combo_curso.set("")
        self.__entrada_nota.delete(0, tk.END)
        self.__combo_ciclo.set("")
        self.__entrada_annio.delete(0, tk.END)
        self.__combo_carnet.focus()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    # askyesno devuelve True si el usuario presiona "Sí"
    def confirmar_eliminacion(self):
        return messagebox.askyesno("Confirmación", "¿Desea eliminar esta calificación?")

    def salir(self):
        self.__ventana.destroy()
import tkinter as tk
from tkinter import ttk, messagebox     # ttk tiene el Combobox y el Treeview


class EstudianteVista:
    # Constructor: arma la ventana. Recibe la ventana principal (ventana_padre).
    def __init__(self, ventana_padre):
        # Toplevel = ventana secundaria
        self.__ventana = tk.Toplevel(ventana_padre)
        self.__ventana.title("Gestión de estudiantes")
        self.__ventana.resizable(False, False)

        tk.Label(self.__ventana, text="Registro de estudiantes", font=("Arial", 15, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(15, 10)
        )

        # Campos del formulario: un Label con el texto y un Entry para escribir
        tk.Label(self.__ventana, text="Carné:").grid(row=1, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__entrada_carnet = tk.Entry(self.__ventana, width=35)
        self.__entrada_carnet.grid(row=1, column=1, sticky="w")

        tk.Label(self.__ventana, text="Nombre:").grid(row=2, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__entrada_nombre = tk.Entry(self.__ventana, width=35)
        self.__entrada_nombre.grid(row=2, column=1, sticky="w")

        tk.Label(self.__ventana, text="Fecha nacimiento (dd/mm/aaaa):").grid(
            row=3, column=0, padx=(20, 10), pady=5, sticky="e"
        )
        self.__entrada_edad = tk.Entry(self.__ventana, width=35)
        self.__entrada_edad.grid(row=3, column=1, sticky="w")

        # Combobox: lista desplegable para elegir la carrera
        tk.Label(self.__ventana, text="Carrera:").grid(row=4, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__combo_carrera = ttk.Combobox(
            self.__ventana,
            width=32,
            values=["Informática Empresarial", "Administración de Empresas",
                    "Contaduría Pública", "Turismo Ecológico", "Inglés"]
        )
        self.__combo_carrera.grid(row=4, column=1, sticky="w")

        tk.Label(self.__ventana, text="Correo:").grid(row=5, column=0, padx=(20, 10), pady=5, sticky="e")
        self.__entrada_correo = tk.Entry(self.__ventana, width=35)
        self.__entrada_correo.grid(row=5, column=1, sticky="w")

        # Frame: contenedor para acomodar los botones en una sola fila
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

        # Tabla (Treeview) para listar los estudiantes registrados
        self.__tabla = ttk.Treeview(self.__ventana, columns=("carnet", "nombre", "fecha", "carrera", "correo"),
                                    show="headings", height=8)
        self.__tabla.heading("carnet", text="Carné")
        self.__tabla.heading("nombre", text="Nombre")
        self.__tabla.heading("fecha", text="Fecha nac.")
        self.__tabla.heading("carrera", text="Carrera")
        self.__tabla.heading("correo", text="Correo")
        self.__tabla.column("carnet", width=90)
        self.__tabla.column("nombre", width=180)
        self.__tabla.column("fecha", width=90)
        self.__tabla.column("carrera", width=170)
        self.__tabla.column("correo", width=180)
        self.__tabla.grid(row=7, column=0, columnspan=2, padx=20, pady=(5, 15))

        self.__entrada_carnet.focus()

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

    # ---------- Leer lo que escribió el usuario (get devuelve texto; strip quita espacios) ----------

    def obtener_carnet(self):
        return self.__entrada_carnet.get().strip()

    def obtener_nombre(self):
        return self.__entrada_nombre.get().strip()

    def obtener_edad(self):
        return self.__entrada_edad.get().strip()

    def obtener_carrera(self):
        return self.__combo_carrera.get().strip()

    def obtener_correo(self):
        return self.__entrada_correo.get().strip()

    # ---------- Mostrar cosas en la ventana ----------

    # Pone los datos del estudiante consultado en los campos
    def mostrar_estudiante(self, estudiante):
        self.limpiar_campos()
        self.__entrada_carnet.insert(0, estudiante.get_carnet())
        self.__entrada_nombre.insert(0, estudiante.get_nombre())
        self.__entrada_edad.insert(0, estudiante.get_edad())
        self.__combo_carrera.set(estudiante.get_carrera())
        self.__entrada_correo.insert(0, estudiante.get_correo())

    # Borra todas las filas de la tabla y la vuelve a llenar con la lista
    def mostrar_tabla(self, estudiantes):
        for fila in self.__tabla.get_children():
            self.__tabla.delete(fila)

        for estudiante in estudiantes:
            self.__tabla.insert("", tk.END, values=(estudiante.get_carnet(), estudiante.get_nombre(),
                                                    estudiante.get_edad(), estudiante.get_carrera(),
                                                    estudiante.get_correo()))

    # Borra lo escrito en todos los campos
    def limpiar_campos(self):
        self.__entrada_carnet.delete(0, tk.END)
        self.__entrada_nombre.delete(0, tk.END)
        self.__entrada_edad.delete(0, tk.END)
        self.__combo_carrera.set("")
        self.__entrada_correo.delete(0, tk.END)
        self.__entrada_carnet.focus()

    # ---------- Mensajes ----------

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    # askyesno devuelve True si el usuario presiona "Sí"
    def confirmar_eliminacion(self):
        return messagebox.askyesno("Confirmación", "¿Desea eliminar este estudiante y todas sus calificaciones?")

    # Cierra la ventana
    def salir(self):
        self.__ventana.destroy()
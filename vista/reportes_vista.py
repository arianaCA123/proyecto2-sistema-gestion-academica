import tkinter as tk


class ReportesVista:
    # Constructor: arma la ventana. Recibe la ventana principal (ventana_padre).
    def __init__(self, ventana_padre):
        # Toplevel = ventana secundaria
        self.__ventana = tk.Toplevel(ventana_padre)
        self.__ventana.title("Reportes")
        self.__ventana.resizable(False, False)

        tk.Label(self.__ventana, text="Reportes", font=("Arial", 15, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(15, 10)
        )
        tk.Label(self.__ventana, text="Seleccione un reporte:").grid(
            row=1, column=0, columnspan=2, padx=20, sticky="w"
        )

        # Todos los Radiobutton usan la misma variable, por eso solo se puede marcar uno.
        # Al marcar uno, la variable toma su value. Empieza marcado "listado".
        self.__opcion = tk.StringVar(value="listado")

        tk.Radiobutton(self.__ventana, text="Listado general de estudiantes",
                       variable=self.__opcion, value="listado").grid(row=2, column=0, columnspan=2, padx=40, sticky="w")
        tk.Radiobutton(self.__ventana, text="Promedio de notas por curso",
                       variable=self.__opcion, value="promedio").grid(row=3, column=0, columnspan=2, padx=40, sticky="w")
        tk.Radiobutton(self.__ventana, text="Estudiantes aprobados",
                       variable=self.__opcion, value="aprobados").grid(row=4, column=0, columnspan=2, padx=40, sticky="w")
        tk.Radiobutton(self.__ventana, text="Estudiantes reprobados",
                       variable=self.__opcion, value="reprobados").grid(row=5, column=0, columnspan=2, padx=40, sticky="w")
        tk.Radiobutton(self.__ventana, text="Cantidad total de cursos",
                       variable=self.__opcion, value="cantidad").grid(row=6, column=0, columnspan=2, padx=40, sticky="w")

        # Frame: contenedor para los dos botones
        marco_botones = tk.Frame(self.__ventana)
        marco_botones.grid(row=7, column=0, columnspan=2, pady=10)

        self.__boton_generar = tk.Button(marco_botones, text="Generar reporte", width=15)
        self.__boton_generar.grid(row=0, column=0, padx=5)
        self.__boton_salir = tk.Button(marco_botones, text="Salir", width=15)
        self.__boton_salir.grid(row=0, column=1, padx=5)

        # Listbox: listado donde se muestra el resultado del reporte
        self.__lista_resultado = tk.Listbox(self.__ventana, width=100, height=12)
        self.__lista_resultado.grid(row=8, column=0, columnspan=2, padx=20, pady=(0, 15))

    # El controlador le entrega los métodos que se ejecutan al presionar cada botón (sin paréntesis).
    def configurar_eventos(self, generar, salir):
        self.__boton_generar.config(command=generar)
        self.__boton_salir.config(command=salir)
        self.__ventana.protocol("WM_DELETE_WINDOW", salir)      # al cerrar con la X

    # Devuelve el value del Radiobutton marcado: "listado", "promedio", "aprobados", "reprobados" o "cantidad"
    def obtener_opcion(self):
        return self.__opcion.get()

    # Borra el listado y escribe cada línea del reporte
    def mostrar_resultado(self, lineas):
        self.__lista_resultado.delete(0, tk.END)
        for linea in lineas:
            self.__lista_resultado.insert(tk.END, linea)

    # Cierra la ventana
    def salir(self):
        self.__ventana.destroy()
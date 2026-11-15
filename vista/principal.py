import tkinter as tk
from tkinter import ttk, messagebox
from estudiante_vista import EstudianteVista
from curso_vista import CursoVista
from calificacion_vista import CalificacionVista
from reportes_vista import ReportesVista

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SISTEMA DE GESTION ACADEMICA")
        self.geometry("750x450")
        self.resizable(False, False)

        ttk.Label(
            self,
            text="SISTEMA DE GESTION ACADEMICA",
            font=("Helvetica", 16)
        ).grid(row=0, column=0, columnspan=3, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        ttk.Label(
            self,
            text="Seleccione una opción:"
        ).grid(row=1, column=0, columnspan=3, pady=10)

        self.boton_gestion_estudiante = ttk.Button(
            self,
            text="Gestión de Estudiantes",
            width=20,
            command=self.click_boton_estudiantes
        )
        self.boton_gestion_estudiante.grid(row=2, column=0, padx=10, pady=10, ipady=10)

        self.boton_gestion_cursos = ttk.Button(
            self,
            text="Gestión de Cursos",
            width=20,
            command=self.click_boton_cursos
        )
        self.boton_gestion_cursos.grid(row=2, column=1, padx=10, pady=10, ipady=10)

        self.boton_reguistro_calificaciones = ttk.Button(
            self,
            text="Registro de Calificaciones",
            width=20,
            command=self.click_boton_calificaciones
        )
        self.boton_reguistro_calificaciones.grid(row=3, column=0, padx=10, pady=10, ipady=10)

        self.boton_reportes = ttk.Button(
            self,
            text="Reportes",
            width=20,
            command=self.click_boton_reportes
        )
        self.boton_reportes.grid(row=3, column=1, padx=10, pady=10, ipady=10)

        self.boton_acerca_de = ttk.Button(
            self,
            text="Acerca de",
            width=20,
            command=self.acerca_de
        )
        self.boton_acerca_de.grid(row=4, column=0, padx=10, pady=10, ipady=10)

        self.boton_salir = ttk.Button(
            self,
            text="Salir",
            width=20
        )
        self.boton_salir.grid(row=4, column=1, padx=10, pady=10, ipady=10)

    def click_boton_estudiantes(self):
        estudiante_vista = EstudianteVista(self)
        estudiante_vista.mainloop()

    def click_boton_cursos(self):
        curso_vista = CursoVista(self)
        curso_vista.mainloop()

    def click_boton_calificaciones(self):
        #calificacion_vista = CalificacionVista(self)
        #calificacion_vista.mainloop()
        pass

    def click_boton_reportes(self):
        reportes_vista = ReportesVista(self)
        reportes_vista.mainloop()

    def acerca_de(self):
        mensaje = """
        SISTEMA DE GESTIÓN ACADÉMICA

        Aplicación diseñada para facilitar la administración
        de la información académica.

        Funcionalidades:
        • Gestión de estudiantes.
        • Gestión de cursos.
        • Registro de calificaciones.
        • Generación de reportes.

        Desarrollado en Python utilizando Tkinter.
        Versión 1.0
        """

        messagebox.showinfo("Acerca de", mensaje)



app = Principal()
app.mainloop()
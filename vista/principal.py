# VISTA - Clase Principal
# Ventana principal del sistema: tiene un botón para abrir cada ventana secundaria.
# No abre las ventanas ella misma: llama a los métodos que le entrega el controlador.

import tkinter as tk
from tkinter import ttk, messagebox
from vista.estudiante_vista import EstudianteVista
from vista.curso_vista import CursoVista
from vista.calificacion_vista import CalificacionVista
from vista.reportes_vista import ReportesVista

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()

        # Métodos del controlador que abren cada ventana (los entrega configurar_eventos)
        self.__abrir_estudiantes = None
        self.__abrir_cursos = None
        self.__abrir_calificaciones = None
        self.__abrir_reportes = None

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

        # Botones: cada uno ejecuta su método click_boton_... al presionarse
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
            command=self.click_boton_acerca_de
        )
        self.boton_acerca_de.grid(row=4, column=0, padx=10, pady=10, ipady=10)

        self.boton_salir = ttk.Button(
            self,
            text="Salir",
            width=20,
            command=self.destroy        # cierra la ventana principal y termina el programa
        )
        self.boton_salir.grid(row=4, column=1, padx=10, pady=10, ipady=10)

    # El controlador le entrega los métodos que abren cada ventana
    def configurar_eventos(self, abrir_estudiantes, abrir_cursos, abrir_calificaciones, abrir_reportes):
        self.__abrir_estudiantes = abrir_estudiantes
        self.__abrir_cursos = abrir_cursos
        self.__abrir_calificaciones = abrir_calificaciones
        self.__abrir_reportes = abrir_reportes

    # Cada botón llama al método del controlador y le pasa esta ventana como ventana padre (self)
    def click_boton_estudiantes(self):
        self.__abrir_estudiantes(self)

    def click_boton_cursos(self):
        self.__abrir_cursos(self)

    def click_boton_calificaciones(self):
        self.__abrir_calificaciones(self)

    def click_boton_reportes(self):
        self.__abrir_reportes(self)

    def click_boton_acerca_de(self):
        messagebox.showinfo("Acerca de", "Sistema de Gestión Académica\nProyecto #2 - Desarrollo de Software II")
import tkinter as tk
from tkinter import ttk

class CalificacionVista():
    def __init__(self, ventana_padre):
        self.__ventana = tk.Toplevel(ventana_padre)
        self.__ventana.title("Calificación")
        self.__ventana.geometry("750x450")
        self.__ventana.resizable(False, False)
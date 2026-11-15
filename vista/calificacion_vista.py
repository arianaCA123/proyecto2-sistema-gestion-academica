import tkinter as tk
from tkinter import ttk

class CalificacionVista():
    def __init__(self, ventana_padre):
        self.__ventana = tk.Toplevel(ventana_padre)
        self.title("Calificación")
        self.geometry("750x450")
        self.resizable(False, False)
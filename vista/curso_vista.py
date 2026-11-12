import tkinter as tk
from tkinter import ttk, messagebox


class CursoVista:

    # Constructor: crea la ventana para gestionar los cursos.
    # Recibe la ventana principal para abrir esta ventana secundaria.

    def __init__(self, ventana_padre):

        # Crea una ventana secundaria.
        self.__ventana = tk.Toplevel(ventana_padre)
        self.__ventana.title("Gestión de cursos")
        self.__ventana.geometry("750x450")
      

        # Título de la ventana.
        tk.Label(self.__ventana,text="Registro de cursos",font=("Arial", 15, "bold")).grid(row=0, column=0, columnspan=4, pady=15)

        # campo para ingresar el código del curso.
        tk.Label(self.__ventana, text="Código:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.__entrada_codigo = tk.Entry(self.__ventana, width=30)
        self.__entrada_codigo.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        
      
        # campo para ingresar el nombre del curso.
        tk.Label(self.__ventana, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.__entrada_nombre = tk.Entry(self.__ventana, width=30)
        self.__entrada_nombre.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")
       

        # campo para ingresar la cantidad de creditos.
        tk.Label(self.__ventana, text="Créditos:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.__entrada_creditos = tk.Entry(self.__ventana, width=30)
        self.__entrada_creditos.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        # campo para ingresar el ciclo del curso.
        # Uso de Combobox para que la eleccion del ciclo sea una lista despeglable  (para que se tome como numero romano)
        tk.Label(self.__ventana, text="Ciclo:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.__entrada_ciclo = ttk.Combobox(self.__ventana,values=["I", "II", "III", "IV", "V", "VI", "VII", "VIII"],state="readonly",width=27)
        self.__entrada_ciclo.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        
        #______________________________________________________________________________________________
        # Marco para agrupar los botones.
        marco_botones = tk.Frame(self.__ventana)
        marco_botones.grid(row=5, column=0, columnspan=4, pady=15)
        
        
        # Botónes para (registrar, consultar, modificar, eliminar, limpiar, cerrar.)
        
        self.__boton_registrar = tk.Button(marco_botones, text="Registrar", width=10)
        self.__boton_registrar.grid(row=0, column=0, padx=3)

        self.__boton_consultar = tk.Button(marco_botones, text="Consultar", width=10)
        self.__boton_consultar.grid(row=0, column=1, padx=3)
        
        self.__boton_modificar = tk.Button(marco_botones, text="Modificar", width=10)
        self.__boton_modificar.grid(row=0, column=2, padx=3)

        self.__boton_eliminar = tk.Button(marco_botones, text="Eliminar", width=10)
        self.__boton_eliminar.grid(row=0, column=3, padx=3)

        self.__boton_limpiar = tk.Button(marco_botones, text="Limpiar", width=10)
        self.__boton_limpiar.grid(row=0, column=4, padx=3)
        
        # Salir estara en marco de botones no en ventana
        self.__boton_salir = tk.Button(marco_botones, text="Salir", width=10)
        self.__boton_salir.grid(row=0, column=5, padx=3)

       #_______________________________________________________________________
        # Tabla para mostrar los cursos registrados.
        self.__tabla = ttk.Treeview(self.__ventana,columns=("codigo", "nombre", "creditos", "ciclo"),show="headings")

        # Encabezados de las columnas.
        self.__tabla.heading("codigo", text="Código")
        self.__tabla.heading("nombre", text="Nombre")
        self.__tabla.heading("creditos", text="Créditos")
        self.__tabla.heading("ciclo", text="Ciclo")

        # Ubicación de la tabla.
        self.__tabla.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # Coloca el cursor inicialmente en el campo código.
        self.__entrada_codigo.focus() #el cuadrito

    # Conecta los botones con los métodos del Controlador.
    # Recibe las funciones que se ejecutarán al presionar cada botón.

    def configurar_eventos(self, registrar, consultar, modificar,eliminar, limpiar, salir):
        self.__boton_registrar.config(command=registrar)
        self.__boton_consultar.config(command=consultar)
        self.__boton_modificar.config(command=modificar)
        self.__boton_eliminar.config(command=eliminar)
        self.__boton_limpiar.config(command=limpiar)
        self.__boton_salir.config(command=salir)

        # Permite cerrar la ventana con la X.
        self.__ventana.protocol("WM_DELETE_WINDOW", salir)

    # Obtiene el código escrito en el campo.
    def obtener_codigo(self):
        return self.__entrada_codigo.get().strip()

    # Obtiene el nombre escrito en el campo.
    def obtener_nombre(self):
        return self.__entrada_nombre.get().strip()

    # Obtiene los créditos escritos en el campo.
    def obtener_creditos(self):
        return self.__entrada_creditos.get().strip()

    # Obtiene el ciclo escrito en el campo.
    def obtener_ciclo(self):
        return self.__entrada_ciclo.get().strip()

    # Muestra los datos de un curso en los campos.
    def mostrar_curso(self, curso):

        self.limpiar_campos()

        self.__entrada_codigo.insert(0, curso.get_codigo())  #se usa insert() por que se introduce texto mediante (Entry)
        self.__entrada_nombre.insert(0, curso.get_nombre())
        self.__entrada_creditos.insert(0, str(curso.get_creditos()))
        self.__entrada_ciclo.set(curso.get_ciclo())   # Se utiliza set() y no insert porque el ciclo es un Combobox y permite seleccionar una opción.

    # Limpia todos los campos del formulario.
    def limpiar_campos(self):

        self.__entrada_codigo.delete(0, tk.END)
        self.__entrada_nombre.delete(0, tk.END)
        self.__entrada_creditos.delete(0, tk.END)
        self.__entrada_ciclo.set("")    #.set("") deja vacío el Combobox.

    # Muestra los cursos registrados en la tabla.
    def mostrar_tabla(self, cursos):

        # Obtiene las filas que hay en la tabla y las elimina.
        for fila in self.__tabla.get_children():
            self.__tabla.delete(fila)

        # Recorre los cursos y agrega sus datos a la tabla.
        for curso in cursos:
            self.__tabla.insert("",tk.END,values=(curso.get_codigo(),curso.get_nombre(),curso.get_creditos(),curso.get_ciclo()))

    # Muestra un mensaje informativo.
    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información:", mensaje)

    # Muestra un mensaje de error.
    def mostrar_error(self, mensaje):
        messagebox.showerror("Error...", mensaje)

    # Solicita confirmación antes de eliminar un curso si / no.
    def confirmar_eliminacion(self):
        return messagebox.askyesno("Confirmación","¿Desea eliminar este curso?")

    # Cierra la ventana de cursos.
    def salir(self):
        self.__ventana.destroy()

   
# MODELO - Clase Estudiante
# Representa a un estudiante. Guarda sus datos y calcula su edad.
# No usa ventanas: solo datos.

from datetime import date      # date.today() da la fecha de hoy, se usa para calcular la edad


class Estudiante:
    # Constructor: se ejecuta cuando se crea un objeto Estudiante.
    # Usa los setters para guardar los datos.
    def __init__(self, carnet, nombre, edad, carrera, correo):
        self.set_carnet(carnet)
        self.set_nombre(nombre)
        self.set_edad(edad)          # el enunciado lo llama "edad", pero guarda la fecha de nacimiento (dd/mm/aaaa)
        self.set_carrera(carrera)
        self.set_correo(correo)


    def set_carnet(self, carnet):
        self.__carnet = carnet

    def get_carnet(self):
        return self.__carnet

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        self.__edad = edad

    def get_edad(self):
        return self.__edad           # devuelve la fecha de nacimiento, no los años

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def set_correo(self, correo):
        self.__correo = correo

    def get_correo(self):
        return self.__correo

    # Calcula la edad en años a partir de la fecha de nacimiento
    def calcular_edad(self):
        partes = self.get_edad().split("/")     # "15/03/2005" -> ["15", "03", "2005"]
        dia = int(partes[0])                    # int() pasa el texto a número
        mes = int(partes[1])
        anio = int(partes[2])

        hoy = date.today()                      # fecha de hoy
        edad = hoy.year - anio                  # resta de años

        # si todavía no ha cumplido años este año, se le resta 1
        if hoy.month < mes or (hoy.month == mes and hoy.day < dia):
            edad = edad - 1

        return edad

    # Se ejecuta automáticamente cuando se hace print(estudiante) o str(estudiante).
    # El enunciado pide llamar a calcular_edad() aquí adentro.
    def __str__(self):
        return f"Carné: {self.get_carnet()} - Nombre: {self.get_nombre()} - " \
               f"Edad: {self.calcular_edad()} años - Carrera: {self.get_carrera()} - " \
               f"Correo: {self.get_correo()}"
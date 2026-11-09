# MODELO - Clase Curso
# No utiliza ventanas, solamente maneja los datos de un curso.
class Curso:

    def __init__(self, codigo, nombre, creditos, ciclo):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_creditos(creditos)
        self.set_ciclo(ciclo)
        
 # Setter y getter del código

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_creditos(self, creditos):
        self.__creditos = creditos

    def get_creditos(self):
        return self.__creditos

    def set_ciclo(self, ciclo):
        self.__ciclo = ciclo

    def get_ciclo(self):
        return self.__ciclo
    
# representa la información del curso como texto.
 # Se ejecuta cuando hacemos print(curso) o str(curso).
    def __str__(self):
        return f"Código: {self.get_codigo()} - " \
               f"Nombre: {self.get_nombre()} - " \
               f"Créditos: {self.get_creditos()} - " \
               f"Ciclo: {self.get_ciclo()}
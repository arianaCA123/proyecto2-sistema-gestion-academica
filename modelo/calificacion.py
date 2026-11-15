class Calificacion:
    def __init__(self, carnet_estudiante, codigo_curso, nota,ciclo,annio):
        self.set_carnet_estudiante(carnet_estudiante)
        self.set_codigo_curso(codigo_curso)
        self.set_nota(nota)
        self.set_ciclo(ciclo)
        self.set_annio(annio)

    def get_carnet_estudiante(self):
        return self.__carnet_estudiante

    def set_carnet_estudiante(self, carnet_estudiante):
        self.__carnet_estudiante = carnet_estudiante

    def get_codigo_curso(self):
        return self.__codigo_curso

    def set_codigo_curso(self, codigo_curso):
        self.__codigo_curso = codigo_curso

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def get_ciclo(self):
        return self.__ciclo

    def set_ciclo(self, ciclo):
        self.__ciclo = ciclo

    def get_annio(self):
        return self.__annio

    def set_annio(self, annio):
        self.__annio = annio

    def __str__(self):
        return f"Carnet: {self.__carnet_estudiante} || Curso: {self.__codigo_curso} || Nota: {self.__nota} || Ciclo: {self.__ciclo} || Año: {self.__annio}"
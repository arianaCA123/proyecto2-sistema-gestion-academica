from modelo.calificacion import Calificacion

class RegistroCalificacion:
    def __init__(self):
        # Lista unidimensional de objetos Calificacion.
        self.__calificaciones = []

    def crear_calificacion(self, carnet_estudiante, codigo_curso, nota, ciclo, annio):

        if self.buscar_por_carnet(carnet_estudiante) is not None:
            return False

        calificacion = Calificacion(carnet_estudiante, codigo_curso, nota, ciclo, annio)
        self.__calificaciones.append(calificacion)
        return True

    def consultar_calificaciones(self, carnet_estudiante):
        califacacion_estudiate = self.buscar_por_carnet(carnet_estudiante)
        if califacacion_estudiate is not None:
            return califacacion_estudiate
        return None

    def modificar_calificacion(self, carnet_estudiante, nuevo_codigo_curso, nueva_nota, nuevo_ciclo, nuevo_annio):
        calificacion = self.buscar_por_carnet(carnet_estudiante)
        if calificacion is not None:
            calificacion.set_codigo_curso(nuevo_codigo_curso)
            calificacion.set_nota(nueva_nota)
            calificacion.set_ciclo(nuevo_ciclo)
            calificacion.set_annio(nuevo_annio)
            return True
        return False

    def eliminar_calificacion(self, carnet_estudiante):
        calificacion = self.buscar_por_carnet(carnet_estudiante)
        if calificacion is not None:
            self.__calificaciones.remove(calificacion)
            return True
        return False

    def listar_calificaciones(self):
        if len(self.__calificaciones) == 0:
            return None
        return self.__calificaciones
        

    def buscar_por_carnet(self, carnet_estudiante):
        # Devuelve una lista de calificaciones del estudiante con el carnet dado.
        for calificacion in self.__calificaciones:
            if calificacion.get_carnet_estudiante() == carnet_estudiante:
                return calificacion
from modelo.calificacion import Calificacion


class RegistroCalificacion:
    def __init__(self):
        self.__calificaciones = []

    def obtener_lista(self):
        return self.__calificaciones

    def buscar(self, carnet_estudiante, codigo_curso, ciclo, annio):
        for calificacion in self.__calificaciones:
            if (calificacion.get_carnet_estudiante() == carnet_estudiante
                    and calificacion.get_codigo_curso() == codigo_curso
                    and calificacion.get_ciclo() == ciclo
                    and calificacion.get_annio() == annio):
                return calificacion
        return None

    def crear_calificacion(self, carnet_estudiante, codigo_curso, nota, ciclo, annio):
        if self.buscar(carnet_estudiante, codigo_curso, ciclo, annio) is not None:
            return False

        calificacion = Calificacion(carnet_estudiante, codigo_curso, nota, ciclo, annio)
        self.__calificaciones.append(calificacion)
        return True

    def modificar_calificacion(self, carnet_estudiante, codigo_curso, ciclo, annio, nueva_nota):
        calificacion = self.buscar(carnet_estudiante, codigo_curso, ciclo, annio)
        if calificacion is not None:
            calificacion.set_nota(nueva_nota)
            return True
        return False

    def eliminar_calificacion(self, carnet_estudiante, codigo_curso, ciclo, annio):
        calificacion = self.buscar(carnet_estudiante, codigo_curso, ciclo, annio)
        if calificacion is not None:
            self.__calificaciones.remove(calificacion)
            return True
        return False
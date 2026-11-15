from modelo.estudiante import Estudiante


class RegistroEstudiante:
    def __init__(self):
        # Lista unidimensional de objetos Estudiante.
        self.__estudiantes = []

    # Devuelve la lista completa de estudiantes
    def obtener_lista(self):
        return self.__estudiantes

    # Recorre la lista buscando el carné.
    # Devuelve el estudiante si lo encuentra, o None si no existe.
    def buscar_por_carnet(self, carnet):
        for estudiante in self.__estudiantes:
            if estudiante.get_carnet() == carnet:
                return estudiante
        return None

    # Crea el estudiante y lo agrega a la lista.
    # Devuelve False si ya existe ese carné, o True si lo guardó.
    def guardar_estudiante(self, carnet, nombre, edad, carrera, correo):
        if self.buscar_por_carnet(carnet) != None:
            return False

        estudiante = Estudiante(carnet, nombre, edad, carrera, correo)
        self.__estudiantes.append(estudiante)
        return True

    # Cambia los datos de un estudiante. El carné no se cambia porque es el que lo identifica.
    # Devuelve el estudiante modificado, o None si no existe.
    def modificar_estudiante(self, carnet, nombre, edad, carrera, correo):
        estudiante = self.buscar_por_carnet(carnet)
        if estudiante != None:
            estudiante.set_nombre(nombre)
            estudiante.set_edad(edad)
            estudiante.set_carrera(carrera)
            estudiante.set_correo(correo)
        return estudiante

    # Quita el estudiante de la lista.
    # Devuelve False si no existe, o True si lo eliminó.
    def eliminar_estudiante(self, carnet):
        estudiante = self.buscar_por_carnet(carnet)
        if estudiante == None:
            return False

        self.__estudiantes.remove(estudiante)
        return True

    # ---------- REPORTES: cada uno devuelve una lista de textos ----------

    # Listado general de estudiantes (usa el __str__, que ya trae la edad)
    def reporte_listado(self):
        lineas = []

        for estudiante in self.__estudiantes:
            lineas.append(str(estudiante))

        return lineas

    # Estudiantes aprobados (nota mayor o igual a 70).
    # Recibe la lista de calificaciones, que se la pasa el controlador.
    def reporte_aprobados(self, calificaciones):
        lineas = []

        for calificacion in calificaciones:
            if calificacion.get_nota() >= 70:
                lineas.append(f"Carné: {calificacion.get_carnet_estudiante()} | "
                              f"Curso: {calificacion.get_codigo_curso()} | "
                              f"Nota: {calificacion.get_nota():.2f}")

        return lineas

    # Estudiantes reprobados (nota menor a 70)
    def reporte_reprobados(self, calificaciones):
        lineas = []

        for calificacion in calificaciones:
            if calificacion.get_nota() < 70:
                lineas.append(f"Carné: {calificacion.get_carnet_estudiante()} | "
                              f"Curso: {calificacion.get_codigo_curso()} | "
                              f"Nota: {calificacion.get_nota():.2f}")

        return lineas
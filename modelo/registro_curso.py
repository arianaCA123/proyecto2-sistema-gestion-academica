# MODELO - Clase RegistroCurso
# Administra la lista de cursos registrados (guardar, buscar, modificar, eliminar y reportes de cursos).
#
# Reportes que usa el controlador: reporte_promedio_por_curso(calificaciones) y cantidad_cursos().

from modelo.curso import Curso

class RegistroCurso:

    def __init__(self):
        # Lista unidimensional de objetos Curso.
        self.__cursos = []

    # Devuelve la lista completa de cursos.
    def listar_cursos(self):
        return self.__cursos

    # Recorre la lista buscando el codigo del curso.
    # Devuelve el curso si lo encuentra, o None si no existe.
    def buscar_por_codigo(self, codigo):
        codigo = codigo.strip()

        for curso in self.__cursos:
            if curso.get_codigo() == codigo:
                return curso

        return None

    
    # Devuelve un mensaje indicando el resultado.
    def registrar_curso(self, codigo, nombre, creditos, ciclo):

        # strip() quita los espacios al inicio y al final.
        codigo = codigo.strip()
        nombre = nombre.strip()
        ciclo = ciclo.strip()
        
        # Verifica si ya existe un curso con ese código.
        if self.buscar_por_codigo(codigo) is not None:
            return "El curso ya existe"


        # El Modelo crea el objeto Curso.
        curso = Curso(codigo, nombre, creditos, ciclo)
        self.__cursos.append(curso)  #se añade a lista

        return "Curso registrado correctamente"

    # Modifica los datos de un curso.
    # el código no se cambia porque es el que identifica al curso.
    def modificar_curso(self, codigo, nuevo_nombre, nuevos_creditos, nuevo_ciclo):

        codigo = codigo.strip()
        nuevo_nombre = nuevo_nombre.strip()
        nuevo_ciclo = nuevo_ciclo.strip()

        curso = self.buscar_por_codigo(codigo)

        if curso is None:
            return "Curso no encontrado"

        # Actualiza datos con setters.
        curso.set_nombre(nuevo_nombre)
        curso.set_creditos(nuevos_creditos)
        curso.set_ciclo(nuevo_ciclo)

        return "Curso modificado correctamente"

    # Elimina un curso de la lista.
    # La confirmación de eliminación se pregunta en la Vista.
    def eliminar_curso(self, codigo):

        codigo = codigo.strip()
        curso = self.buscar_por_codigo(codigo)

        if curso is None:
            return "Curso no encontrado"

        self.__cursos.remove(curso)

        return "Curso eliminado correctamente"
      
    # Verifica si la lista de cursos está vacía.
    def esta_vacio(self):
        return len(self.__cursos) == 0

   #----REPORTE--- Cantidad total de cursos registrados
    def cantidad_cursos(self):
        return len(self.__cursos)

    # ---- REPORTE --- Promedio de notas por curso
    # Recibe la lista de calificaciones (se la pasa el controlador) y devuelve una lista de textos.
    def reporte_promedio_por_curso(self, calificaciones):
        lineas = []

        for curso in self.__cursos:
            suma = 0
            cantidad = 0

            # Suma las notas de este curso
            for calificacion in calificaciones:
                if calificacion.get_codigo_curso() == curso.get_codigo():
                    suma = suma + calificacion.get_nota()
                    cantidad = cantidad + 1

            # Solo se muestran los cursos que tienen notas (así no se divide entre 0)
            if cantidad > 0:
                promedio = suma / cantidad
                lineas.append(f"Curso: {curso.get_codigo()} - {curso.get_nombre()} | Promedio: {promedio:.2f}")

        return lineas
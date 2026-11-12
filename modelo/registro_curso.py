# MODELO - Clase RegistroCurso
# administra la lista de cursos registrados.

from modelo.curso import Curso

class RegistroCurso:

    def __init__(self):
        # Lista unidimensional de objetos Curso.
        self.cursos = []

    # Devuelve la lista completa de cursos.
    def listar_cursos(self):
        return self.cursos

    # Recorre la lista buscando el codigo del curso.
    # Devuelve el curso si lo encuentra, o None si no existe.
    def buscar_por_codigo(self, codigo):
        codigo = codigo.strip()

        for curso in self.cursos:
            if curso.get_codigo() == codigo:
                return curso

        return None

    # Valida los datos, crea el curso y lo agrega a la lista.
    # Devuelve un mensaje indicando el resultado.
    def registrar_curso(self, codigo, nombre, creditos, ciclo):

        # strip() quita los espacios al inicio y al final.
        codigo = codigo.strip()
        nombre = nombre.strip()
        ciclo = ciclo.strip()

        # Verifica que ningún campo esté vacío.
        #  Los créditos serán validados en el Controlador.
        
        if codigo == "" or nombre == "" or ciclo == "":
            return "Faltan datos por ingresar"

        # Verifica si ya existe un curso con ese código.
        if self.buscar_por_codigo(codigo) is not None:
            return "El curso ya existe"

        # El Modelo crea el objeto Curso.
        curso = Curso(codigo, nombre, creditos, ciclo)
        self.cursos.append(curso)  #se añade a lista

        return "Curso registrado correctamente"

    # Modifica los datos de un curso.
    # el código no se cambia porque es el que identifica al curso.
    def modificar_curso(self, codigo, nuevo_nombre, nuevos_creditos, nuevo_ciclo):

        codigo = codigo.strip()
        nuevo_nombre = nuevo_nombre.strip()
        nuevo_ciclo = nuevo_ciclo.strip()

        # Verifica que ningún campo esté vacío.
        # Los créditos se validan en controlador.
        if codigo == "" or nuevo_nombre == "" or nuevo_ciclo == "":
            return "Faltan datos por ingresar"

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

        self.cursos.remove(curso)

        return "Curso eliminado correctamente"
      
    # Verifica si la lista de cursos está vacía.
    def esta_vacio(self):
        return len(self.cursos) == 0

   #----REPORTE--- Cantidad total de cursos registrados
    def cantidad_cursos(self):
        return len(self.cursos)
  
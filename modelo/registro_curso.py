from modelo.curso import Curso

class RegistroCurso:

    def __init__(self):
        self.__cursos = []

    def buscar_por_codigo(self, codigo):
        for curso in self.__cursos:
            if curso.get_codigo() == codigo:
                return curso

        return None

    def registrar_curso(self, codigo, nombre, creditos, ciclo):
        curso = self.buscar_por_codigo(codigo)

        if curso is not None:
            return "CODIGO_DUPLICADO"

        nuevo_curso = Curso(codigo, nombre, creditos, ciclo)
        self.__cursos.append(nuevo_curso)

        return "REGISTRADO"

    def modificar_curso(self, codigo, nuevo_nombre, nuevos_creditos, nuevo_ciclo):
        curso = self.buscar_por_codigo(codigo)

        if curso is None:
            return "NO_ENCONTRADO"

        curso.set_nombre(nuevo_nombre)
        curso.set_creditos(nuevos_creditos)
        curso.set_ciclo(nuevo_ciclo)

        return "MODIFICADO"

    def eliminar_curso(self, codigo):
        curso = self.buscar_por_codigo(codigo)

        if curso is None:
            return "NO_ENCONTRADO"

        self.__cursos.remove(curso)

        return "ELIMINADO"

    def listar_cursos(self):
        return self.__cursos

    def esta_vacio(self):
        return len(self.__cursos) == 0
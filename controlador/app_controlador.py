# CONTROLADOR - Clase AppControlador
# Conecta la Vista de cursos, estudiante y calificacion con el Registro.

from modelo.registro_estudiante import RegistroEstudiante
from modelo.registro_curso import RegistroCurso
from modelo.registro_calificacion import RegistroCalificacion

from vista.estudiante_vista import EstudianteVista
from vista.curso_vista import CursoVista
from vista.calificacion_vista import CalificacionVista
from vista.reportes_vista import ReportesVista

#no esta terminado, por que necesito las partes de califiacion y estudiantes para integrarlas

class AppControlador:

    # Constructor
    def __init__(self):
        
         
        # Registro de estudiantes (Ariana)
         self.__registro_estudiante = RegistroEstudiante()

        # Registro de cursos (yo)
        self.__registro_curso = RegistroCurso()

        # Registro de calificaciones (Carlos)
        self.__registro_calificacion = RegistroCalificacion()
#_______________________________________________________________________   
        
         # vistas inicialmente las ventanas no estan abiertas (None).
        self.__vista_estudiante = None
        self.__vista_curso = None
        self.__vista_calificacion = None
        self.__vista_reportes = None

# ________________________________________________________________________________


    # Abre la ventana de cursos y conecta sus botones.
    # Recibe la ventana principal como padre.
    def abrir_cursos(self, ventana_padre):

        # Crea la ventana secundaria de cursos.
        self.__vista_curso = CursoVista(ventana_padre)

        # Conecta cada botón con su método correspondiente.
        self.__vista_curso.configurar_eventos(self.registrar_curso,self.consultar_curso,self.modificar_curso,self.eliminar_curso,self.limpiar_campos,self.salir)

        # Muestra los cursos que ya están registrados.
        self.actualizar_tabla()

    # Registra un curso nuevo.
    def registrar_curso(self):

        # Obtiene los datos escritos en la Vista.
        codigo = self.__vista_curso.obtener_codigo()
        nombre = self.__vista_curso.obtener_nombre()
        creditos = self.__vista_curso.obtener_creditos()
        ciclo = self.__vista_curso.obtener_ciclo()

        # Verifica que todos los campos tengan información.
        if codigo == "" or nombre == "" or creditos == "" or ciclo == "":
            self.__vista_curso.mostrar_error("Debe completar todos los campos.")
            return

        # Valida que los créditos sean números enteros.
        if not creditos.isdigit():
            self.__vista_curso.mostrar_error("Los créditos deben ser un número entero.")
            return

        creditos = int(creditos)

        # Verifica que los créditos sean mayores que cero.
        if creditos <= 0:
            self.__vista_curso.mostrar_error("Los créditos deben ser mayores que cero.")
            return

        # Envía los datos al Registro para guardar el curso.
        mensaje = self.__registro_curso.registrar_curso(codigo, nombre, creditos, ciclo)

        # Muestra el resultado de la operación.
        if mensaje == "Curso registrado correctamente":
            self.__vista_curso.mostrar_mensaje(mensaje)

            # Actualiza la tabla para mostrar el nuevo curso.
            self.actualizar_tabla()

            # Limpia los campos después del registro.
            self.limpiar_campos()

        else:
            self.__vista_curso.mostrar_error(mensaje)

    # Busca un curso utilizando su código.
    def consultar_curso(self):

        # Obtiene el código escrito por el usuario.
        codigo = self.__vista_curso.obtener_codigo()

        # Verifica que se haya ingresado un código.
        if codigo == "":
            self.__vista_curso.mostrar_error("Ingrese el código del curso.")
            return

        # Verifica si existen cursos registrados.
        if self.__registro_curso.esta_vacio():
            self.__vista_curso.mostrar_error("No hay cursos registrados.")
            return

        # Busca el curso en el Registro.
        curso = self.__registro_curso.buscar_por_codigo(codigo)

        # Verifica si encontró el curso.
        if curso is None:
            self.__vista_curso.mostrar_error("Curso no encontrado.")
        else:
            # Muestra los datos del curso en los campos.
            self.__vista_curso.mostrar_curso(curso)

    # Modifica los datos de un curso existente.
    def modificar_curso(self):

        # Obtiene los datos ingresados en la Vista.
        codigo = self.__vista_curso.obtener_codigo()
        nombre = self.__vista_curso.obtener_nombre()
        creditos = self.__vista_curso.obtener_creditos()
        ciclo = self.__vista_curso.obtener_ciclo()

        # Verifica que todos los campos tengan información.
        if codigo == "" or nombre == "" or creditos == "" or ciclo == "":
            self.__vista_curso.mostrar_error("Debe completar todos los campos.")
            return

        # Valida que los créditos sean números enteros.
        if not creditos.isdigit():
            self.__vista_curso.mostrar_error("Los créditos deben ser un número entero.")
            return

        creditos = int(creditos)

        # Verifica que los créditos sean mayores que cero.
        if creditos <= 0:
            self.__vista_curso.mostrar_error("Los créditos deben ser mayores que cero.")
            return

        # Envía los nuevos datos al Registro.
        mensaje = self.__registro_curso.modificar_curso(codigo, nombre, creditos, ciclo)

        # Muestra el resultado de la modificación.
        if mensaje == "Curso modificado correctamente":
            self.__vista_curso.mostrar_mensaje(mensaje)

            # Actualiza la tabla con los datos modificados.
            self.actualizar_tabla()

            # Limpia los campos.
            self.limpiar_campos()

        else:
            self.__vista_curso.mostrar_error(mensaje)

    # Elimina un curso utilizando su código.
    def eliminar_curso(self):

        # Obtiene el código del curso.
        codigo = self.__vista_curso.obtener_codigo()

        # Verifica que se haya ingresado un código.
        if codigo == "":
            self.__vista_curso.mostrar_error("Ingrese el código del curso.")
            return

        # Busca el curso antes de solicitar confirmación.
        curso = self.__registro_curso.buscar_por_codigo(codigo)

        if curso is None:
            self.__vista_curso.mostrar_error("Curso no encontrado.")
            return

        # Pregunta si el usuario desea confirmar la eliminación.
        if self.__vista_curso.confirmar_eliminacion():

            # Envía el código al Registro para eliminar el curso.
            mensaje = self.__registro_curso.eliminar_curso(codigo)

            self.__vista_curso.mostrar_mensaje(mensaje)

            # Actualiza la tabla después de eliminar.
            self.actualizar_tabla()

            # Limpia los campos.
            self.limpiar_campos()

    # Actualiza la tabla de cursos.
    def actualizar_tabla(self):

        # Obtiene la lista de cursos del Registro.
        cursos = self.__registro_curso.listar_cursos()

        # Envía la lista a la Vista para mostrarla.
        self.__vista_curso.mostrar_tabla(cursos)

    # Limpia los campos de la ventana.
    def limpiar_campos(self):

        self.__vista_curso.limpiar_campos()

    # Cierra la ventana de cursos.
    def salir(self):

        self.__vista_curso.salir()

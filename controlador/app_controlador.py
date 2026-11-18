# CONTROLADOR - Clase AppControlador
# Conecta las Vistas (ventanas) con el Modelo (registros).
# Recibe lo que escribe el usuario, lo valida, le pide al Modelo que guarde, busque,
# modifique o elimine, y le dice a la Vista qué mensaje o datos mostrar.
# No crea objetos del dominio (eso lo hace el Modelo).


from modelo.registro_estudiante import RegistroEstudiante
from modelo.registro_curso import RegistroCurso
from modelo.registro_calificacion import RegistroCalificacion

from vista.estudiante_vista import EstudianteVista
from vista.curso_vista import CursoVista
from vista.calificacion_vista import CalificacionVista
from vista.reportes_vista import ReportesVista
from vista.principal import Principal

from datetime import date   # Importa date para validar que las fechas de nacimiento existan en el calendario y sea valida.

class AppControlador:

    # Constructor: crea los tres registros (el Modelo) y deja las ventanas sin abrir
    def __init__(self):

        # Registro de estudiantes 
        self.__registro_estudiante = RegistroEstudiante()

        # Registro de cursos 
        self.__registro_curso = RegistroCurso()

        # Registro de calificaciones 
        self.__registro_calificacion = RegistroCalificacion()

        # Vistas: al inicio las ventanas no están abiertas (None).
        self.__vista_estudiante = None
        self.__vista_curso = None
        self.__vista_calificacion = None
        self.__vista_reportes = None

    # =================== CURSOS ===================

    # Abre la ventana de cursos y conecta sus botones.
    # Recibe la ventana principal como padre.
    def abrir_cursos(self, ventana_padre):

        # Crea la ventana secundaria de cursos.
        self.__vista_curso = CursoVista(ventana_padre)

        # Conecta cada botón con su método correspondiente.
        self.__vista_curso.configurar_eventos(self.registrar_curso,self.consultar_curso,self.modificar_curso,self.eliminar_curso,self.limpiar_campos_curso,self.salir_curso)

        # Muestra los cursos que ya están registrados.
        self.actualizar_tabla_curso()

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
            self.actualizar_tabla_curso()
            
            # Actualiza los cursos disponibles en el ComboBox de calificaciones.
            self.actualizar_combos_calificacion()

            # Limpia los campos después del registro.
            self.limpiar_campos_curso()

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
            self.actualizar_tabla_curso()

            # Limpia los campos.
            self.limpiar_campos_curso()

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

            # Obtiene la lista de calificaciones.
            calificaciones = self.__registro_calificacion.obtener_lista()

            # Recorre una copia para eliminar las calificaciones del curso.
            for calificacion in calificaciones[:]:
                if calificacion.get_codigo_curso() == codigo:
                    self.__registro_calificacion.eliminar_calificacion(calificacion.get_carnet_estudiante(),codigo,calificacion.get_ciclo(),calificacion.get_annio())

            # Elimina el curso.
            mensaje = self.__registro_curso.eliminar_curso(codigo)

            self.__vista_curso.mostrar_mensaje(mensaje)

            # Actualiza la tabla después de eliminar.
            self.actualizar_tabla_curso()

            # Actualiza los cursos disponibles en el ComboBox de calificaciones.
            self.actualizar_combos_calificacion()

            # Limpia los campos.
            self.limpiar_campos_curso()
        

    # Actualiza la tabla de cursos.
    def actualizar_tabla_curso(self):

        # Obtiene la lista de cursos del Registro.
        cursos = self.__registro_curso.listar_cursos()

        # Envía la lista a la Vista para mostrarla.
        self.__vista_curso.mostrar_tabla(cursos)

    # Limpia los campos de la ventana.
    def limpiar_campos_curso(self):

        self.__vista_curso.limpiar_campos()

    # Cierra la ventana de cursos.
    def salir_curso(self):

        self.__vista_curso.salir()

    # Crea la ventana principal, conecta sus botones y arranca el programa
    def iniciar(self):
        principal = Principal()
        principal.configurar_eventos(
            self.abrir_estudiantes,
            self.abrir_cursos,
            self.abrir_calificaciones,
            self.abrir_reportes
        )
        principal.mainloop()

    # =================== ESTUDIANTES ===================

    # Abre la ventana de estudiantes, conecta los botones y llena la tabla
    def abrir_estudiantes(self, ventana_padre):
        self.__vista_estudiante = EstudianteVista(ventana_padre)
        self.__vista_estudiante.configurar_eventos(
            self.guardar_estudiante,
            self.consultar_estudiante,
            self.modificar_estudiante,
            self.eliminar_estudiante,
            self.limpiar_campos_estudiante,
            self.salir_estudiante)
        
        self.__vista_estudiante.mostrar_tabla(self.__registro_estudiante.obtener_lista())

    # Revisa que la fecha tenga el formato dd/mm/aaaa validos
    # Devuelve True si está bien y False si está mal.
    
    def validar_fecha(self, fecha):
        try:
            partes = fecha.split("/")
            
            if len(partes) != 3:
                return False

            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])

            date(anio, mes, dia)

            return True

        except ValueError:
            return False

    # Botón Guardar
    def guardar_estudiante(self):
        carnet = self.__vista_estudiante.obtener_carnet()
        nombre = self.__vista_estudiante.obtener_nombre()
        edad = self.__vista_estudiante.obtener_edad()
        carrera = self.__vista_estudiante.obtener_carrera()
        correo = self.__vista_estudiante.obtener_correo()

        if carnet == "" or nombre == "" or edad == "" or carrera == "" or correo == "":
            self.__vista_estudiante.mostrar_error("Debe llenar todos los campos.")
            return

        if self.validar_fecha(edad) == False:
            self.__vista_estudiante.mostrar_error("La fecha de nacimiento debe tener el formato dd/mm/aaaa.")
            return

        # El Modelo es quien crea el objeto Estudiante y lo guarda en la lista
        if self.__registro_estudiante.guardar_estudiante(carnet, nombre, edad, carrera, correo) == False:
            self.__vista_estudiante.mostrar_error("Ya existe un estudiante con ese carné.")
            return

        self.__vista_estudiante.mostrar_mensaje("Estudiante guardado correctamente.")
        self.__vista_estudiante.limpiar_campos()
        self.__vista_estudiante.mostrar_tabla(self.__registro_estudiante.obtener_lista())
        
        # Actualiza los carnés disponibles en el ComboBox de calificaciones.
        self.actualizar_combos_calificacion()

    # Botón Consultar
    def consultar_estudiante(self):
        carnet = self.__vista_estudiante.obtener_carnet()

        if carnet == "":
            self.__vista_estudiante.mostrar_error("Digite el carné que desea consultar.")
            return

        estudiante = self.__registro_estudiante.buscar_por_carnet(carnet)

        if estudiante == None:
            self.__vista_estudiante.mostrar_error("No existe un estudiante con ese carné.")
        else:
            self.__vista_estudiante.mostrar_estudiante(estudiante)           # llena los campos
            self.__vista_estudiante.mostrar_mensaje(str(estudiante))         # aquí se ve la edad calculada

    # Botón Modificar: primero se consulta (llena los campos), se cambian los datos y luego se modifica
    def modificar_estudiante(self):
        carnet = self.__vista_estudiante.obtener_carnet()
        nombre = self.__vista_estudiante.obtener_nombre()
        edad = self.__vista_estudiante.obtener_edad()
        carrera = self.__vista_estudiante.obtener_carrera()
        correo = self.__vista_estudiante.obtener_correo()

        if carnet == "" or nombre == "" or edad == "" or carrera == "" or correo == "":
            self.__vista_estudiante.mostrar_error("Primero consulte al estudiante y luego modifique sus datos.")
            return

        if self.validar_fecha(edad) == False:
            self.__vista_estudiante.mostrar_error("La fecha de nacimiento debe tener el formato dd/mm/aaaa.")
            return

        estudiante = self.__registro_estudiante.modificar_estudiante(carnet, nombre, edad, carrera, correo)

        if estudiante == None:
            self.__vista_estudiante.mostrar_error("No existe un estudiante con ese carné.")
        else:
            self.__vista_estudiante.mostrar_mensaje("Estudiante modificado correctamente.")
            self.__vista_estudiante.limpiar_campos()
            self.__vista_estudiante.mostrar_tabla(self.__registro_estudiante.obtener_lista())

    
    
    # Botón Eliminar
    def eliminar_estudiante(self):
        carnet = self.__vista_estudiante.obtener_carnet()

        if carnet == "":
            self.__vista_estudiante.mostrar_error("Digite el carné que desea eliminar.")
            return

        if self.__registro_estudiante.buscar_por_carnet(carnet) == None:
            self.__vista_estudiante.mostrar_error("No existe un estudiante con ese carné.")
            return

        # Pide confirmación antes de eliminar.
        #Si el usuario presiona Sí, busca todas las calificaciones de ese estudiante y las elimina.
        if self.__vista_estudiante.confirmar_eliminacion() == True:

            # Obtiene la lista de calificaciones.
            calificaciones = self.__registro_calificacion.obtener_lista()

            # Recorre una copia para eliminar las calificaciones del estudiante.
            for calificacion in calificaciones[:]:
                if calificacion.get_carnet_estudiante() == carnet:
                    self.__registro_calificacion.eliminar_calificacion(carnet,calificacion.get_codigo_curso(),calificacion.get_ciclo(),calificacion.get_annio())

            # Elimina al estudiante.
            self.__registro_estudiante.eliminar_estudiante(carnet)

            self.__vista_estudiante.mostrar_mensaje("Estudiante y sus calificaciones eliminados correctamente.")

            # Limpia los campos y actualiza la tabla.
            self.__vista_estudiante.limpiar_campos()
            self.__vista_estudiante.mostrar_tabla(self.__registro_estudiante.obtener_lista())

            # Actualiza los carnés disponibles en el ComboBox de calificaciones.
            self.actualizar_combos_calificacion()
    
    

    # Botón Limpiar
    def limpiar_campos_estudiante(self):
        self.__vista_estudiante.limpiar_campos()

    # Botón Salir
    def salir_estudiante(self):
        self.__vista_estudiante.salir()

    # =================== REPORTES ===================

    # Abre la ventana de reportes y conecta los botones
    def abrir_reportes(self, ventana_padre):
        self.__vista_reportes = ReportesVista(ventana_padre)
        self.__vista_reportes.configurar_eventos(
            self.generar_reporte,
            self.salir_reportes
        )

    # Botón Generar reporte: según el Radiobutton elegido, pide el reporte al registro que corresponde
    def generar_reporte(self):
        opcion = self.__vista_reportes.obtener_opcion()
        calificaciones = self.__registro_calificacion.obtener_lista()

        match opcion:
            case "listado":
                lineas = self.__registro_estudiante.reporte_listado()
            case "aprobados":
                lineas = self.__registro_estudiante.reporte_aprobados(calificaciones)
            case "reprobados":
                lineas = self.__registro_estudiante.reporte_reprobados(calificaciones)
            case "promedio":
                lineas = self.__registro_curso.reporte_promedio_por_curso(calificaciones)
            case _:
                lineas = ["Cantidad total de cursos registrados: " + str(self.__registro_curso.cantidad_cursos())]

        if len(lineas) == 0:
            lineas = ["No hay datos para mostrar en este reporte."]

        self.__vista_reportes.mostrar_resultado(lineas)

    # Botón Salir
    def salir_reportes(self):
        self.__vista_reportes.salir()

            # =================== CALIFICACIONES ===================

    # Abre la ventana de calificaciones, conecta los botones y llena las listas y la tabla
    def abrir_calificaciones(self, ventana_padre):
        self.__vista_calificacion = CalificacionVista(ventana_padre)
        self.__vista_calificacion.configurar_eventos(
            self.guardar_calificacion,
            self.consultar_calificacion,
            self.modificar_calificacion,
            self.eliminar_calificacion,
            self.limpiar_campos_calificacion,
            self.salir_calificacion
        )
        self.actualizar_combos_calificacion()
        self.actualizar_tabla_calificacion()

    # Llena las listas desplegables con los carnets y códigos que ya están registrados.
    # Así la vista de calificaciones se conecta con estudiantes y cursos solo a través del controlador.
    def actualizar_combos_calificacion(self):
        
         # Evita actualizar los ComboBox si la ventana de calificaciones está cerrada.
        if self.__vista_calificacion is None:
            return
        
        carnets = []
        
        for estudiante in self.__registro_estudiante.obtener_lista():
            carnets.append(estudiante.get_carnet())

        codigos = []
        for curso in self.__registro_curso.listar_cursos():
            codigos.append(curso.get_codigo())

        self.__vista_calificacion.cargar_carnets(carnets)
        self.__vista_calificacion.cargar_cursos(codigos)

    # Vuelve a llenar la tabla. La calificación solo guarda el carnet y el código,
    # por eso se arman dos diccionarios para mostrar también el nombre del estudiante y del curso.
    def actualizar_tabla_calificacion(self):
        nombres_estudiantes = {}
        for estudiante in self.__registro_estudiante.obtener_lista():
            nombres_estudiantes[estudiante.get_carnet()] = estudiante.get_nombre()

        nombres_cursos = {}
        for curso in self.__registro_curso.listar_cursos():
            nombres_cursos[curso.get_codigo()] = curso.get_nombre()

        self.__vista_calificacion.mostrar_tabla(
            self.__registro_calificacion.obtener_lista(),
            nombres_estudiantes,
            nombres_cursos
        )

    # Revisa que la nota sea un número entre 0 y 100. Devuelve True si está bien y False si está mal.
    def validar_nota(self, nota):
        try:
            valor = float(nota)         # si no se puede convertir a número, da error y cae en except
        except ValueError:
            return False

        return valor >= 0 and valor <= 100

    # Revisa que el año tenga 4 dígitos (solo números)
    def validar_annio(self, annio):
        return annio.isdigit() and len(annio) == 4

    # Botón Guardar
    def guardar_calificacion(self):
        carnet = self.__vista_calificacion.obtener_carnet()
        codigo = self.__vista_calificacion.obtener_curso()
        nota = self.__vista_calificacion.obtener_nota()
        ciclo = self.__vista_calificacion.obtener_ciclo()
        annio = self.__vista_calificacion.obtener_annio()

        if carnet == "" or codigo == "" or nota == "" or ciclo == "" or annio == "":
            self.__vista_calificacion.mostrar_error("Debe llenar todos los campos.")
            return

        if self.validar_nota(nota) == False:
            self.__vista_calificacion.mostrar_error("La nota debe ser un número entre 0 y 100.")
            return

        if self.validar_annio(annio) == False:
            self.__vista_calificacion.mostrar_error("El año debe tener 4 dígitos, por ejemplo 2026.")
            return

        # No se registran calificaciones de estudiantes o cursos que no existen
        if self.__registro_estudiante.buscar_por_carnet(carnet) == None:
            self.__vista_calificacion.mostrar_error("No existe un estudiante con ese carné.")
            return

        if self.__registro_curso.buscar_por_codigo(codigo) == None:
            self.__vista_calificacion.mostrar_error("No existe un curso con ese código.")
            return

        # La nota se guarda como número (float) y el año como texto (str).
        # El Modelo crea el objeto Calificacion; devuelve False si ya existe esa misma calificación.
        if self.__registro_calificacion.crear_calificacion(carnet, codigo, float(nota), ciclo, annio) == False:
            self.__vista_calificacion.mostrar_error("Ya existe una calificación de ese estudiante en ese curso y período.")
            return

        self.__vista_calificacion.mostrar_mensaje("Calificación guardada correctamente.")
        self.__vista_calificacion.limpiar_campos()
        self.actualizar_tabla_calificacion()

    # Botón Consultar: se identifica la calificación con carnet + curso + ciclo + año
    def consultar_calificacion(self):
        carnet = self.__vista_calificacion.obtener_carnet()
        codigo = self.__vista_calificacion.obtener_curso()
        ciclo = self.__vista_calificacion.obtener_ciclo()
        annio = self.__vista_calificacion.obtener_annio()

        if carnet == "" or codigo == "" or ciclo == "" or annio == "":
            self.__vista_calificacion.mostrar_error("Seleccione el carné, el curso, el ciclo y digite el año para consultar.")
            return

        if self.validar_annio(annio) == False:
            self.__vista_calificacion.mostrar_error("El año debe tener 4 dígitos, por ejemplo 2026.")
            return

        calificacion = self.__registro_calificacion.buscar(carnet, codigo, ciclo, annio)

        if calificacion == None:
            self.__vista_calificacion.mostrar_error("No existe esa calificación.")
        else:
            self.__vista_calificacion.mostrar_calificacion(calificacion)         # llena los campos
            self.__vista_calificacion.mostrar_mensaje(str(calificacion))

    # Botón Modificar: primero se consulta (llena los campos), se cambia la nota y luego se modifica.
    # Solo se puede cambiar la nota; carné, curso y período son lo que identifica la calificación.
    def modificar_calificacion(self):
        carnet = self.__vista_calificacion.obtener_carnet()
        codigo = self.__vista_calificacion.obtener_curso()
        nota = self.__vista_calificacion.obtener_nota()
        ciclo = self.__vista_calificacion.obtener_ciclo()
        annio = self.__vista_calificacion.obtener_annio()

        if carnet == "" or codigo == "" or nota == "" or ciclo == "" or annio == "":
            self.__vista_calificacion.mostrar_error("Primero consulte la calificación y luego modifique la nota.")
            return

        if self.validar_nota(nota) == False:
            self.__vista_calificacion.mostrar_error("La nota debe ser un número entre 0 y 100.")
            return

        if self.validar_annio(annio) == False:
            self.__vista_calificacion.mostrar_error("El año debe tener 4 dígitos, por ejemplo 2026.")
            return

        # El Modelo devuelve False si no encontró la calificación
        if self.__registro_calificacion.modificar_calificacion(carnet, codigo, ciclo, annio, float(nota)) == False:
            self.__vista_calificacion.mostrar_error("No existe esa calificación.")
        else:
            self.__vista_calificacion.mostrar_mensaje("Calificación modificada correctamente.")
            self.__vista_calificacion.limpiar_campos()
            self.actualizar_tabla_calificacion()

    # Botón Eliminar
    def eliminar_calificacion(self):
        carnet = self.__vista_calificacion.obtener_carnet()
        codigo = self.__vista_calificacion.obtener_curso()
        ciclo = self.__vista_calificacion.obtener_ciclo()
        annio = self.__vista_calificacion.obtener_annio()

        if carnet == "" or codigo == "" or ciclo == "" or annio == "":
            self.__vista_calificacion.mostrar_error("Seleccione el carné, el curso, el ciclo y digite el año de la calificación a eliminar.")
            return

        if self.validar_annio(annio) == False:
            self.__vista_calificacion.mostrar_error("El año debe tener 4 dígitos, por ejemplo 2026.")
            return

        if self.__registro_calificacion.buscar(carnet, codigo, ciclo, annio) == None:
                                               
            self.__vista_calificacion.mostrar_error("No existe esa calificación.")
            return

        # Pide confirmación antes de eliminar
        if self.__vista_calificacion.confirmar_eliminacion() == True:
            self.__registro_calificacion.eliminar_calificacion(carnet, codigo, ciclo, annio)
            self.__vista_calificacion.mostrar_mensaje("Calificación eliminada correctamente.")
            self.__vista_calificacion.limpiar_campos()
            self.actualizar_tabla_calificacion()

    # Botón Limpiar
    def limpiar_campos_calificacion(self):
        self.__vista_calificacion.limpiar_campos()

    # Botón Salir
    def salir_calificacion(self):
        if self.__vista_calificacion is not None:
            self.__vista_calificacion.salir()
            self.__vista_calificacion = None
    # =================== ESTUDIANTES ===================

    # Abre la ventana de estudiantes y llena la tabla
    def abrir_estudiantes(self, ventana_padre):
        self.vista_estudiante = EstudianteVista(ventana_padre, self)
        self.vista_estudiante.mostrar_tabla(self.registro_estudiante.obtener_lista())

    # Botón Registrar
    def registrar_estudiante(self, carnet, nombre, edad, carrera, correo):
        mensaje = self.registro_estudiante.registrar(carnet, nombre, edad, carrera, correo)   # Modelo
        self.vista_estudiante.mostrar_mensaje(mensaje)                                        # Vista
        self.vista_estudiante.mostrar_tabla(self.registro_estudiante.obtener_lista())

        # Los mensajes de éxito siempre llevan la palabra "correctamente"
        if "correctamente" in mensaje:
            self.vista_estudiante.limpiar()

    # Botón Consultar
    def consultar_estudiante(self, carnet):
        estudiante = self.registro_estudiante.buscar_por_carnet(carnet.strip())

        if estudiante is None:
            self.vista_estudiante.mostrar_mensaje("No existe un estudiante con ese carné.")
        else:
            self.vista_estudiante.llenar_campos(estudiante)
            self.vista_estudiante.mostrar_mensaje(str(estudiante))     # aquí se ve la edad calculada

    # Botón Modificar
    def modificar_estudiante(self, carnet, nombre, edad, carrera, correo):
        mensaje = self.registro_estudiante.modificar(carnet, nombre, edad, carrera, correo)
        self.vista_estudiante.mostrar_mensaje(mensaje)
        self.vista_estudiante.mostrar_tabla(self.registro_estudiante.obtener_lista())

        if "correctamente" in mensaje:
            self.vista_estudiante.limpiar()

    # Botón Eliminar (la confirmación ya se preguntó en la vista)
    def eliminar_estudiante(self, carnet):
        mensaje = self.registro_estudiante.eliminar(carnet)
        self.vista_estudiante.mostrar_mensaje(mensaje)
        self.vista_estudiante.mostrar_tabla(self.registro_estudiante.obtener_lista())

        if "correctamente" in mensaje:
            self.vista_estudiante.limpiar()

    # =================== REPORTES ===================

    # Abre la ventana de reportes
    def abrir_reportes(self, ventana_padre):
        self.vista_reportes = ReportesVista(ventana_padre, self)

    # Botón Generar reporte: según el Radiobutton elegido, pide el reporte al registro que corresponde
    def generar_reporte(self, opcion):
        calificaciones = self.registro_calificacion.obtener_lista()

        match opcion:
            case "listado":
                lineas = self.registro_estudiante.reporte_listado()
            case "aprobados":
                lineas = self.registro_estudiante.reporte_aprobados(calificaciones)
            case "reprobados":
                lineas = self.registro_estudiante.reporte_reprobados(calificaciones)
            case "promedio":
                lineas = self.registro_curso.reporte_promedio_por_curso(calificaciones)
            case _:
                lineas = self.registro_curso.reporte_cantidad_cursos()

        if len(lineas) == 0:
            lineas = ["No hay datos para mostrar en este reporte."]

        self.vista_reportes.mostrar_resultado(lineas)
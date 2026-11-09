from modelo.estudiante import Estudiante


class RegistroEstudiante:
    def __init__(self):
        # Lista unidimensional de objetos Estudiante.
        self.estudiantes = []

    # Devuelve la lista completa de estudiantes
    def obtener_lista(self):
        return self.estudiantes

    # Recorre la lista buscando el carné.
    # Devuelve el estudiante si lo encuentra, o None si no existe.
    def buscar_por_carnet(self, carnet):
        for estudiante in self.estudiantes:
            if estudiante.get_carnet() == carnet:
                return estudiante

        return None

    # Revisa que la fecha venga como dd/mm/aaaa (si viene mal, calcular_edad daría error).
    # Devuelve True si está bien y False si está mal.
    def validar_fecha(self, fecha):
        partes = fecha.split("/")

        if len(partes) != 3:            # debe tener día, mes y año
            return False

        for parte in partes:
            if not parte.isdigit():     # cada parte debe ser solo números
                return False

        return True

    # Valida los datos, crea el estudiante y lo agrega a la lista. Devuelve un mensaje.
    
    def registrar(self, carnet, nombre, edad, carrera, correo):
        # strip() quita los espacios al inicio y al final.
        carnet = carnet.strip()
        nombre = nombre.strip()
        edad = edad.strip()
        correo = correo.strip()

        if carnet == "" or nombre == "" or edad == "" or carrera == "" or correo == "":
            return "Debe llenar todos los campos."

        if not self.validar_fecha(edad):
            return "La fecha de nacimiento debe tener el formato dd/mm/aaaa."

        if self.buscar_por_carnet(carnet) is not None:
            return "Ya existe un estudiante con ese carné."

        # El Modelo es quien crea el objeto Estudiante.
        estudiante = Estudiante(carnet, nombre, edad, carrera, correo)
        self.estudiantes.append(estudiante)

        return "Estudiante registrado correctamente."

    # Cambia los datos de un estudiante. El carné no se cambia porque es el que lo identifica.
    def modificar(self, carnet, nombre, edad, carrera, correo):
        carnet = carnet.strip()
        nombre = nombre.strip()
        edad = edad.strip()
        correo = correo.strip()

        if carnet == "" or nombre == "" or edad == "" or carrera == "" or correo == "":
            return "Debe llenar todos los campos."

        if not self.validar_fecha(edad):
            return "La fecha de nacimiento debe tener el formato dd/mm/aaaa."

        estudiante = self.buscar_por_carnet(carnet)

        if estudiante is None:
            return "No existe un estudiante con ese carné."

        estudiante.set_nombre(nombre)
        estudiante.set_edad(edad)
        estudiante.set_carrera(carrera)
        estudiante.set_correo(correo)

        return "Estudiante modificado correctamente."

    # Quita el estudiante de la lista.
    # La confirmación ("¿Desea eliminar?") se le pregunta al usuario en la vista.
    def eliminar(self, carnet):
        carnet = carnet.strip()
        estudiante = self.buscar_por_carnet(carnet)

        if estudiante is None:
            return "No existe un estudiante con ese carné."

        self.estudiantes.remove(estudiante)

        return "Estudiante eliminado correctamente."

    # ---------- REPORTES: cada uno devuelve una lista de textos ----------

    # Listado general de estudiantes (usa el __str__, que ya trae la edad)
    def reporte_listado(self):
        lineas = []

        for estudiante in self.estudiantes:
            lineas.append(str(estudiante))

        return lineas

    # Estudiantes aprobados (nota mayor o igual a 70).
    # Recibe la lista de calificaciones, que se la pasa el controlador.
    def reporte_aprobados(self, calificaciones):
        lineas = []

        for calificacion in calificaciones:
            if calificacion.get_nota() >= 70:
                lineas.append(f"Carné: {calificacion.get_carnet_estudiante()} - "
                              f"Curso: {calificacion.get_codigo_curso()} - "
                              f"Nota: {calificacion.get_nota():.2f}")

        return lineas

    # Estudiantes reprobados (nota menor a 70)
    def reporte_reprobados(self, calificaciones):
        lineas = []

        for calificacion in calificaciones:
            if calificacion.get_nota() < 70:
                lineas.append(f"Carné: {calificacion.get_carnet_estudiante()} - "
                              f"Curso: {calificacion.get_codigo_curso()} - "
                              f"Nota: {calificacion.get_nota():.2f}")

        return lineas
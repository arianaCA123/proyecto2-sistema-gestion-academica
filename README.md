# Sistema de Gestión Académica

Aplicación de escritorio desarrollada en Python con Tkinter para administrar información académica: estudiantes, cursos y calificaciones. Proyecto #2 del curso Desarrollo de Software II (Informática Empresarial), II ciclo lectivo 2026.

## Integrantes

| Nombre | Carné |
|---|---|
| Ariana Carrillo Azofeifa | C5D753 |
| Michelle Hernández | C4I585 |
| Carlos Alvarado | C30348 |

## Características

- **Gestión de estudiantes:** registrar, consultar por carnet (con la edad calculada a partir de la fecha de nacimiento), modificar, eliminar y listar.
- **Gestión de cursos:** registrar, consultar por código, modificar, eliminar y listar.
- **Gestión de calificaciones:** registrar, consultar, modificar, eliminar y listar.
- **Reportes:** listado general de estudiantes, promedio de notas por curso, estudiantes aprobados (nota >= 70), estudiantes reprobados y cantidad total de cursos.
- **Validaciones:** no se permiten carnets ni códigos de curso duplicados, no se registran calificaciones de estudiantes o cursos inexistentes, la nota debe estar entre 0 y 100, se informa cuando un registro no existe y se solicita confirmación antes de eliminar.

## Arquitectura

El proyecto sigue el patrón Modelo–Vista–Controlador (MVC) y aplica Programación Orientada a Objetos (atributos privados, constructor, getters, setters y `__str__`).

- **modelo/**: clases del dominio (`Estudiante`, `Curso`, `Calificacion`) y clases de registro que administran las listas en memoria y crean los objetos.
- **vista/**: ventanas de Tkinter (principal, estudiantes, cursos, calificaciones y reportes).
- **controlador/**: coordina la comunicación entre la vista y el modelo.
- **main.py**: punto de entrada de la aplicación.

```
proyecto_2/
│
├── modelo/
│   ├── estudiante.py
│   ├── curso.py
│   ├── calificacion.py
│   ├── registro_estudiante.py
│   ├── registro_curso.py
│   └── registro_calificacion.py
│
├── vista/
│   ├── principal.py
│   ├── estudiante_vista.py
│   ├── curso_vista.py
│   ├── calificacion_vista.py
│   └── reportes_vista.py
│
├── controlador/
│   └── app_controlador.py
│
└── main.py
```

## Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)

No requiere bases de datos, archivos ni librerías externas. La información se almacena únicamente en memoria, mediante listas unidimensionales de objetos, mientras el programa está en ejecución.

## Ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/<usuario>/sistema-gestion-academica-python.git
   cd sistema-gestion-academica-python
   ```

2. Ejecutar la aplicación desde la raíz del proyecto:

   ```bash
   python main.py
   ```

   En algunos sistemas el comando es `python3 main.py`.

## Notas

Proyecto académico. Los datos no se guardan: al cerrar la aplicación se pierden.

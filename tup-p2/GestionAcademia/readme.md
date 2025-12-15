## Sistema de Gestión de Cursos en una Academia
Diseñar un sistema para gestionar cursos de una academia online, incluyendo la asignación de cupos disponibles.

### Requisitos:
- Cada curso tiene un nombre, un mes y año de inicio y un cupo máximo de estudiantes, que por default es 30.
- Cada estudiante tiene un nombre, un apellido y correo electrónico.
- Se puede inscribir un estudiante en un curso si hay cupo disponible y la fecha actual no es mayor al inicio del mismo.
- Los estudiantes pueden darse de baja de un curso.
- Además de cursos la Academia ofrece webinars, que tienen nombre, mes y año de inicio, pero no tienen cupo máximo de estudiantes. Un estudiante puede inscribirse y darse de baja de un webinar.
- Para emitir certificados se necesita saber si un estudiante completó el curso o webinar, por eso se tiene además de una lista de inscriptos una lista de finalización que contiene a los estudiantes que finalizaron el curso / webinar.
# **Parte 3: Sistema de Gestión de Inventario - Python

Tiempo: 45 minutos
Puntaje: 10 puntos | Aprobación: 6+ puntos

OBJETIVO

Implementar un sistema de gestión de inventario para una tienda de electrónica que maneje diferentes tipos de dispositivos, aplicando los principios de Programación Orientada a Objetos.

REQUERIMIENTOS DEL SISTEMA

Características Comunes:

* Todos los dispositivos comparten: marca, modelo, precio y estado (inicialmente "apagado")
* Cada dispositivo debe poder encenderse y mostrar su información específica

Dispositivos Específicos:

Smartphone:

* Capacidad de almacenamiento en GB
* Capacidad de instalar aplicaciones
* Información debe incluir cantidad de apps instaladas

Tablet:

* Tamaño de pantalla en pulgadas
* Modo tablet especial
* Información debe incluir tamaño de pantalla

Funcionalidades del Programa Principal:

1. Crear al menos 3 dispositivos de diferentes tipos
2. Mostrar información detallada de cada dispositivo
3. Instalar aplicaciones en los smartphones
4. Cambiar el estado de todos los dispositivos

ESTRUCTURA DE ARCHIVOS

Se proporcionan 4 archivos para implementar la solución:

* dispositivo.py - Clase base (completamente implementada)
* smartphone.py - Clase para smartphones (a implementar)
* tablet.py - Clase para tablets (a implementar)
* main.py - Programa principal (a implementar)

RÚBRICA DE EVALUACIÓN

PUNTOS OBLIGATORIOS (5 puntos):

* Main - Recorrer lista y mostrar información (2 pts)
* Constructores con herencia correcta (3 pts)

PUNTOS ADICIONALES (5 puntos):

* Métodos mostrar_info() con polimorfismo (2 pts)
* Instalar aplicaciones en smartphone (1 pt)
* Método modo_tablet() implementado (1 pt)
* Método encender() funcionando (1 pt)
* Código funcionando sin errores (1 pt)

CONDICIÓN DE APROBACIÓN:

Mínimo 6 puntos - Debe cumplir puntos obligatorios (5 pts) + al menos 1 punto adicional

Descargar Plantilla Aquí

Nota: La plantilla contiene la estructura base. Debe analizar las relaciones entre clases para una implementación óptima.

**

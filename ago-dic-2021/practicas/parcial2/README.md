# Parcial 2 Parte 1

## Descripción
En un archivo tenemos guardadas las calificaciones de los alumnos, en un formato como este:

```
<nombre_alumno> <materia> <calificacion>
<nombre_alumno> <materia> <calificacion>
<nombre_alumno> <materia> <calificacion>
<nombre_alumno> <materia> <calificacion>
...
```


Haz un pequeño programa que lea el contenido de este archivo y muestre el promedio de cada alumno.

### Especificaciones
El archivo tiene por lo menos una linea.

El nombre del alumno, la materia y la calificación está separada por un espacio cada uno.

Todas las calificaciones de un alumno están siempre seguidas.

La calificación es un flotante con 2 decimales siempre.

### Ejemplo
#### Entrada
```
Jose_Lopez quimica 89.00
Jose_Lopez matematicas 85.34
Maria_Martinez fisica 95.50
Maria_Martinez español 90.00
```
#### Salida
```
Jose_Lopez 87.17
Maria_Martinez 92.75
```
### Pruebas
Realiza las pruebas unitarias de la función utilizando un Mock para simular el archivo con los datos. Recuerda de poner casos de prueba que abarquen lo más que se pueda del dominio del programa.

# Parcial 2 Parte 2
Define una Interfaz `Escritor`, esta tiene que tener un método `Escribir` que tome un string como parámetro. Luego Define una función que utilize esta interfaz (tome algún texto del usuario y haga algún cálculo) y lo *escriba* en algún lado por medio de esa Interfaz.

Tendrás que definir:
 - Interfaz Escritor
 - Función que utiliza la interfaz
 - por lo menos una *implementación* de la interfaz `Escritor` (escribir a pantalla, a un archivo, a una petición HTTP, a una imagen, a binario, etc.)
 - un mock de la interfaz (otra implementación)

Ejemplifica unas pruebas de integración sobre la función y la implementación principal con los elementos que definiste arriba.
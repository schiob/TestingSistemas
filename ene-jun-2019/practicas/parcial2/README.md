# Parcial 2

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
### Primera Parte
Realiza las pruebas unitarias de la función utilizando un Mock para simular el archivo con los datos. Recuerda de poner casos de prueba que abarquen lo más que se pueda del dominio del programa.

### Segunda Parte
Realiza pruebas de integración sobre la función preparando el ambiente de las pruebas, creando el archivo mencionado, y limpiando borrando el archivo de pruebas al final.
# Práctica 4
Seguimos practicando con los tests unitarios. La práctica se divide en 2 partes:

## Parte 1 - archivos.py
Escriban un programa que reciba en una línea 2 flotantes representando la altura en metros y el peso en kg, calcula el IMC y guárdalo en un archivo `imc.txt` con 2 puntos decimales de presición.

### Input
Una sola linea con 2 flotantes separados por espacios.

### Output
Nada a STDOUT todo tiene que escribirse en el archivo `imc.txt`.

### Ejemplos

#### Entrada
```
1.80 73
```
#### Salida
`22.53` En el archivo

## Parte 2 - test_archivos.py

Implementa un test unitario sobre la función de la parte 1 puedes guiarte de [aquí](https://docs.python.org/3/library/unittest.html).

Pon varios casos de prueba tratando de cubrir la mayor cantidad de posibles entradas.

### Puntos Importantes
En las pruebas usar el método `setUp` para preparar el ambiente de pruebas (checar que los archivos no existan) y `tearDown` para limpiar las pruebas (borrar los archivos que se generaron).

documentación: https://docs.python.org/3/library/unittest.html

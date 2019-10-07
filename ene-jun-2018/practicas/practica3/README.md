# Práctica 3
En esta práctica van a hacer su primer test unitario. La práctica se divide en 2 partes:

## Parte 1 - triangulo.py
Recuerdan el programa de dado 3 lados de un triángulo decir qué tipo de triángulo es? Bueno implementen esa función:

Escriban un programa que reciba en una línea 3 enteros representando los lados del triángulo y muestre qué tipo de triángulo es.

### Input
Una sola linea con 3 enteros separados por espacios. Cada enero
n<sub>i</sub> puede estar en el rango `-100 <= n <= 100`.

### Output
Imprime en una sola linea una de las siguientes opciones:
 - `equilátero`
 - `isósceles`
 - `escaleno`
 - `no triángulo`

### Ejemplos

#### Entrada
```
3 3 3
```
#### Salida

```
equilátero
```
#### Entrada
```
1 2 3
```
#### Salida

```
no triángulo
```

### Puntos Importantes
Toda la lógica para procesar encapsularla en una función, dejando la lectura de stdin y la escritura a stdout fuera de la función.

Esta función debe de tomar como parámetros la lista de lados o 3 enteros, y regresar el string del resultado.


## Parte 2 - test_triangulo.py

Implementa un test unitario sobre la función de la parte 1 puedes guiarte de [aquí](https://docs.python.org/3/library/unittest.html).

Pon varios casos de prueba tratando de cubrir la mayor cantidad de posibles entradas.

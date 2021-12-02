# Práctica 3
Primera práctica de Unit testing. Desarrolla el siguiente programa e implementa los casos de prueba que están más abajo.

## Parte 1 - Problema
A Juanita le gustan mucho los números y todas las propiedades que pueden tener. Algunos son pares, otros son negativos, inclusive hay algunos que son primos!!! Juantita tiene una lista de **n** números y quiere saver cuántos de esos números tienen determinadas propiedades.

Ayuda a Juanita a procesar la lista para que no se tarde tanto tiempo en leer toda la lista.

### Input
La entrada consiste en 2 lineas.

La primera línea tiene un número entero **n** que representa la cantidad de números que tiene la lista.

La segunda línea contiene **n** enteros separados por espacios.

### Output
Imprime los siguientes datos.

 - Cuántos números son positivos
 - Cuántos números son negativos
 - Cuántos números son pares
 - Cuántos números son impares

Cada uno en una línea con el formato:
`n número(s) positivos`


### Ejemplo de entrada:

```
5
51 -12 -3 0 2
```

### Ejemplo de salida:

```
2 número(s) positivo(s)
2 número(s) negativo(s)
3 número(s) par(es)
2 número(s) impar(es)
```


## Parte 2 - Unit tests
Aobre el programa de Juanita, implementa los siguientes casos de prueba en pruebas unitarias sobre la función que hayas hecho para calcular la cantidad de números:

```
<(entrada), (salida esperada)>
```

```
<(51, -12, -3, 0, 2), 

"2 número(s) positivo(s)
2 número(s) negativo(s)
3 número(s) par(es)
2 número(s) impar(es)">
```

```
<(0, 1, 2, 3, 4), 

"4 número(s) positivo(s)
0 número(s) negativo(s)
3 número(s) par(es)
2 número(s) impar(es)">
```

```
<(-1, -2, -3), 

"0 número(s) positivo(s)
3 número(s) negativo(s)
1 número(s) par(es)
2 número(s) impar(es)">
```

```
<(0), 

"0 número(s) positivo(s)
0 número(s) negativo(s)
1 número(s) par(es)
0 número(s) impar(es)">
```
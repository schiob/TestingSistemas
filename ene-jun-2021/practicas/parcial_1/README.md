# Primer parcial
Resuelve los siguientes problemas y aplica los casos de prueba que están al final.

## Problema 1
A Pedrito le gustan los números triangulares [(wikipedia)](https://es.wikipedia.org/wiki/N%C3%BAmero_triangular), pero para saber cuál es el número triangular **n** tiene hacer un cálculo a mano, así que te pide que le ayudes a hacer un programa para facilitarle la tarea:

### Entrada
Recibirás una sola línea con un entero **n** representado la posición del número triangular
#### Ejemplos
`
1
`

`
3
`

`
4
`
### Salida
Imprime una sola linea con el entero que es el **n** número triangular.

#### Ejemplos

`
1
`

`
6
`

`
10
`

### Casos de pruebas
<1, 1>

<3, 6>

<4, 10>

<56, 1596>

<400, 80200>

## Problema 2 | Mocks

Escribe un programita que lea un archivo `csv` que tiene el siguiente formato:

```
usuario,correo,puntos
Tom,tomas@hotmail.com,85
Juan,juan@hotmail.com,75
Maria,maria84@gmail.com,90
Paco,paquito123@outlook.com,74
Ana,anaa22@gmail.com,88
Marcos,marcosss@hotmail.com,92
```

Y calcule el promedio de calificación dependiendo del dominio del correo del usuario. Y muestre un resultado como este:

```
hotmail.com 84.0
gmail.com 89.0
outlook.com 74.0
```

Una vez tengas el programa ejecuta las pruebas unitarias, utiliza un Mock para reemplazar el archivo donde está la entrada de datos.

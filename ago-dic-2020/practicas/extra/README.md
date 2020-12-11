# Extra
Resuelve los siguiente problemas y aplica los casos de prueba correspondientes.

## Problema 1
Queremos conocer la suma de todos los número impares entre dos enteros. Sin incluir estos números.

### Entrada
Recibirás una sola linea con dos enteros **x**, **y** corresponiente a los dos extremos del rango.
#### Ejemplos
`
6 -5
`

`
12 15
`

`
12 12
`
### Salida
Imprime una sola linea con el resultado de la suma de los números impares.

#### Ejemplos

`
5
`

`
13
`

`
0
`

### Casos de pruebas
Entrada y salida esperada:

<(6 -5), 5>

<(12 15), 13>

<(12 12), 0>

<(123 321), 21756>

<(4321 1234), 4284911>

<(-19289 7853), -77593260>

## Problema 2
Un archivo tiene guarda una lista de deseos en para el intercambio de este año, quieres que te regalen el regalo más caro pero ese ya te lo ganaron, así que busca el segundo más caro y muestralo en la pantalla.


### Entrada
El archivo tiene por lo menos una linea y no más de 100 lineas y cada linea tiene un string, seguido de un espacio y el precio del producto con puntos decimales.

### Ejemplo de archivo:

```
controlRemoto 450.00
hamburguesa 90.00
Switch 6999.99
tarjetaRegalo 500.00
PixelCelular 15000.00
```

### Salida
Muestra el nombre del segundo elemento más grande. Si hay dos con el mismo precio puedes tomar cualquiera de los 2.

### Ejemplo
Switch

### Notas
Utiliza un mock para hacer las pruebas y crea un número suficiente de casos de prueba.
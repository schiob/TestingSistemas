# Parcial 1 | Otro más
Realiza el siguiente ejercicio y realiza pruebas unitarias correspondientes con los casos de pruebas que consideres necesarios.

## Ejercicio 1
Escribe un programa que reciba por stdin el pedido de tacos de un cliente e imprima el total.

### Input
Una sola linea con `n` palabras separados por espacios, donde `0 < n <= 30`. (O sea que te puedo pasar entre 1 ó 30 palabras)

Cada palabra puede ser alguna de las opciones de este menú:

 - `cachete`
 - `lengua`
 - `tripitas`
 - `pastor`
 - `machito`

Cada taco tiene un precio dependiendo de qué es:
 - cachete: `13`
 - lengua: `10`
 - tripitas: `9`
 - pastor: `15`
 - machito: `14`

### Output
Imprime en una sola linea un entero representanto el total que tiene que pagar el cliente.


### Ejemplos

#### Entrada
```
cachete lengua cachete tripitas machito machito machito cachete lengua
```
#### Salida

```
110
```

## Ejercicio 2
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
# Práctica 2
Escriban el siguiente programa tomando en cuenta los `Puntos Importantes` que se indican al final.

## taquitos.py
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

# Pruebas
Realiza las pruebas unitarias de la función con los casos de pruebas que creas necesarias.
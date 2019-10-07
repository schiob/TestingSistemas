# Práctica 2
Preparándonos para empezar a hacer pruebas unitarias y con el fin de que sigan practicado python, git y github, escriban el siguiente programa tomando en cuenta los `Puntos Importantes` que se indican al final.

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

## Puntos Importantes
Toda la lógica para procesar encapsularla en una función, dejando la lectura de stdin y la escritura a stdout fuera de la función.

Esta función debe de tomar como parámetros la lista de tacos, y regresar el entero del total.

Puedes usar de ejemplo el programa `este_ejemplo.py`

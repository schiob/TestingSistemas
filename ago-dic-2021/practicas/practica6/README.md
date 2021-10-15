# Practica 6

Escribe un sistema que se conforme por 5 `funciones` (unidades a probar). Y realiza pruebas unitarias sobre todas las funciones.

Este sistema va a tener una lista de usuarios los cuales tienen mayor o menor prioridad, y un pool de posibles viajes a los que pueden conectarse. Tu programa tiene que conectar los usuarios a los viajes de acuerdo a ciertas reglas definidas en la función principal:

## Funcion Principal
La primera será una función principal que se encargará de emparejar usuarios con sus viajes.
Esta función principal, extrae el usuario de mayor prioridad de la función `siguiente_usuario`, y lo enlaza con el viaje con la menor tarifa, esta lista de viajes los extrae de la función `viajes_disponibles`. La función regresa una lista de usuarios con el id del viaje al que se emparejaron.

### Entrada
No tiene entrada

### Salida
una lista de usuarios con el id del viaje al que se emparejaron: 

```
Tom - viaje 234
Susana - viaje 722
Andres - viaje 210
Pepe - viaje 92
```

## Funcion siguiente_usuario
Esta función regresa el siguiente usuario que tiene mayor prioridad en la lista de usuarios. Esta lista está cargada en un archivo que contiene la siguiente estructura:

```
Tom 4
Susana 2
Andres 10
Pepe 3
Luis 2
```

Donde la primera palabra de cada renglón es el nombre del usuario y la segunda es el nivel de prioridad entre 1 y 10, donde 10 es la prioridad más baja. Una vez que la función regrese el nombre del usuario este se eliminará de la lista.

Si hay 2 o más usuarios con la misma prioridad, se extrae el primer usuario entre ellos.

### Entrada
Nada
### Salida
Un solo string que contenga el nombre del usuario:

```
Tom
```

## Funcion viajes_disponibles
Esta función regresa los viajes disponibles los cuales se calculan con conductores y tarifa. La lista de conductores los extrae de la función `extraer_conductores` y luego calcula la tarifa de cada conductor pasando su antigüedad por la función `calcular_tarifa` una vez teniendo estos dos datos, los regresa en una lista con el id del viaje y la tarifa.

El id del viaje inicia en `1` y se incrementan conforme se van calculando.

### Entrada
Nada

### Salida
Una lista de Viajes con su id y su tarifa:

```
[
    [1, 50],
    [2, 75],
    [3, 40],
    [4, 100]
]
```

## Función extraer_conductores
Esta función regresa la lista de conductores la cuál el programa extrae de un archivo que tiene el siguiente formato:

```
Juan 3
Jesus 2
Maria 3
Toño 1
```

Donde la primera palabra es el nombre y la segunda es el número de años que tiene trabajando.

### Entrada
Nada

### Salida
Una lista con los conductores

```
[
    ["Juan", 3],
    ["Jesus", 2],
    ["Maria", 3],
    ["Toño", 1],
]
```

## Funcion calcular_tarifa
Esta función toma un número que corresponde a la antigüedad de un conductor y calcula la tarifa del viaje con la siguiente fórmula:

`tarifa = 20 + (10*antigüedad)`

### Entrada
Un número entero representado la antigüedad

### Salida
Un número entero representado la tarifa
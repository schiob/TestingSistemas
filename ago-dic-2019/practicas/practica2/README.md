# Practica 2 - Pair programming
Carlitos tiene muchos pantalones, cada pantalón es de una márca en especial y un precio por el que lo compró.

El problema es que ya no tiene espacio en su ropero y él quiere comprar más pantalones, así que necesita seleccionar algunos para venderlos y hacer espacio.

Carlitos tiene una serie de reglas:
 - Quiere disminuir la cantidad de pantalones de **N** a **X**
 - No quiere dejar su ropero sin pantalones de una marca que ya tenía, (si tenía 2 pantalones de la marca *Levice*, se quiere quedar por lo menos con 1)
 - Quiere vender primero los pantalones más caros.
 - Y vender como máximo 5 pantalones de cada marca.

Ayuda a Carlitos a hacer ese programa.

Imprime como resultado el número de pantalones que vas a vender, siempre y cuando se pueda. Y si se puede imprime también cuanto dinero sacaste.

## Especificaciones de Entrada
La primera linea tiene 2 enteros separados por un espacio, el número de pantalones **N**, el número pantalones a los que quiere llegar **X**.

Después hay **N** lineas donde en cada una hay un string y un entero separados por un espacio. La marca del pantalón **Ni** y su precio.

## Especificaciones de Salida
Imprime un **0** si no se puede llegar a la meta con las reglas y si sí imprime el número de pantalones que ventiste y la ganancia que escogiste.

## Ejemplo entrada

```
8 5
Patito 4
Patito 5
Levice 15
Patito 5
Levice 3
Nike 20
Nike 18
Levice 4
```

## Ejemplo salida
```
3 40
```
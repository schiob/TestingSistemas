# Ejercicio

App de conteo de calorías.

 - Una comida
  - Entrada (platillo)
  - Plato principal (platillo)
  - Postre (platillo)

 - Platillo
  - Ingrediente 1
  - ingrediente 2
  ...

 - Ingrediente
  - X calorías.


## Entidades
 - Ingrediente
  - Nombre
  - Unidad de medida
  - Calorias x unidad
 - Platillo
  - Nombre
  - []ingredientes Y cantidad
 - Comida
  - []Platillos
 - Dieta
  - TotalDeCaloriasPorDia
  - []ComidasConsumidas

## Acciones
 - Dado una comida calcular las calorias
 - Dada la dieta de una persona y lo que lleva en el día, decir si la comida entra o no en su dieta.
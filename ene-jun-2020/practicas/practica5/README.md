# Práctica 5
Realiza las 3 siguientes funciones y las pruebas tanto unitarias como de integración.

 - Dados los 3 lados de una caja como enteros, calcular el volumen de esa caja.
 - Dada una lista de contenedores y cuánto volumen tiene cada uno, calcular el total de volumen que tenemos.
    - Ejemplo: ((5,4), (2, 3), (6,2)) -> Total 38
    - En ese ejemplo pasan como parámetro 5 contenedores de 4, 2 de 3 y 6 de 2.

 - Una función donde le pasemos como parámetro el lado de 3 cajas cúbicas y el volumen total que queremos guardar. Use las funciones de arriba y calcule una opción de cuántas cajas hay que tener de cada tipo para poder almacenar todo el volumen.
   - Ejemplo: Le pasamos (4, 2, 3, 100) -> ((1,4), (1, 3), (2,2))
   - Explicación: Cada caja de 4 de lado tiene de volumen 64 así que con una basta, la de 3  da 27, así que con una nos acercamos a 100 sin pasarnos, para cumplir con el objetivo solo faltarían 2 cajas de 2 de lado y listo.
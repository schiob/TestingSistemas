# Práctica 4 | Test unitarios con Mocks

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

Una vez tengas el programa ejecuta las pruebas unitarias, unas pruebas hazlas leyendo un archivo real, y en otras pruebas utiliza un Mock para reemplazar esta entrada de datos.

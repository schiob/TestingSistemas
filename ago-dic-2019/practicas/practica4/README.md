# Practica 4 - Unit testing y mocks
La práctica tiene 3 partes, primero desarrollar una pequeña función, luego hacer las pruebas unitarias sin usar mocks y al final volver a hacer las pruebas pero con mocks.

## Parte 1
La función tiene que leer el contenido de un archivo y lo devuelva como resultado eliminando cualquier caracter que no sea alfanumérico ([A-Z][a-z][0-9]), y transformando todas las letras de mayúscula a minúscula.

La función recive como parámetro el path del archivo y regresa el string del contenido aplicando las reglas de arriba.

## Parte 2 
Realizar las pruebas unitarias aplicando varios casos de prueba donde existe el archivo pero no tiene nada, exista el archivo con texto que remover, exista el archivo sin texto que se tenga que cambiar, etc.

## Parte 3 
Realizar las mismas pruebas pero con mocks para no necesitar crear el archivo cada vez.

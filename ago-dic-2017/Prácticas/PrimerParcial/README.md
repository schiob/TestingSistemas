# Primer Parcial
### 1
Hacer un archivo `primer_parcial.py` que tenga una función:

La función recibe el path de un archivo el cual tiene una sola linea. Esta linea tiene 3 enteros separados por un espacio los cuales representan 3 lados de un triángulo. La función debe leer el archivo y regresar un string representando el tipo de triángulo que es de acuerdo con sus lados:

```
Tri_from_file(path string):
  read file
  process content
  return string

```
Posibles resultados:
 - Equilátero
 - Isóceles
 - Escaleno
 - No triángulo

### 2

Aplica los siguientes casos de prueba sobre el programa del Tipo de Triángulo. Puedes usar Mocks para no crear archivos, o puedes preparar el ambiente creando los archivos necesarios con el método setUp:

Formato:

<(nombre del archivo) ”Contenido del archivo”, “string esperado de respuesta”>

Ejemplo:

<(test.txt) ”4 4 4”, “Equilátero”>

Explicación:

Los tres enteros que están en el archivo “test.txt” representan los lados de un triángulo equilátero, así que la función debe regresar el string “Equilátero”.

Casos de prueba:

<(equi1.txt) ”3 3 3”), “Equilátero”>
<(equi2.txt) ”5 5 5”), “Equilátero”>

<(notri1.txt) ”0 0 0”, “No triángulo”>
<(notri2.txt) ”0 5 7”, “No triángulo”>
<(notri3.txt) ”1 2 3”, “No triángulo”>

<(iso1.txt) ”10 7 7”, “Isóceles”>
<(iso2.txt) ”4 5 4“, “Isóceles”>

<(esca1.txt) ”8 6 5”, “Escaleno”>

Separar cada grupo en diferentes pruebas (Métodos de la clase) según su salida:
```
    def TestEquilatero(self):
    # codigo

  def TestNoTri(self):
    # codigo

  def TestIsoceles(self):
    # codigo

  def TestEscaleno(self):
    # codigo
```

Subir el código al repo como con las otras prácticas.

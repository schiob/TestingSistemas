# Práctica 2
### 1
Hacer un archivo `practica2.py` que tenga dos funciones:

La primera recibe el path de un archivo y regresa su contenido como string
```
PrintFile(path string):
  return read(path)

```

La segunda recibe el path de un archivo y un string y no regresa nada pero sobreescribe el string en el archivo
```
WriteFile(path string, str string):
  write(path, string)  # Sobreescribir

```

(El contenido de las funciones mostradas arriba es pseudocódigo para facilitar la explicación)

### 2
Hacer un archivo `test_practica2.py` que aplique los siguientes casos de prueba sobre `practica2.py`:

 - PrintFile
  - <path archivo que tenga escrito "hola tacos", "hola tacos">
  - <path archivo que esté bacío "", "">
  - <path archivo con saltos de línea "hola\nsalto\ntamal", "hola\nsalto\ntamal">

 - WriteFile
  - <(path archivo nuevo, "charmander"), (archivo que tenga escrito "charmander")>
  - <(path de archivo existente, "Ya es viernes"), (archivo que tenga escrito "Ya es viernes")>

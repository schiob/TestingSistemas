# Practica 4 Ejercicio Mock

Utiliza lo que vimos en clase, unittest.mock y unittest.patch para hacer las pruebas unitarias de la siguiente función:

```python
def calc_prom():
    file = open("archivito.txt", "r")
    total = 0
    for linea in file:
        total += int(linea)
    
    return total

if __name__ == "__main__":
    print(calc_prom())
```

Suerte :)
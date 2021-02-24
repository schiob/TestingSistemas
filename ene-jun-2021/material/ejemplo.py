def tipoTriangulo(a: int, b: int, c: int):
    '''Me regresa el tipo de triángulo que es, iso, equi, etc, etc, etc.'''
    if a == 0 and b == 0 and c == 0:
        return "no"
    
    return "cosa"

'''
<(5, 5, 5), "equilátero">
<(1000000, 1000000, 1000000), "equilátero">
<(4, 3, 0), "no">
<(-4, 3, 5), "no">
<(5, 3, 5), "iso">
<(5, 3, 6), "esc">
<(2, 2, 4), "no">
'''
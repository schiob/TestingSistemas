import math


def pract1_vol_cil(radio, altura):
    # Fórmula para el volumen --> pi*r^2*h
    vlmn = math.pi * radio ** 2 * altura
    print("El volumen de tu cilindro es: " + str(vlmn))
    return vlmn


if __name__ == '__main__':
    pract1_vol_cil(5, 9)

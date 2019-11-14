## -*- coding: utf-8 -*-
def archtolst(path):
    f = open(path, "r")
    lines = []
    for x in f:
        lines.append(x)
    f.close()
    return lines


def extrapolate(ls):
    ret = []
    ex = ls.split()
    ret.append(ex[0])
    ret.append(ex[2])
    return ret

def calcularpromedio(ls):
    suma = 0
    for c in ls:
        c = float(c)
        suma += c
    pro = suma / len(ls)
    return pro

def dividirporalumno(ls):
    map = {}
    for ln in ls:
        name, calif = extrapolate(ln)
        if name in map:
            map[name].append(calif)
            #map[name] =
        else:
            temp = []
            temp.append(calif)
            map[name] = temp
    return map

def calcular_imprimir(m):
    l = ""
    for name in m:
        promedio = calcularpromedio(m[name])
        l += "{} {:.2f}".format(name, promedio)
        l += "\n"
    return l

def main(path):
    x = archtolst(path)
    y = dividirporalumno(x)
    z = calcular_imprimir(y)
    return z

if __name__ == '__main__':
    print(main("entrada.txt"))

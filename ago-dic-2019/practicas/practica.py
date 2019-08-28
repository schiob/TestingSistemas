import math

def v_cilindro(radio = None, altura = None):
    if radio == None:
        radio = float( input("Radio: ") )
    if altura == None:
        altura = float( input("Volumen: ") )
    volumen = math.pi * (math.pow(radio, 2)) * altura
    return volumen

print(v_cilindro())
                        

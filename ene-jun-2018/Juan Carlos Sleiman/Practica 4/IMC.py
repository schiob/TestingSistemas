import os

def calcIMC (peso, altura):

        if altura >= 3:
            return "Seguro que eres humano?."
        else:
            res = peso / altura**2
            f = open ('IMC.txt','w')
            f.write('IMC=%.2f' %res)
            f.close()


if __name__ == '__main__':
    peso, altura = input('Pon peso en kg y altura en mts\n').split(' ')
    peso = float(peso)
    altura = float(altura)
    calcIMC(peso, altura)

"""mock_o.assert_called_once_with(text, w)"""

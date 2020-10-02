import csv
import unittest
columnas=['usuario','correo','puntos']
archivo = open("datos.csv")
reader = csv.reader(archivo)
readerList = list(reader)

def promedio(dominio: str, lista):
    try:
        cont = 0
        suma = 0
        for i in lista:
            if dominio in i[1]:
                cont = cont + 1
                suma = suma + int(i[2])
        promedio = (suma/cont)
        return promedio
    except:
        return "Error"

class TestPromedio(unittest.TestCase):
    def test1(self):
        TestCases = [
            {
                "dominio":"@hotmail.com",
                "promedio":84.0
            },
            {
                "dominio":"@gmail.com",
                "promedio":89.0
            },
            {
               "dominio":"@outlook.com",
                "promedio":74.0
            },
            {
                "dominio": 5465454,
                "promedio": "Error"
            }
        ]
        for tc in TestCases:
            salida = promedio(tc["dominio"],readerList)
            self.assertEqual(tc["promedio"],salida)
if __name__ == '__main__':
    unittest.main()
    
    
    
    
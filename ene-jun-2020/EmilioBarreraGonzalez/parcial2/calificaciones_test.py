import unittest
from calificaciones import *
import os

class calificaciones_test(unittest.TestCase):
    def setUp(self):
        file = open("test.txt","w+")
        file.write("TESTING")
        file.close()
        file = open("test2.txt","w+")
        file.write(
            "Emilio_Barrera Matematicas 100\n"+
            "Fernando_Garcia Matematicas 100"
        )
        file.close()
        file = open("test3.txt", "w+")
        file.write(
            "Emilio_Barrera Matematicas 100\n"+
            "Emilio_Barrera Espanol 100\n"+
            "Emilio_Barrera Historia 100\n"+
            "Fernando_Garcia Matematicas 100\n"+
            "Fernando_Garcia Espanol 100\n"+
            "Fernando_Garcia Historia 99\n"+
            "Angela_Sanchez Matematicas 100\n"+
            "Angela_Sanchez Espanol 100\n"+
            "Angela_Sanchez Historia 100"
        )
    def test_lectura_archivo(self):
        salida_esp=["TESTING"]
        salida_act=lectura_archivo("test.txt")
        self.assertEqual(salida_esp,salida_act)

    def test_lectura_materias(self):
        tc = [
            {
                'in':['Emilio_Barrera Matematicas 100'],
                'ex':[{'nombre':'Emilio_Barrera','materia':'Matematicas','calif':'100'}]
            },
            {
                'in':['Emilio_Barrera Matematicas 100','Emilio_Barrera Espanol 100'],
                'ex':[
                    {'nombre':'Emilio_Barrera','materia':'Matematicas','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Espanol','calif':'100'}
                    ]
            }
        ]
        for i in tc:
            actual = lectura_materias(i['in'])
            self.assertEqual(i['ex'],actual)
    
    def test_calc_promedio(self):
        tc =[
            {
                'in':[
                    {'nombre':'Emilio_Barrera','materia':'Matematicas','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Espanol','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Historia','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Fisica','calif':'100'},
                    
                ],
                'ex':[
                    {'nombre':'Emilio_Barrera','promedio':100}
                    ]
            },
            {
                'in':[
                    {'nombre':'Emilio_Barrera','materia':'Matematicas','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Espanol','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Historia','calif':'100'},
                    {'nombre':'Emilio_Barrera','materia':'Fisica','calif':'100'},
                    {'nombre':'Fernando_Garcia','materia':'Fisica','calif':'100'},

                    
                ],
                'ex':[
                    {'nombre':'Emilio_Barrera','promedio':100},
                    {'nombre':'Fernando_Garcia','promedio':100}
                    ]
            },
        ] 
        for i in tc:
            actual = calcular_promedio(i['in'])
            self.assertEqual(i['ex'],actual)
    
    def test_lectura_archivo_and_lectura_materias(self):
        cont = lectura_archivo("test2.txt")
        calif = lectura_materias(cont)
        ex = [
            {'nombre':"Emilio_Barrera",'materia':'Matematicas','calif':'100'},
            {'nombre':"Fernando_Garcia",'materia':"Matematicas",'calif':'100'}
        ]
        self.assertEqual(ex,calif)

    def test_total(self):
        cont= lectura_archivo("test3.txt")
        calif = lectura_materias(cont)
        prom = calcular_promedio(calif)
        ex = [
            {
                "nombre":"Emilio_Barrera",
                "promedio":100.00
            },
            {
                "nombre":"Fernando_Garcia",
                "promedio": 99.67
            },
            {
                "nombre":"Angela_Sanchez",
                "promedio": 100.00
            }
        ] 

    def tearDown(self):
        os.remove("test.txt")
        os.remove("test2.txt")
        os.remove("test3.txt")


if __name__=='__main__':
    unittest.main()
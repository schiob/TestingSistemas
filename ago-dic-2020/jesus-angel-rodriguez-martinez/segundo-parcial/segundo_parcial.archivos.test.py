# -*- coding: utf-8 -*-
import os
from unittest.mock import Mock
import unittest
from segundo_parcial import obtener_promedio

class promedio_test(unittest.TestCase):
    def testPromedio(self):
        test_cases = (
            {"ruta": "seccion_A.txt", "datos" : "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00", "resultado" : "Jose_Lopez 87.17\nMaria_Martinez 92.75"},
            {"ruta": "seccion_B.txt", "datos" : "Jose_Lopez quimica 100.00\nMaria_Martinez fisica 95.50\nSudo_von español 90.00", "resultado" : "Jose_Lopez 100.00\nMaria_Martinez 95.50\nSudo_von 90.00"},
        )
        for tc in test_cases:
            # Se crea el archivo temporal.
            archivo = open(tc["ruta"], "w")
            archivo.write(tc["datos"])
            archivo.close()
            # Se lee el archivo.
            archivo = open(tc["ruta"], "r")
            self.assertEqual(obtener_promedio(archivo), tc["resultado"])
            # Se cierra y elimina el archivo temporal.
            archivo.close()
            os.remove(tc["ruta"])

    def testPromedioSinDatos(self):
        test_cases = (
            {"ruta": "vacio.txt", "datos" : "", "resultado" : "La lista de calificaciones está vacía"},
        )
        for tc in test_cases:
            # Se crea el archivo temporal.
            archivo = open(tc["ruta"], "w")
            archivo.write(tc["datos"])
            archivo.close()
            # Se lee el archivo.
            archivo = open(tc["ruta"], "r")
            self.assertEqual(obtener_promedio(archivo), tc["resultado"])
            # Se cierra y elimina el archivo temporal.
            archivo.close()
            os.remove(tc["ruta"])

    def testPromedioCaracteresInvalidos(self):
        test_cases = (
            {"ruta": "seccion_A.txt", "datos" : "Jose_Lopez quimica @\nJose_Lopez matematicas á\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00", "resultado" : "No es una calificación válida"},
            {"ruta": "seccion_B.txt", "datos" : "Jose_Lopez quimica -100.00\nMaria_Martinez fisica XD\nSudo_von español 90.00", "resultado" : "No es una calificación válida"},
        )
        for tc in test_cases:
            # Se crea el archivo temporal.
            archivo = open(tc["ruta"], "w")
            archivo.write(tc["datos"])
            archivo.close()
            # Se lee el archivo.
            archivo = open(tc["ruta"], "r")
            self.assertEqual(obtener_promedio(archivo), tc["resultado"])
            # Se cierra y elimina el archivo temporal.
            archivo.close()
            os.remove(tc["ruta"])  
if __name__ == "__main__":
    unittest.main()
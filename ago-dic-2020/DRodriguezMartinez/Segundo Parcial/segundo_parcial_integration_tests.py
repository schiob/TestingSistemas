import subprocess
from  unittest import mock, TestCase
from segundo_parcial import calcular_promedio

class segundo_parcial_test(TestCase):
    def createFile(self, data: str):
        subprocess.run(f"echo {data} > temp.txt", shell=True)

    def deleteFile(self):
        subprocess.run("rm temp.txt", shell=True)

    def testChio(self):
        esperado = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}
        data = str(bytes("Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez espanol 90.00", "latin-1"))[1:]

        self.createFile(data)
        real = calcular_promedio("temp.txt")

        self.deleteFile()
        assert esperado == real 

    def testResultadosNormales(self):
        esperado = {'Daniela_Rodriguez': 95, 'Maria_Martinez': 92.75, 'Persona_1': 85.2} 
        data = str(bytes("Daniela_Rodriguez quimica 95\nDaniela_Rodriguez matematicas 95\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00\nPersona_1 quimica 85.2", "latin-1"))[1:]

        self.createFile(data)

        real = calcular_promedio("temp.txt")

        self.deleteFile()
        assert esperado == real


    def testSinDatos(self):
        esperado = {}
        data = ""

        self.createFile(data)

        real = calcular_promedio("temp.txt")

        self.deleteFile()
        assert esperado == real


    def testCalificacionSinNumeros(self):
        data = str(bytes("Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español A", "latin-1"))[1:]

        self.createFile(data)
        with self.assertRaisesWithMessage(ValueError):
                calcular_promedio("temp.txt")
                self.deleteFile()

    def testNumerosNegativos(self):
        data = str(bytes("Jose_Lopez quimica -89.00\nJose_Lopez matematicas -85.34\nMaria_Martinez fisica -95.50\nMaria_Martinez español -90.00","latin-1"))[1:]

        self.createFile(data)
        with self.assertRaisesWithMessage(ValueError):
                calcular_promedio("temp.txt")
                self.deleteFile()

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
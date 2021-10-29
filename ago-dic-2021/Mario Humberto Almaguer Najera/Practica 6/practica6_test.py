import unittest
from practica6 import Practica6
from unittest.mock import patch

# link diagrama: https://ibb.co/TgsyDpp

class practica6_test(unittest.TestCase):
    
    @patch('practica6.Practica6.siguiente_usuario')
    def test_funcion_principal_siguente_usuario(self, mock_siguiente_usuario):
        # Cantidad de viajes que queremos crear
        cantidad_viajes = 3

        # Usar el mock para que nos regrese siempre JuanMockeado al llamar siguiente_usuario()
        mock_siguiente_usuario.return_value = 'JuanMockeado'

        # Instanciar Practica6 para usar sus metodos
        pr = Practica6()

        # La funcion_principal depende de siguiente_viaje(), pero el diccionario viajes esta vacio, por eso
        # hay que llamar viajes_disponibles(cantidad_viajes)
        pr.viajes_disponibles(cantidad_viajes)

        # Almacenamos 'JuanMockaedo' en la variable respuesta
        respuesta = pr.siguiente_usuario()

        # Comprobamos que al llamar la funcion_principal nos regrese una lista con Usuario: JuanMockeado | Viaje #
        self.assertEqual(pr.funcion_principal(cantidad_viajes), [
                         'Usuario: {} | Viaje: 1'.format(respuesta), 'Usuario: {} | Viaje: 2'.format(respuesta), 'Usuario: {} | Viaje: 3'.format(respuesta)])

    @patch('practica6.Practica6.siguiente_viaje')
    def test_funcion_principal_siguiente_viaje(self, mock_siguiente_viaje):
        # Cantidad de viajes que queremos crear
        cantidad_viajes = 3

        # Usar el mock para que nos regrese siempre 1 al llamar siguiente_viaje()
        mock_siguiente_viaje.return_value = 1

        # Instanciar Practica6 para usar sus metodos
        pr = Practica6()

        # La funcion_principal depende de siguiente_usuario()
        # Almacenamos 1 en la variable respuesta
        respuesta = pr.siguiente_viaje()

        self.assertEqual(pr.funcion_principal(cantidad_viajes), [
                         'Usuario: Susana | Viaje: 1', 'Usuario: Luis | Viaje: 1', 'Usuario: Pepe | Viaje: 1'])

    @patch('practica6.Practica6.viajes_disponibles')
    def test_siguiente_viaje_viaje_disponibles(self, mock_viajes_disponibles):
        # Cantidad de viajes que queremos crear
        cantidad_viajes = 3

        # Usar el mock para que nos regrese un diccionario con ID_Viaje : Tarifa
        mock_viajes_disponibles.return_value = {1: 60, 2: 65, 3: 80}

        # Instanciamos Practica6 para usar nuestros metodos
        pr = Practica6()

        # Llamamos al metodo viajes_disponibles y lo guardamos en respuesta
        respuesta = pr.viajes_disponibles(cantidad_viajes)

        # Asignar nuestra respuesta al diccionario viajes.
        pr.viajes = respuesta

        # Llamamos al metodo siguiente_viaje de la clase Practica6, deberia de funcionar ya que hicimos un mock
        # de su dependencia viajes_disponibles()
        # Comprobamos que sea el siguiente_viaje sea el viaje ID_Viaje con tarifa mas baja
        # return siguiente_viaje() == 1
        self.assertEqual(pr.siguiente_viaje(), 1)

        # return siguiente_viaje() == 2
        self.assertEqual(pr.siguiente_viaje(), 2)

        # return siguiente_viaje() == 3
        self.assertEqual(pr.siguiente_viaje(), 3)

    @patch('practica6.Practica6.obtener_agnos_trabajando')
    def test_viajes_disponibles_obtener_agnos_trabajando(self, mock_obtener_agnos_trabajando):
        # Cantidad de viajes que queremos crear
        cantidad_viajes = 3

        # Usar nuestro mock y hacer que nos regrese agnos = 3 trabajando de un conductor
        mock_obtener_agnos_trabajando.return_value = ['ConductorMockeado', 3]

        # Instanciar nuestra clase Practica6 para usar nuestros metodos
        pr = Practica6()

        # Llamar al metodo obtener_agnos_trabajando y almacenarlo en la variable resultado
        resultado = pr.obtener_agnos_trabajando()[1]

        # Llamamos al metodo viajes_disponibles, su dependencia esta vez es obtener_agnos_trabajando() por eso se crea el mock
        # Comprobar que la salida de viajes disponibles sea igual, pero usando el mock agnos_trabajando = 3 por lo tanto tarifa = 50
        self.assertEqual(pr.viajes_disponibles(
            cantidad_viajes), {1: 50, 2: 50, 3: 50})

    @patch('practica6.Practica6.calcular_tarifa')
    def test_viajes_disponibles_calcular_tarifa(self, mock_calcular_tarifa):
        # Cantidad de viajes que queremos crear
        cantidad_viajes = 3

        # Usar nuestro mock y hacer que nos regrese una tarifa = 90
        mock_calcular_tarifa.return_value = 90

        # Instanciar nuestra clase Practica6 para usar nuestros metodos
        pr = Practica6()

        # Llamar al metodo calcular_tarifa y almacenarlo en la variable resultado
        resultado = pr.calcular_tarifa()
        
        # Llamamos al metodo viajes_disponibles, su dependencia esta vez es calcular_tarifa() por eso se crea el mock
        # Comprobar que la salida de viajes disponibles sea igual, pero usando el mock tarifa = 90 por lo tanto tarifa = 90
        self.assertEqual(pr.viajes_disponibles(cantidad_viajes), {
                         1: resultado, 2: resultado, 3: resultado})


if __name__ == '__main__':
    unittest.main()



#region Fuentes
# https://manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/pruebas/integracion/
# https://www.fugue.co/blog/2016-02-11-python-mocking-101
# https://www.paradigmadigital.com/dev/mockear-tests-python/
# https://aaronlelevier.github.io/python-unit-testing-with-magicmock/
#endregion
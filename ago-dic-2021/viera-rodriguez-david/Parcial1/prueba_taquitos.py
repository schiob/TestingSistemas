import unittest
from taquitos import tacos

class casos(unittest.TestCase):
    def test_ejemplogit(self):
        pedido = "cachete lengua cachete tripitas machito machito machito cachete lengua"
        cuenta = 110
        self.assertEqual(cuenta,tacos(pedido))

    def test_mayor_a_30(self):
        pedido = "cachete lengua cachete tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua tripitas machito machito machito cachete lengua"
        cuenta = "Error"
        self.assertEqual(cuenta,tacos(pedido))
    
    def test_5_tacos(self):
        pedido = "cachete lengua tripitas machito machito"
        cuenta = 60
        self.assertEqual(cuenta,tacos(pedido))

    def test_taco_falso(self):
        pedido = "cachete lengua asada"
        cuenta = 23
        self.assertEqual(cuenta,tacos(pedido))

if __name__=='__main__':
    unittest.main()
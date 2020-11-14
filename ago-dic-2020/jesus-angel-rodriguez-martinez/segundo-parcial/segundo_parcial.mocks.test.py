# -*- coding: utf-8 -*-
from unittest.mock import Mock
import unittest
from segundo_parcial import obtener_promedio

class promedio_test(unittest.TestCase):
    def testPromedio(self):
        mock = Mock()
        test_cases = (
            {"datos" : ['Jose_Lopez quimica 89.00\n', 'Jose_Lopez matematicas 85.34\n', 'Maria_Martinez fisica 95.50\n', 'Maria_Martinez español 90.00'], "resultado" : "Jose_Lopez 87.17\nMaria_Martinez 92.75"},
            {"datos" : ['Jose_Lopez quimica 100.00\n', 'Maria_Martinez fisica 95.50\n', 'Sudo_von español 90.00'], "resultado" : "Jose_Lopez 100.00\nMaria_Martinez 95.50\nSudo_von 90.00"},
        )
        for tc in test_cases:
            mock.readlines.return_value = tc["datos"]
            self.assertEqual(obtener_promedio(mock), tc['resultado'])
    
if __name__ == "__main__":
    unittest.main()

from parcial_2 import *
import unittest
from unittest import mock
import os

class promedios_test(unittest.TestCase):
    def setUp(self):
        file = open("test_1.csv","w+")
        file.write("Jose_Lopez quimica 89.00\n"+
                    "Jose_Lopez matematicas 85.34\n"+
                    "Maria_Martinez fisica 95.50\n"+
                    "Maria_Martinez español 90.00")
        file.close()
        file = open("test_2.csv","w+")
        file.write("Juan_Perez matematicas 100.00\n"+
                    "Juan_Perez fisica_2 70.99\n"+
                    "Juan_Perez geografia 82.33\n"+
                    "Lorena_Chavez matematicas 56.65\n"+
                    "Lorena_Chavez fisica_2 92.39\n"+
                    "Lorena_Chavez geografia 89.19"
        )
        file.close()
        file = open("test_3.csv","w+")
        file.write("Erick_Gomez matematicas 69.36\n"+
                    "Erick_Gomez español 89.48\n"+
                    "Erick_Gomez computacion 96.44\n"+
                    "Fernando_Chavez matematicas 75.50\n"+
                    "Fernando_Chavez español 100.00\n"+
                    "Fernando_Chavez computacion 84.61\n"+
                    "Paula_Aguilar matematicas 70.01\n"+
                    "Paula_Aguilar español 76.67\n"+
                    "Paula_Aguilar computacion 80.03\n")
        file.close()

    def test_archivo_tiene_datos(self):
        filep = "test_1.csv"
        test1 = validate_file(filep)
        self.assertEqual(test1,True)

    def test_get_data(self):
        filep = "test_1.csv"
        file_list = [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'español', '90.00']]
        file_data_test = read_alumn_data(filep) 
        self.assertEqual(file_data_test,file_list)
    
    def test_get_names(self):
        data = [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'español', '90.00']]
        names = ['Jose_Lopez', 'Maria_Martinez']
        names_from_data = get_names(data)
        self.assertEqual(names_from_data,names)

    def test_obtener_promedios(self):
        set_1 ={'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}
        set_2 = {'Juan_Perez': 84.44, 'Lorena_Chavez': 79.41}
        set_3 = {'Erick_Gomez': 85.09, 'Fernando_Chavez': 86.7, 'Paula_Aguilar': 75.57}
        list1 = read_alumn_data("test_1.csv")
        list2 = read_alumn_data("test_2.csv")
        list3 = read_alumn_data("test_3.csv")
        test1 = get_averages(list1)
        test2 = get_averages(list2)
        test3 = get_averages(list3)
        self.assertEqual(test1,set_1)
        self.assertEqual(test2,set_2)
        self.assertEqual(test3,set_3)
    

        
 
    def tearDown(self):
        os.remove("test_1.csv")
        os.remove("test_2.csv")
        os.remove("test_3.csv")






if __name__=='__main__':
    unittest.main()
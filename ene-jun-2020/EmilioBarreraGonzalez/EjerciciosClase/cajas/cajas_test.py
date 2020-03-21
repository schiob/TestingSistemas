import unittest
from cajas import cont, transformacion, volumen
class prueba1(unittest.TestCase):
    #Prueba cont
    def test_transform(self):
        tts=[
            {"in":["3,8","4,9","3,.5"],"ex":61.5},
            {"in":["2,4","4,8"],"ex":40},
            {"in":["3,2","4,6","6,2","2,9"], "ex":60},
            {"in":["2,3","2,.5","1,10","2,2"], "ex":21}
        ]
        for tc in tts:
            self.assertEqual(cont(tc["in"]), tc["ex"])

    def test_vol(self):
        tts=[
            {"in1":4, "in2":4, "in3":4 , "ex":64},
            {"in1":2 ,"in2":2, "in3":2 , "ex":8},
            {"in1":3, "in2":2, "in3":1 , "ex":6},
            {"in1":9 ,"in2":9, "in3":9 , "ex":729}
        ]
        for tc in tts:
            self.assertEqual(volumen(tc["in1"],tc["in2"],tc["in3"]), tc["ex"])
if __name__ == "__main__":
    unittest.main()
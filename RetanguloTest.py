import unittest
from Retangulo import calcular_area_retangulo

class TestMethod(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(calcular_area_retangulo(4,5), 20, "Esperado 20")
    
    def test_case2(self):
        self.assertEqual(calcular_area_retangulo(7,3), 21, "Esperado 21")
    
    def test_case3(self):
        self.assertEqual(calcular_area_retangulo(0,10), 0, "Esperado 0")
    
    def test_case4(self):
        self.assertEqual(calcular_area_retangulo(2,-5), 0, "Esperado 0")

    def test_case5(self):
        self.assertEqual(calcular_area_retangulo(0,0), 0, "Esperado 0")
    
    def test_case6(self):
        self.assertEqual(calcular_area_retangulo(-5,-5), 0, "Esperado 0")

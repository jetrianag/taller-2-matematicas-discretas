import unittest
import sys
import os
import math
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from boole_shannon_compucuantic.shannon import frecuencia_texto, entropia_texto
 
class TestFrecuenciaTexto(unittest.TestCase):
 
    def test_cuenta_cada_simbolo_correctamente(self):
        frecuencia = frecuencia_texto("AAAB")
        self.assertEqual(frecuencia, {"A": 3, "B": 1})
 
    def test_texto_con_un_solo_simbolo(self):
        frecuencia = frecuencia_texto("ZZZZ")
        self.assertEqual(frecuencia, {"Z": 4})
 
    def test_incluye_espacios_como_simbolo(self):
        frecuencia = frecuencia_texto("A A")
        self.assertEqual(frecuencia, {"A": 2, " ": 1})
        
if __name__ == "__main__":
    unittest.main()
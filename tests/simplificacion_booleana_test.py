import unittest
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from boole_shannon_compucuantic.simplificacion_booleana import (num_a_binario, se_combinan,encontrar_implicantes_primos,elegir_implicantes_esenciales,termino_a_expresion,simplificar,tabla_desde_minterminos,tabla_desde_terminos, verificar_equivalencia,)
  
class TestFuncionesBasicas(unittest.TestCase):
 
    def test_num_a_binario_rellena_con_ceros(self):
        self.assertEqual(num_a_binario(5, 3), "101")
        self.assertEqual(num_a_binario(1, 3), "001")
        self.assertEqual(num_a_binario(0, 4), "0000")
 
    def test_se_combinan_terminos_con_una_diferencia(self):
        # "101" y "001" difieren solo en el primer bit -> se combinan
        self.assertEqual(se_combinan("101", "001"), "-01")
 
    def test_se_combinan_terminos_con_mas_de_una_diferencia(self):
        # "101" y "010" difieren en los tres bits -> no se combinan
        self.assertIsNone(se_combinan("101", "010"))
 
    def test_se_combinan_terminos_identicos(self):
        # Dos términos iguales tienen 0 diferencias, no 1 -> no se combinan
        self.assertIsNone(se_combinan("101", "101"))

if __name__ == "__main__":
     unittest.main()
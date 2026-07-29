import unittest
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from boole_shannon_compucuantic.simulador_cuantico import (multiplicar_matriz_vector,aplicar_compuerta,calcular_probabilidades,simular_mediciones)

class TestCompuertas(unittest.TestCase):
    """Casos de prueba obligatorios del enunciado."""
 
    def test_X_manda_0_a_1(self):
        # X|0> = |1>
        resultado = aplicar_compuerta("X", [1, 0])
        self.assertEqual(resultado, [0, 1])
 
    def test_X_manda_1_a_0(self):
        resultado = aplicar_compuerta("X", [0, 1])
        self.assertEqual(resultado, [1, 0])
 
    def test_Z_deja_0_igual(self):
        resultado = aplicar_compuerta("Z", [1, 0])
        self.assertEqual(resultado, [1, 0])
 
    def test_Z_invierte_el_signo_de_1(self):
        resultado = aplicar_compuerta("Z", [0, 1])
        self.assertEqual(resultado, [0, -1])
 
    def test_H_produce_probabilidades_cercanas_a_50_50(self):
        # H|0> produce probabilidades cercanas a 50% y 50%
        resultado = aplicar_compuerta("H", [1, 0])
        prob_0, prob_1 = calcular_probabilidades(resultado)
        self.assertAlmostEqual(prob_0, 0.5, places=9)
        self.assertAlmostEqual(prob_1, 0.5, places=9)
 
    def test_HH_recupera_el_estado_original(self):
        # HH|0> = |0>, salvo errores numericos pequeños
        estado_h = aplicar_compuerta("H", [1, 0])
        estado_hh = aplicar_compuerta("H", estado_h)
        self.assertAlmostEqual(estado_hh[0], 1.0, places=9)
        self.assertAlmostEqual(estado_hh[1], 0.0, places=9)
 
    def test_compuerta_desconocida_lanza_error(self):
        with self.assertRaises(ValueError):
            aplicar_compuerta("Y", [1, 0])

if __name__ == "__main__":
    unittest.main()
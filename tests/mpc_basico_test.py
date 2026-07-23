import unittest
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from cripto.mpc_basico import generar_partes,repartir_notas, suma_parcial_servidor, reconstruir_suma, calcular_promedio, simular_protocolo 
class TestMPC(unittest.TestCase):
     def test_generar_partes_suman_la_nota_original(self):
        M = 1000003
        nota = 37
        s1, s2, s3 = generar_partes(nota, M)
        self.assertEqual((s1 + s2 + s3) % M, nota)

     def test_ejemplo_minimo_del_enunciado(self):
        # Notas del enunciado: [40, 35, 50, 25] -> suma 150, promedio 37.5
        resultado = simular_protocolo([40, 35, 50, 25])
        self.assertEqual(resultado["suma_total"], 150)
        self.assertEqual(resultado["promedio"], 37.5)

     def test_ningun_servidor_ve_la_nota_original(self):
        M = 1000003
        nota = 45
        s1, s2, s3 = generar_partes(nota, M)
        self.assertTrue(s1 != nota or s2 != nota or s3 != nota)

     def test_promedio_sin_notas_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_promedio(suma_total=0, cantidad_notas=0)
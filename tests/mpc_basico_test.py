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
        
import unittest
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from cripto.mpc_basico import generar_partes,repartir_notas, suma_parcial_servidor, reconstruir_suma, calcular_promedio, simular_protocolo 
class TestMPC(unittest.TestCase):
    
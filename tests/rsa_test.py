import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cripto.rsa import euclides_extendido,inverso_modular, generar_llaves, cifrar_rsa, descifrar_rsa

class TestRSA(unittest.TestCase):
    def test_caso_obligatorio_del_enunciado(self):
        llaves = generar_llaves(p=61, q=53, e=17)
        self.assertEqual(llaves["n"], 3233)
        self.assertEqual(llaves["phi"], 3120)
        self.assertEqual(llaves["d"], 2753)

        M = 65
        C = cifrar_rsa(M, llaves["e"], llaves["n"])
        self.assertEqual(C, 2790)
        self.assertEqual(descifrar_rsa(C, llaves["d"], llaves["n"]), M)
        
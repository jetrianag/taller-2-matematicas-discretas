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

    def test_euclides_extendido_identidad_bezout(self):
        a, b = 240, 46
        g, x, y = euclides_extendido(a, b)
        self.assertEqual(g, 2)  # mcd(240, 46) = 2
        self.assertEqual(a * x + b * y, g)

    def test_e_invalido_lanza_error(self):
        # Con p=61, q=53 -> phi=3120. e=6 comparte factor con phi -> inválido
        with self.assertRaises(ValueError):
            generar_llaves(p=61, q=53, e=6)

    def test_ciclo_completo_con_otro_mensaje(self):
        llaves = generar_llaves(p=17, q=11, e=7)  # n=187, phi=160
        for M in [5, 42, 100]:
            C = cifrar_rsa(M, llaves["e"], llaves["n"])
            self.assertEqual(descifrar_rsa(C, llaves["d"], llaves["n"]), M)

    if __name__ == "__main__":
    unittest.main()
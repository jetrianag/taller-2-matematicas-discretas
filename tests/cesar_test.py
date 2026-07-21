import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from cripto.cesar import cifrar_cesar, descifrar_cesar, fuerza_bruta_cesar

class TestCesar(unittest.TestCase):

    def test_cifrado_ejemplo_taller(self):
        #caso minimo que estaba en el taller
        self.assertEqual(cifrar_cesar("HOLA UNAL", 3), "KROD XQDO")

   def test_descifrado_es_inverso_del_cifrado(self):
        texto_original = "HOLA, Mundo 2026"
        k = 7
        cifrado = cifrar_cesar(texto_original, k)
        self.assertEqual(descifrar_cesar(cifrado, k), texto_original)

    def test_conserva_puntuacion_numeros_y_espacios(self):
        original = "Clase: 8:00 am, sala #3"
        k = 5
        cifrado = cifrar_cesar(original, k)
        for original_c, cifrado_c in zip(original, cifrado):
            if not original_c.isalpha():
                self.assertEqual(original_c, cifrado_c)
    
    def test_mayusculas_y_minusculas_independientes(self):
        cifrado = cifrar_cesar("aA", 1)
        self.assertEqual(cifrado, "bB")

    
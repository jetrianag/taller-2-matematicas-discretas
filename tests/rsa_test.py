import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cripto.rsa import euclides_extendido,inverso_modular, generar_llaves, cifrar_rsa, descifrar_rsa

class TestRSA(unittest.TestCase):
    
import unittest
import sys
import os
import io
from contextlib import redirect_stdout
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from boole.tablas_verdad import (expresion1,expresion2,expresion3,EXPRESIONES,generar_tabla,evaluar_entrada)
 
 
class TestExpresiones(unittest.TestCase):
 
    def test_expresion1_AB_or_notC(self):
        # (A AND B) OR (NOT C)
        self.assertTrue(expresion1(True, True, True, False))    # T and T = T -> True
        self.assertTrue(expresion1(False, False, False, False)) # F or (not F)=T -> True
        self.assertFalse(expresion1(True, False, True, False))  # F or (not T)=F -> False
        self.assertFalse(expresion1(False, False, True, False)) # F or F -> False
 
    def test_expresion2_AxorB_and_C(self):
        # (A XOR B) AND C
        self.assertTrue(expresion2(True, False, True, False))   # T and T -> True
        self.assertFalse(expresion2(True, True, True, False))   # F and T -> False (A y B iguales)
        self.assertFalse(expresion2(False, False, True, False)) # F and T -> False
        self.assertFalse(expresion2(True, False, False, False)) # T and F -> False
 
    def test_expresion3_AorB_and_notA_or_C(self):
        # (A OR B) AND (NOT A OR C)
        self.assertTrue(expresion3(True, False, True, False))   # T and (F or T)=T -> True
        self.assertFalse(expresion3(True, False, False, False)) # T and (F or F)=F -> False
        self.assertTrue(expresion3(False, True, False, False))  # T and (T or F)=T -> True
        self.assertFalse(expresion3(False, False, False, False))# F and ... -> False
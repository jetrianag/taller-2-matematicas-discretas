import unittest
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
 
from grafos.coloreo_grafos import (colorear_grafo, es_coloreo_valido, resumen_por_color,GRAFO_EJEMPLO)
 
 
class TestColoreo(unittest.TestCase):
 
    def test_grafo_ejemplo_tiene_minimo_10_vertices(self):
        self.assertGreaterEqual(len(GRAFO_EJEMPLO), 10)
 
    def test_coloreo_del_grafo_ejemplo_es_valido(self):
        colores = colorear_grafo(GRAFO_EJEMPLO)
        self.assertTrue(es_coloreo_valido(GRAFO_EJEMPLO, colores))
 
    def test_todos_los_vertices_reciben_color(self):
        colores = colorear_grafo(GRAFO_EJEMPLO)
        self.assertEqual(set(colores.keys()), set(GRAFO_EJEMPLO.keys()))

if __name__ == "__main__":
    unittest.main()
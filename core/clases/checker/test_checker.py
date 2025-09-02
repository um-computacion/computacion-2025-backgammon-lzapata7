"""
Tests unitarios para la clase Checker.
"""

import unittest
import sys
import os

# Agregar el directorio padre al path para poder importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.clases.checker.checker import Checker


class TestChecker(unittest.TestCase):
    """Tests para la clase Checker."""
    
    def test_checker_creation_white(self):
        """Test de creación de ficha blanca."""
        white_checker = Checker("white")
        self.assertEqual(white_checker.get_color(), "white")
    
    def test_checker_creation_black(self):
        """Test de creación de ficha negra."""
        black_checker = Checker("black")
        self.assertEqual(black_checker.get_color(), "black")
    
    def test_checker_string_representation_white(self):
        """Test de representación en string de ficha blanca."""
        white_checker = Checker("white")
        self.assertEqual(str(white_checker), "W")
    
    def test_checker_string_representation_black(self):
        """Test de representación en string de ficha negra."""
        black_checker = Checker("black")
        self.assertEqual(str(black_checker), "B")
    
    def test_checker_equality_same_color(self):
        """Test de igualdad entre fichas del mismo color."""
        white1 = Checker("white")
        white2 = Checker("white")
        self.assertEqual(white1, white2)
        
        black1 = Checker("black")
        black2 = Checker("black")
        self.assertEqual(black1, black2)
    
    def test_checker_inequality_different_colors(self):
        """Test de desigualdad entre fichas de diferentes colores."""
        white_checker = Checker("white")
        black_checker = Checker("black")
        self.assertNotEqual(white_checker, black_checker)
    
    def test_checker_inequality_with_none(self):
        """Test de desigualdad con None."""
        checker = Checker("white")
        self.assertNotEqual(checker, None)
        self.assertFalse(checker.__eq__(None))
    
    def test_set_color_white_to_black(self):
        """Test de cambio de color de blanco a negro."""
        checker = Checker("white")
        checker.set_color("black")
        self.assertEqual(checker.get_color(), "black")
        self.assertEqual(str(checker), "B")
    
    def test_set_color_black_to_white(self):
        """Test de cambio de color de negro a blanco."""
        checker = Checker("black")
        checker.set_color("white")
        self.assertEqual(checker.get_color(), "white")
        self.assertEqual(str(checker), "W")
    
    def test_set_color_custom_value(self):
        """Test de establecer un color personalizado."""
        checker = Checker("white")
        checker.set_color("red")
        self.assertEqual(checker.get_color(), "red")
        # La representación string seguirá la lógica original
        self.assertEqual(str(checker), "B")  # Cualquier color != "white" se muestra como "B"
    
    def test_checker_immutability_after_creation(self):
        """Test de que el color inicial se mantiene hasta que se cambie explícitamente."""
        checker = Checker("white")
        original_color = checker.get_color()
        
        # Realizar varias operaciones
        str(checker)
        checker.__eq__(checker)
        
        # El color debe mantenerse igual
        self.assertEqual(checker.get_color(), original_color)


if __name__ == "__main__":
    unittest.main(verbosity=2)
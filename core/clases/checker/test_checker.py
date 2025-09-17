import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.clases.checker.checker import Checker


class TestChecker(unittest.TestCase):   
    
    def test_checker_creation_white(self):
        
        white_checker = Checker("white")
        self.assertEqual(white_checker.get_color(), "white")
    
    def test_checker_creation_black(self):
        
        black_checker = Checker("black")
        self.assertEqual(black_checker.get_color(), "black")
    
    def test_checker_string_representation_white(self):
       
        white_checker = Checker("white")
        self.assertEqual(str(white_checker), "W")
    
    def test_checker_string_representation_black(self):
         
        black_checker = Checker("black")
        self.assertEqual(str(black_checker), "B")
    
    def test_checker_equality_same_color(self):
        
        white1 = Checker("white")
        white2 = Checker("white")
        self.assertEqual(white1, white2)
        
        black1 = Checker("black")
        black2 = Checker("black")
        self.assertEqual(black1, black2)
    
    def test_checker_inequality_different_colors(self):
        
        white_checker = Checker("white")
        black_checker = Checker("black")
        self.assertNotEqual(white_checker, black_checker)
    
    def test_checker_inequality_with_none(self):
        
        checker = Checker("white")
        self.assertNotEqual(checker, None)
        self.assertFalse(checker.__eq__(None))
    
    def test_set_color_white_to_black(self):
        
        checker = Checker("white")
        checker.set_color("black")
        self.assertEqual(checker.get_color(), "black")
        self.assertEqual(str(checker), "B")
    
    def test_set_color_black_to_white(self):
       
        checker = Checker("black")
        checker.set_color("white")
        self.assertEqual(checker.get_color(), "white")
        self.assertEqual(str(checker), "W")
    
    def test_set_color_custom_value(self):
        
        checker = Checker("white")
        checker.set_color("red")
        self.assertEqual(checker.get_color(), "red")
        self.assertEqual(str(checker), "B")  
    
    def test_checker_immutability_after_creation(self):
       
        checker = Checker("white")
        original_color = checker.get_color()
        
        
        str(checker)
        checker.__eq__(checker)
        
        
        self.assertEqual(checker.get_color(), original_color)


if __name__ == "__main__":
    unittest.main(verbosity=2)
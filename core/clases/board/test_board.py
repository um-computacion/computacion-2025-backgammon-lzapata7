"""
Tests unitarios para la clase Board.
"""

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.clases.board.board import Board
from core.clases.checker.checker import Checker


class TestBoard(unittest.TestCase):
    
    
    def setUp(self):
        self.board = Board()
    
    def test_board_initialization(self):
    
        all_points = self.board.get_all_points()
        self.assertEqual(len(all_points), 24)
    
    def test_initial_setup_white_checkers(self):

        self.assertEqual(self.board.get_point_count(1), 2)
        self.assertEqual(self.board.get_point_color(1), "white")
        
        self.assertEqual(self.board.get_point_count(12), 5)
        self.assertEqual(self.board.get_point_color(12), "white")
        
        self.assertEqual(self.board.get_point_count(17), 3)
        self.assertEqual(self.board.get_point_color(17), "white")
        
        self.assertEqual(self.board.get_point_count(19), 5)
        self.assertEqual(self.board.get_point_color(19), "white")
    
    def test_initial_setup_black_checkers(self):
        
        self.assertEqual(self.board.get_point_count(24), 2)
        self.assertEqual(self.board.get_point_color(24), "black")
        

        self.assertEqual(self.board.get_point_count(13), 5)
        self.assertEqual(self.board.get_point_color(13), "black")
        
      
        self.assertEqual(self.board.get_point_count(8), 3)
        self.assertEqual(self.board.get_point_color(8), "black")
        
  
        self.assertEqual(self.board.get_point_count(6), 5)
        self.assertEqual(self.board.get_point_color(6), "black")
    
   def test_initial_setup_total_checkers(self):
      
        white_count = 0
        black_count = 0
        
        for point in range(1, 25):
            checkers = self.board.get_point(point)
            for checker in checkers:
                if checker.get_color() == "white":
                    white_count += 1
                else:
                    black_count += 1
        
        self.assertEqual(white_count, 15)
        self.assertEqual(black_count, 15)
    
    def test_empty_points_initially(self):
      
        empty_points = [2, 3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 18, 20, 21, 22, 23]
        
        for point in empty_points:
            self.assertTrue(self.board.is_point_empty(point))
            self.assertIsNone(self.board.get_point_color(point))
            self.assertEqual(self.board.get_point_count(point), 0)
    
    def test_get_point_invalid_numbers(self):
      
        self.assertEqual(self.board.get_point_count(0), 0)
        self.assertEqual(self.board.get_point_count(25), 0)
        self.assertEqual(self.board.get_point_count(-1), 0)
        self.assertEqual(self.board.get_point_color(0), None)
        self.assertEqual(self.board.get_point_color(25), None)
        self.assertEqual(self.board.get_point([]), [])
        self.assertEqual(self.board.get_point(100), [])
    
    def test_get_point_returns_copy(self):
        "
        original_checkers = self.board.get_point(1)
        original_count = len(original_checkers)
        
        # Modificar la lista devuelta
        original_checkers.append(Checker("white"))
        
        # Verificar que el tablero no se modificó
        current_checkers = self.board.get_point(1)
        self.assertEqual(len(current_checkers), original_count)
    
    def test_can_move_to_empty_point(self):
        
        self.assertTrue(self.board.can_move_to_point(2, "white"))
        self.assertTrue(self.board.can_move_to_point(2, "black"))
    
    def test_can_move_to_own_point(self):
        
        self.assertTrue(self.board.can_move_to_point(1, "white"))
        self.assertTrue(self.board.can_move_to_point(24, "black"))
    
    def test_can_move_to_opponent_point_multiple_checkers(self):
        
        self.assertFalse(self.board.can_move_to_point(13, "white"))  # 5 fichas negras
        self.assertFalse(self.board.can_move_to_point(1, "black"))   # 2 fichas blancas
    
    def test_can_move_to_opponent_point_single_checker(self):
        
        test_board = Board()
        test_board._Board__points__ = [[] for _ in range(24)]
        test_board._Board__points__[1] = [Checker("black")]  # Una ficha negra en punto 2
        
        self.assertTrue(test_board.can_move_to_point(2, "white"))
    
    def test_move_checker_successful(self):
       
        initial_count_1 = self.board.get_point_count(1)
        initial_count_2 = self.board.get_point_count(2)
        
        captured = self.board.move_checker(1, 2, "white")
        
        self.assertEqual(self.board.get_point_count(1), initial_count_1 - 1)
        self.assertEqual(self.board.get_point_count(2), initial_count_2 + 1)
        self.assertEqual(self.board.get_point_color(2), "white")
        self.assertIsNone(captured)
    
    def test_move_checker_with_capture(self):
       
        test_board = Board()
        test_board._Board__points__ = [[] for _ in range(24)]
        test_board._Board__points__[0] = [Checker("white")]  # Ficha blanca en punto 1
        test_board._Board__points__[1] = [Checker("black")]  # Ficha negra en punto 2
        
        captured = test_board.move_checker(1, 2, "white")
        
        self.assertIsNotNone(captured)
        self.assertEqual(captured.get_color(), "black")
        self.assertEqual(test_board.get_point_color(2), "white")
        self.assertEqual(test_board.get_point_count(2), 1)
    
    def test_move_checker_invalid_points(self):
        
        result = self.board.move_checker(0, 1, "white")
        self.assertIsNone(result)
        
        result = self.board.move_checker(1, 25, "white")
        self.assertIsNone(result)
        
        result = self.board.move_checker(-1, 1, "white")
        self.assertIsNone(result)
        
        result = self.board.move_checker(1, 0, "white")
        self.assertIsNone(result)
    
    def test_move_checker_from_empty_point(self):
        
        result = self.board.move_checker(2, 3, "white")  
        self.assertIsNone(result)
    
    def test_move_checker_wrong_color(self):
        
        result = self.board.move_checker(1, 2, "black")  
        self.assertIsNone(result)
    
    def test_move_checker_to_blocked_point(self):
      
        result = self.board.move_checker(1, 13, "white")  
        self.assertIsNone(result)
    
    def test_add_checker_to_point_successful(self):
        
        checker = Checker("white")
        success = self.board.add_checker_to_point(2, checker)
        
        self.assertTrue(success)
        self.assertEqual(self.board.get_point_count(2), 1)
        self.assertEqual(self.board.get_point_color(2), "white")

     def test_add_checker_to_invalid_point(self):
        
        checker = Checker("white")
        success = self.board.add_checker_to_point(0, checker)
        self.assertFalse(success)
        
        success = self.board.add_checker_to_point(25, checker)
        self.assertFalse(success)
    
    def test_add_checker_to_blocked_point(self):
        
        checker = Checker("white")
        success = self.board.add_checker_to_point(13, checker) 
        self.assertFalse(success)
    
    def test_remove_checker_successful(self):
        
        initial_count = self.board.get_point_count(1)
        removed_checker = self.board.remove_checker_from_point(1, "white")
        
        self.assertIsNotNone(removed_checker)
        self.assertEqual(removed_checker.get_color(), "white")
        self.assertEqual(self.board.get_point_count(1), initial_count - 1)
    
    def test_remove_checker_from_empty_point(self):
        
        removed_checker = self.board.remove_checker_from_point(2, "white")
        self.assertIsNone(removed_checker)
    
    def test_remove_checker_wrong_color(self):
        
        removed_checker = self.board.remove_checker_from_point(1, "black")  # Punto 1 tiene fichas blancas
        self.assertIsNone(removed_checker)
    
    def test_remove_checker_from_invalid_point(self):
        
        removed_checker = self.board.remove_checker_from_point(0, "white")
        self.assertIsNone(removed_checker)
        
        removed_checker = self.board.remove_checker_from_point(25, "white")
        self.assertIsNone(removed_checker)
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
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
    
     def test_get_all_points_returns_copy(self):
        
        all_points = self.board.get_all_points()
        self.assertEqual(len(all_points), 24)
        
        # Modificar la lista devuelta
        all_points[0].append(Checker("white"))
        
        # Verificar que el tablero original no se modificó
        original_point = self.board.get_point(1)
        self.assertNotEqual(len(all_points[0]), len(original_point))
    
    def test_is_home_board_white(self):
        """Test de verificación de tablero casa para fichas blancas."""
        # Tablero casa de blancas: puntos 19-24
        self.assertTrue(self.board.is_home_board(19, "white"))
        self.assertTrue(self.board.is_home_board(20, "white"))
        self.assertTrue(self.board.is_home_board(24, "white"))
        
        # No tablero casa
        self.assertFalse(self.board.is_home_board(18, "white"))
        self.assertFalse(self.board.is_home_board(1, "white"))
        self.assertFalse(self.board.is_home_board(12, "white"))
    
    def test_is_home_board_black(self):
        """Test de verificación de tablero casa para fichas negras."""
        # Tablero casa de negras: puntos 1-6
        self.assertTrue(self.board.is_home_board(1, "black"))
        self.assertTrue(self.board.is_home_board(3, "black"))
        self.assertTrue(self.board.is_home_board(6, "black"))
        
        # No tablero casa
        self.assertFalse(self.board.is_home_board(7, "black"))
        self.assertFalse(self.board.is_home_board(24, "black"))
        self.assertFalse(self.board.is_home_board(13, "black"))
    
    def test_empty_board_setup(self):
        """Test de tablero vacío."""
        # Crear tablero vacío
        empty_board = Board()
        for point in empty_board._Board__points__:
            point.clear()
        
        # Verificar que todos los puntos están vacíos
        for i in range(1, 25):
            self.assertTrue(empty_board.is_point_empty(i))
            self.assertIsNone(empty_board.get_point_color(i))
            self.assertEqual(empty_board.get_point_count(i), 0)
    
    def test_point_operations_boundary_cases(self):
        """Test de operaciones en casos límite."""
        # Punto en límite inferior
        self.assertIsInstance(self.board.get_point_count(1), int)
        self.assertIsInstance(self.board.get_point_color(1), str)
        
        # Punto en límite superior
        self.assertIsInstance(self.board.get_point_count(24), int)
        self.assertIsInstance(self.board.get_point_color(24), str)
    
    def test_multiple_moves_same_point(self):
        """Test de múltiples movimientos hacia el mismo punto."""
        # Mover varias fichas al mismo punto vacío
        checker1 = Checker("white")
        checker2 = Checker("white")
        
        success1 = self.board.add_checker_to_point(2, checker1)
        success2 = self.board.add_checker_to_point(2, checker2)
        
        self.assertTrue(success1)
        self.assertTrue(success2)
        self.assertEqual(self.board.get_point_count(2), 2)
        self.assertEqual(self.board.get_point_color(2), "white")
    
    def test_setup_initial_position_called_multiple_times(self):
        """Test de que setup_initial_position se puede llamar múltiples veces."""
        initial_state = self.board.get_all_points()
        
        # Llamar setup nuevamente
        self.board._setup_initial_position()
        
        new_state = self.board.get_all_points()
        
        # Verificar que el estado es el mismo
        for i in range(24):
            self.assertEqual(len(initial_state[i]), len(new_state[i]))

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
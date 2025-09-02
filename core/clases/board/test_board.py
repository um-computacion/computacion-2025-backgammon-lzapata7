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
    
   
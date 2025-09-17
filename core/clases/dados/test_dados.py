import unittest
import sys
import os
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.clases.dados.dados import Dados


class TestDice(unittest.TestCase):
    
    def setUp(self):
       
        self.dice = Dice()
    
    def test_dice_initialization(self):
        
        self.assertEqual(self.dice.get_dice_values(), (0, 0))
        self.assertEqual(len(self.dice.get_available_moves()), 0)
        self.assertFalse(self.dice.has_moves())
        self.assertFalse(self.dice.is_double())
    
    @patch('random.randint')
    def test_dice_roll_normal(self, mock_randint):
        
        mock_randint.side_effect = [3, 5]
        
        die1, die2 = self.dice.roll()
        
        self.assertEqual(die1, 3)
        self.assertEqual(die2, 5)
        self.assertEqual(self.dice.get_dice_values(), (3, 5))
        self.assertEqual(len(self.dice.get_available_moves()), 2)
        self.assertIn(3, self.dice.get_available_moves())
        self.assertIn(5, self.dice.get_available_moves())
        self.assertTrue(self.dice.has_moves())
        self.assertFalse(self.dice.is_double())
    
    @patch('random.randint')
    def test_dice_roll_double(self, mock_randint):
     
        mock_randint.side_effect = [4, 4]
        
        die1, die2 = self.dice.roll()
        
        self.assertEqual(die1, 4)
        self.assertEqual(die2, 4)
        self.assertEqual(self.dice.get_dice_values(), (4, 4))
        self.assertEqual(len(self.dice.get_available_moves()), 4)
        
       
        available_moves = self.dice.get_available_moves()
        for move in available_moves:
            self.assertEqual(move, 4)
        
        self.assertTrue(self.dice.has_moves())
        self.assertTrue(self.dice.is_double())
    
    def test_dice_roll_range(self):
        
        for _ in range(100): 
            die1, die2 = self.dice.roll()
            
            self.assertIn(die1, range(1, 7))
            self.assertIn(die2, range(1, 7))
    
    def test_use_move_successful(self):
   
        self.dice._Dice__die1__ = 3
        self.dice._Dice__die2__ = 5
        self.dice._Dice__moves_available__ = [3, 5]
        
        success = self.dice.use_move(3)
        self.assertTrue(success)
        self.assertEqual(len(self.dice.get_available_moves()), 1)
        self.assertIn(5, self.dice.get_available_moves())
        self.assertNotIn(3, self.dice.get_available_moves())
    
    def test_use_move_invalid(self):
   
        self.dice._Dice__die1__ = 3
        self.dice._Dice__die2__ = 5
        self.dice._Dice__moves_available__ = [3, 5]
        
        success = self.dice.use_move(2)
        self.assertFalse(success)
        self.assertEqual(len(self.dice.get_available_moves()), 2)
  
  
    def test_use_move_from_empty_list(self):
       
        success = self.dice.use_move(3)
        self.assertFalse(success)
        self.assertFalse(self.dice.has_moves())
    
    def test_use_all_moves(self):
        
        self.dice._Dice__die1__ = 2
        self.dice._Dice__die2__ = 4
        self.dice._Dice__moves_available__ = [2, 4]
        
        self.assertTrue(self.dice.use_move(2))
        self.assertTrue(self.dice.use_move(4))
        
        self.assertFalse(self.dice.has_moves())
        self.assertEqual(len(self.dice.get_available_moves()), 0)
    
    def test_use_all_double_moves(self):
        
        self.dice._Dice__die1__ = 6
        self.dice._Dice__die2__ = 6
        self.dice._Dice__moves_available__ = [6, 6, 6, 6]
        
       
        for i in range(4):
            success = self.dice.use_move(6)
            self.assertTrue(success)
            self.assertEqual(len(self.dice.get_available_moves()), 3 - i)
       
        self.assertFalse(self.dice.has_moves())
        self.assertFalse(self.dice.use_move(6))
    
    def test_get_available_moves_returns_copy(self):
        
        self.dice._Dice__moves_available__ = [3, 5]
        
        moves = self.dice.get_available_moves()
        moves.append(99)  
        
        
        original_moves = self.dice.get_available_moves()
        self.assertNotIn(99, original_moves)
        self.assertEqual(len(original_moves), 2)
        

    @patch('random.randint')
    def test_multiple_rolls(self, mock_randint):
        
       
        mock_randint.side_effect = [1, 2]
        die1, die2 = self.dice.roll()
        self.assertEqual((die1, die2), (1, 2))
        
        # Segunda tirada (resetear el mock)
        mock_randint.side_effect = [6, 6]
        die1, die2 = self.dice.roll()
        self.assertEqual((die1, die2), (6, 6))
        self.assertTrue(self.dice.is_double())
        self.assertEqual(len(self.dice.get_available_moves()), 4)
    
    def test_partial_move_usage(self):
        
        
        self.dice._Dice__die1__ = 2
        self.dice._Dice__die2__ = 2
        self.dice._Dice__moves_available__ = [2, 2, 2, 2]
        
        
        self.assertTrue(self.dice.use_move(2))
        self.assertTrue(self.dice.use_move(2))
        
        
        self.assertTrue(self.dice.has_moves())
        self.assertEqual(len(self.dice.get_available_moves()), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
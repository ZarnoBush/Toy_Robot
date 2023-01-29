import unittest
import maze.hungry_joker_maze as obs

class ObstacleTest(unittest.TestCase):
    

        
    def test_position_blocking(self):
        
        test_coods = (130, -30)
        x, y = test_coods
        self.assertTrue(obs.is_position_blocked(x,y))
        
        
    def test_path_blocking(self):
        
        x1,x2,y1,y2 = 0,0, 0, 60
        self.assertTrue(obs.is_path_blocked(x1,x2,y1,y2))
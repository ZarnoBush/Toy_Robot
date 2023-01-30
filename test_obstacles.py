import unittest
import maze.obstacles as obs

class ObstacleTest(unittest.TestCase):
    
    def test_get_obstacles(self):
        
        return_value = obs.get_obstacles()
        self.assertIsInstance(return_value, tuple)
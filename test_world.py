import unittest
from world.text import world


class WorldTest(unittest.TestCase):
    
    def test_forward_north(self):
        testx,testy = (0,0)
        x,y = world.forward_command("N", "Hal", 20, False, False, testx, testy)
        self.assertEqual((x,y), (0,20))
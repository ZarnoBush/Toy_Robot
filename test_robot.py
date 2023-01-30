import unittest
import robot


class TestRobot(unittest.TestCase):
    
    def test_validate_command_mazerun(self):
        
        self.assertEqual(robot.validate_command("mazerun bottom"), True)
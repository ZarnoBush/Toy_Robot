import unittest
import robot
import sys
import io


class TestRobot(unittest.TestCase):
    
    def test_command_validation_for_mazerun(self):
        
        val = robot.validate_command("mazerun")
        
        self.assertEqual(val, True)
        
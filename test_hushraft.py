# test_hushraft.py
"""
Tests for HushRaft module.
"""

import unittest
from hushraft import HushRaft

class TestHushRaft(unittest.TestCase):
    """Test cases for HushRaft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HushRaft()
        self.assertIsInstance(instance, HushRaft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HushRaft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_prismaorm.py
"""
Tests for PrismaOrm module.
"""

import unittest
from prismaorm import PrismaOrm

class TestPrismaOrm(unittest.TestCase):
    """Test cases for PrismaOrm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrismaOrm()
        self.assertIsInstance(instance, PrismaOrm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrismaOrm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

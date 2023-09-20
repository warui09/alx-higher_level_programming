#!/usr/bin/python3
"""
Test module for the Base class
"""

import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """
    Test class for unit testing the Base class
    """
    def test_instantiation_without_id(self):
        """Test instance creation with id"""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_instantiation_with_id(self):
        """Test instance creation without id"""
        base_instance = Base(12)
        self.assertEqual(base_instance.id, 12)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Test module for the Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for unit testing the Base class
    """

    def test_instance_creation_with_id(self):
        """Test instance creation without id"""
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)

    def test_instance_creation_without_id(self):
        """Test instance creation with id"""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)


if __name__ == "__main__":
    unittest.main()

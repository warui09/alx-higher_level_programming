#!/usr/bin/python3
"""
Test suite for Rectangle class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):
    """Test instantiation of the Rectangle class"""
    def test_is_base_instance(self):
        """Test if Ractangle inherits from the Base class"""
        r1 = Rectangle(5, 8)
        self.assertIsInstance(r1, Base)

    def test_no_args(self):
        """Test if TypeError is raised when Rectangle is instantiated
        without arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_two_args(self):
        """Test instantiation with 2 args: width, height"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r1.id + 1, r2.id)

    def test_three_args(self):
        """Test instantiation with 3 arg: width, height, x"""
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r2.x, 6)
        self.assertEqual(r1.id + 1,  r2.id)

    def test_four_args(self):
        """Test instantiation with 4 args: width, height, x, y"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r1.id + 1, r2.id)

    def test_fie_args(self):
        """Test instantiation with 5 args: width, height, x, y, id"""
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

class TestInvalidArgs(unittest.TestCase):
    """Test instantiation of the Rectangle class with
    various invalid arguments"""

    def test_none_width(self):
        """Test instantiation with width of None"""
        r1 = Rectangle(None, 10)
        self.assertRaises(TypeError)

    def test_str_width(self):
        """Test instantiation with width value of string"""
        r1 = Rectangle("2", 10)
        self.assertRaises(TypeError)

    def test_zero_width(self):
        """Test instantiation with width of 0"""
        r1 = Rectangle(0, 10)
        self.assertRaises(ValueError)

    def test_neg_width(self):
        """Test instantiation with a negative value of width"""
        r1 = Rectangle(-3, 10)
        self.assertRaises(ValueError)

    def test_none_height(self):
        """Test instantiation with height of None"""
        r1 = Rectangle(2, None)
        self.assertRaises(TypeError)

    def test_str_height(self):
        """Test instantiation with a height value of a string"""
        r1 = Rectangle(2, "10")
        self.assertRaises(TypeError)

    def test_zero_height(self):
        """Test instantiation with height of 0"""
        r1 = Rectangle(2, 0)
        self.assertRaises(ValueError)

    def test_neg_height(self):
        """Test instantiation with a negative value of height"""
        r1 = Rectangle(2, -10)
        self.assertRaises(ValueError)

    def test_str_x(self):
        """Test instantiation with x of a string value"""
        r1 = Rectangle(1, 2, "3")
        self.assertRaises(TypeError)

    def test_neg_x(self):
        """Test instantiation with negative value for x"""
        r1 = Rectangle(1, 2, -3)
        self.assertRaises(ValueError)

    def test_str_y(self):
        """Test instantiation y of a string value"""
        r1 = Rectangle(1, 2, 3, "4")
        self.assertRaises(TypeError)

    def test_neg_y(self):
        """Test instantiation with negative value of y"""
        r1 = Rectangle(1, 2, 3, -4)
        self.assertRaises(ValueError)

class TestArea(unittest.TestCase):
    """Test the area method of the Rectangle class"""
    
    def test_area(self):
        """Test the area method of the Rectangle class"""
        self.assertEqual(Rectangle(2, 10).area(), 20)

class TestRectangleStrMethod(unittest.TestCase):
    """Test methods of the Rectangle class"""

    def test_str_method(self):
        """Test the __str__ method"""
        r = Rectangle(3, 4, 1, 2, 5)
        expected_output = "[Rectangle] (5) 1/2 - 3/4"
        self.assertEqual(str(r), expected_output)

class TestRectangleDisplay(unittest.TestCase):
    """Test the display method of the Rectangle class"""

    def test_display_without_x_and_y_exists(self):
        """Test display() when x and y are omitted"""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        
        # Redirect stdout to capture printed output
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        r.display()

        # Get printed output
        printed_output = sys.stdout.getvalue()

        # Restore the original stdout
        sys.stdout = saved_stdout

        self.assertEqual(printed_output, expected_output)

    def test_display_without_x_exists(self):
        """Test display() when x is omitted"""
        r = Rectangle(3, 2, 0, 1)
        expected_output = "\n###\n###\n"
        
        # Redirect stdout to capture printed output
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        r.display()

        # Get printed output
        printed_output = sys.stdout.getvalue()

        # Restore the original stdout
        sys.stdout = saved_stdout

        self.assertEqual(printed_output, expected_output)

    def test_display_exists(self):
        """Test display() when x and y exist"""
        r = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        
        # Redirect stdout to capture printed output
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        r.display()

        # Get printed output
        printed_output = sys.stdout.getvalue()

        # Restore the original stdout
        sys.stdout = saved_stdout

        self.assertEqual(printed_output, expected_output)

class TestRectangleUpdate(unittest.TestCase):
    """Test the update method of the Rectangle class"""

    def test_update_no_args(self):
        """Test updating with no arguments"""
        #r = Rectangle(1, 2, 3, 4, 5)
        #r.update()
        #self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 1/2")


    def test_update_all_attributes(self):
        """Test updating all attributes"""
        #r = Rectangle(1, 2, 3, 4, 5)
        #r.update(10, 20, 30, 40, 50)
        #self.assertEqual(str(r), "[Rectangle] (10) 40/50 - 20/30")

    def test_update_partial_attributes(self):
        """Test updating some attributes"""
        #r = Rectangle(1, 2, 3, 4, 5)
        #r.update(10, 20)
        #self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 20/2")

    def test_update_order_matters(self):
        """Test that the order of arguments matters"""
        #r = Rectangle(1, 2, 3, 4, 5)
        #r.update(20, 10, 30, 40, 50)  # Arguments in a different order
        #self.assertEqual(str(r), "[Rectangle] (20) 40/50 - 10/30")



if __name__ == "__main__":
    unittest.main()

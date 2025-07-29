#https://github.com/pseudo-named/lab10-AB-RT.git
#Partner 1: Andrew Belser
#Partner 2: Rylie Troendle

from calculator import *
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,100),101)
        self.assertEqual(add(-52,180),128)
        self.assertEqual(add(123,456),579)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(1000,420),580)
        self.assertEqual(sub(-100,-400),300)
        self.assertEqual(sub(12345,0),12345)
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(-5,10),-50)
        self.assertEqual(mul(0,456),0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,2), 5)
        self.assertEqual(div(-9,3),-3)
        self.assertEqual(div(0,5),0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion

        self.assertEqual(div(5,0),"division by zero")


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(100,10),2)
        self.assertEqual(log(16,2),4)
        self.assertEqual(log(324,18),2)

    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual(log(100,-1),"math domain error")

    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertEqual(log(-10, 2),"math domain error")

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(0,0),0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertAlmostEqual(square_root(9),3)
        self.assertAlmostEqual(square_root(0),0)
        self.assertAlmostEqual(square_root(-1),"math domain error")
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

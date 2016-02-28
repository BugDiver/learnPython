import unittest
from basic import is_even
from basic import is_odd
from basic import square
from basic import cube
from basic import simple_interest
from basic import sum_of_1_to_N
from basic import greatest_between_three
from basic import average_of_three

class basicTest(unittest.TestCase):
    def test_is_even(self):
        res = is_even(4)
        self.assertEqual(res , True)
        res = is_even(3)
        self.assertEqual(res ,False)

    def test_is_odd(self):
        res = is_odd(3)
        self.assertEqual(res , True)
        res = is_odd(4)
        self.assertEqual(res ,False)

    def test_square(self):
        res = square(3)
        self.assertEqual(res , 9)
        res = square(4)
        self.assertEqual(res ,16)
    def test_cube(self):
        res = cube(3)
        self.assertEqual(res , 27)
        res = cube(4)
        self.assertEqual(res ,64)

    def test_simple_interest(self):
        res = simple_interest(200 ,3 ,4)
        self.assertEqual(res ,24)

    def test_sum_of_1_to_N(self):
        res = sum_of_1_to_N(10)
        self.assertEqual(res ,55)

    def test_greatest_between_three(self):
        res = greatest_between_three(1 ,5 ,3)
        self.assertEqual(res ,5)

    def test_average_of_three(self):
        res = average_of_three(1 ,5 ,3)
        self.assertEqual(res ,3)
        res = average_of_three(2,3,3)
        self.assertEqual(res ,2.67)


if __name__ == '__main__':
    unittest.main()

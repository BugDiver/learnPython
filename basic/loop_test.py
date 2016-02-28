import unittest
from loop import gcd
from loop import lcm
from loop import compound_interest
from loop import factorial
from loop import fibonacci

class loopTest(unittest.TestCase):
    def test_gcd(self):
        res = gcd(4 ,8)
        self.assertEqual(res , 4)
        res = gcd(25 ,35 )
        self.assertEqual(res ,5)
        res = gcd(35,25 )
        self.assertEqual(res ,5)

    def test_lcm(self):
        res = lcm(4 ,8)
        self.assertEqual(res , 8)
        res = lcm(30 ,75 )
        self.assertEqual(res ,150)
        res = lcm(48 ,72 )
        self.assertEqual(res ,144)

    def test_compound_interest(self):
        res = compound_interest(1000,10,5)
        self.assertEqual(res ,610)

    def test_factorial(self):
        res = factorial(5)
        self.assertEqual(res ,120)

    def test_fibonacci(self):
        res = fibonacci(1)
        self.assertEqual(res ,0)
        res = fibonacci(2)
        self.assertEqual(res ,1)
        res = fibonacci(3)
        self.assertEqual(res ,1)
        res = fibonacci(4)
        self.assertEqual(res ,2)
        res = fibonacci(5)
        self.assertEqual(res ,3)
        res = fibonacci(6)
        self.assertEqual(res ,5)
        res = fibonacci(7)
        self.assertEqual(res ,8)
        res = fibonacci(8)
        self.assertEqual(res ,13)

if __name__ == '__main__':
    unittest.main()

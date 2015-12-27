import unittest

from map_reduce_filter import my_filter
from map_reduce_filter import my_map
from map_reduce_filter import my_reduce



list = [0,1,2,3,4,5,6,7,8,9,10]
def is_even(arg):
    if arg % 2==0:
        return True

def is_odd(arg):
    if arg % 2 != 0:
        return True

def increment(arg):
    return arg + 1

def add(n1 ,n2 ):
    return n1 + n2

def fibno(prev,index):
    if index < 2:
        prev.append(index)
    else:
         prev.append(prev[index-1]+prev[index-2])
    return prev

class arrayTest(unittest.TestCase):
    def test_filter(self):
        res = my_filter(list, is_even)
        self.assertEqual(res ,[0,2,4,6,8,10])
        res = my_filter(list ,is_odd)
        self.assertEqual(res ,[1,3,5,7,9])

    def test_map(self):
        res = my_map(list , increment)
        self.assertEqual(res , [1,2,3,4,5,6,7,8,9,10,11])

    def test_reduce(self):
        res = my_reduce(list,add ,0) # while initial value is provided
        self.assertEqual(res , 55)
        res = my_reduce(list , add ,None) # while initial value is not provided
        self.assertEqual(res ,55)
        res = my_reduce(range(8),fibno,[]) # while an array is passed as initial
        self.assertEqual(res[-1] ,13)

if __name__ == '__main__':
    unittest.main()

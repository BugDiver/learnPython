import unittest;
from  points import Point;

class PointTest(unittest.TestCase):
    def test_point_representation(self):
        p1 = Point(3,4);
        
        self.assertEqual(repr(p1) ,"[Point @x:3,y:4]");
        p2 = Point(0,3);
        self.assertEqual(repr(p2) ,"[Point @x:0,y:3]");
        p3 = Point(2,0);
        self.assertEqual(repr(p3) ,"[Point @x:2,y:0]");

    def test_point_representation_for_negative_coordinates(self):
        p1 = Point(-1,2);
        self.assertEqual(repr(p1) ,"[Point @x:-1,y:2]");
        p2 = Point(-1,-2);
        self.assertEqual(repr(p2) ,"[Point @x:-1,y:-2]");

    def test_point_should_be_equal_to_same_point(self):
        p1 = Point(3,4);
        p2 = Point(3,4);
        self.assertTrue(p1.equals(p2));
        self.assertTrue(p2.equals(p1));

    def test_point_should_not_be_equal_to_any_other_object(self):
        p1 = Point(3,4);
        fakePoint = {};
        fakePoint['__x'] = 3;
        fakePoint['__y'] = 4;
        try:
            self.assertFalse(p1.equals(fakePoint))
        except Exception, e:
            self.assertEqual(e.message ,str(fakePoint)+' is not Point instance');

    def test_point_should_give_distance_betwen_an_given_other_point(self):
        p1 = Point(1,2);
        p2 = Point(4,5);
        self.assertEqual(p1.distanceFrom(p2) ,4.24);

if __name__ == '__main__':
    unittest.main();
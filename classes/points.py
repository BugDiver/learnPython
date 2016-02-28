from math import sqrt

class Point(object):
	def __init__(self, start,end):
		self.__x =start;
		self.__y = end;

	def __repr__(self):
		return "[Point @x:"+str(self.__x)+",y:"+str(self.__y)+"]";

	def equals(self,point):
		if isinstance(point ,Point):
			return self.__x == point.__x and self.__y == point.__y;
		else:
			raise TypeError(str(point)+' is not Point instance');

	def distanceFrom(self,point):
		return round(sqrt(pow((self.__x-point.__x),2)+pow((self.__y-point.__y),2)) ,2);
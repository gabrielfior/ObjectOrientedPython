import math


class MyFirstClass:
    pass

class Point:
    '''Represents a point in 2 dimensional cartesian coordinates'''

    def __init__(self, x = 0, y = 0):
        '''Initialize the position of a new point. x and y can be specified. If not, default to the origin'''
        self.move(x,y)

    def reset(self):
        self.move(0,0)

    def move(self, x, y):
        '''Move point to new position in 2D space'''
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        '''Calculates Euclidian distance by means of Pythagorean Theorem. Distance returned as float'''
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y) ** 2
        )

# how to use it
p = Point()
print(p.x, p.y)
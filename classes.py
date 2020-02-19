"""
* Create a class called `Point` which has two instance variables,
`x` and `y` that represent the `x` and `y` co-ordinates respectively. 

* Initialize these instance variables in the `__init__` method

* Define a method, `distance` on `Point` which accepts another `Point` object as an argument and 
returns the distance between the two points.
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return (((self.x - point.x)**2) + ((self.y - point.y)**2))**0.5

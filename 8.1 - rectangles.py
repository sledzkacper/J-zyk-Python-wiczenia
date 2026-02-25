""" Klasa Rectangle (pod istniejącą już klasą Point z poprzednich zadań) """

from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # iloczyn skalarny

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2):
        self._left = min(x1, x2)
        self._right = max(x1, x2)
        self._bottom = min(y1, y2)
        self._top = max(y1, y2)

    @classmethod
    def from_points(cls, points):
        """Tworzy prostokąt z dwóch punktów: """
           
        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

   
    # podstawowe właściwośći
    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def bottom(self):
        return self._bottom

    @property
    def top(self):
        return self._top

    @property
    def width(self):
        return self._right - self._left

    @property
    def height(self):
        return self._top - self._bottom

    @property
    def area(self):
        return self.width * self.height

    @property
    def center(self):
        cx = self._left + self.width / 2
        cy = self._bottom + self.height / 2
        return Point(cx, cy)


    # Punkty narożne
    @property
    def topleft(self):
        return Point(self._left, self._top)

    @property
    def topright(self):
        return Point(self._right, self._top)

    @property
    def bottomleft(self):
        return Point(self._left, self._bottom)

    @property
    def bottomright(self):
        return Point(self._right, self._bottom)

    # pozostałe metody
    def move(self, dx=0, dy=0):
        self._left += dx
        self._right += dx
        self._bottom += dy
        self._top += dy

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (
            self.left == other.left and
            self.right == other.right and
            self.bottom == other.bottom and
            self.top == other.top
        )

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"Rectangle({self.left}, {self.bottom}, {self.right}, {self.top})"

    def __str__(self):
        return f"({self.left}, {self.bottom}, {self.right}, {self.top})"
    

# if __name__ == "__main__":
#     r = Rectangle(0, 0, 4, 3)
#     print("Area:", r.area)
#     print("Center:", r.center)
